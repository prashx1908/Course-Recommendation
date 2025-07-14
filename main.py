from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from difflib import get_close_matches
from typing import List, Optional

app = FastAPI()

# Allow CORS for local dev and frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the matrix
MATRIX_PATH = "corrected_specialization_matrix (1).csv"
df = pd.read_csv(MATRIX_PATH, index_col=0)
df.columns = df.columns.str.strip()
df.index = df.index.str.strip()

# Utility for fuzzy matching
def get_closest_valid(spec):
    all_specs = list(df.index)
    match = get_close_matches(spec, all_specs, n=1, cutoff=0.7)
    return match[0] if match else None

# Original recommendation logic (kept for backward compatibility)
def bridge_course_recommendation(from_spec, to_spec, threshold_strong=75, threshold_bridge=50):
    if from_spec not in df.index:
        suggested = get_closest_valid(from_spec)
        return {"error": f"Invalid specialization: {from_spec}. Did you mean: {suggested}?"}
    if to_spec not in df.columns:
        suggested = get_closest_valid(to_spec)
        return {"error": f"Invalid specialization: {to_spec}. Did you mean: {suggested}?"}

    base_score = float(df.loc[from_spec, to_spec])

    if base_score >= threshold_strong:
        return {
            "status": "✅ Strong Match",
            "score": base_score,
            "recommendation": to_spec,
            "reason": f"{to_spec} is highly relevant to your background in {from_spec}.",
            "alternatives": []
        }
    elif base_score >= threshold_bridge:
        from_scores = df.loc[from_spec].sort_values(ascending=False)
        to_scores = df[to_spec].sort_values(ascending=False)
        bridge_scores = {}
        for spec in df.columns:
            if spec != from_spec and spec != to_spec:
                f_score = from_scores.get(spec, 0)
                t_score = to_scores.get(spec, 0)
                hybrid = (f_score + t_score) / 2
                if hybrid >= threshold_bridge:
                    bridge_scores[spec] = hybrid
        if bridge_scores:
            best_bridge = sorted(bridge_scores.items(), key=lambda x: x[1], reverse=True)[0][0]
            suggestions = [k for k, _ in sorted(bridge_scores.items(), key=lambda x: x[1], reverse=True)[:3]]
            return {
                "status": "🔁 Bridge Match",
                "score": base_score,
                "recommendation": best_bridge,
                "reason": f"{best_bridge} bridges your background ({from_spec}) and your target ({to_spec}).",
                "alternatives": suggestions
            }
    from_scores = df.loc[from_spec].sort_values(ascending=False)
    fallback = from_scores.head(3)
    return {
        "status": "📌 Strategic Past Match",
        "score": base_score,
        "recommendation": fallback.index[0],
        "reason": f"{to_spec} has low alignment. {fallback.index[0]} is most aligned with your past in {from_spec}.",
        "alternatives": list(fallback.index)
    }

# Map common work roles to matrix-compatible specializations
work_to_specialization = {
    "software engineering": "Software Engineering",
    "counseling": "Psychology",
    "accounting": "Commerce",
    "retail banking": "Finance",
    "data analysis": "Data Science and Analytics",
    "project management": "Program/Project Management",
    "networking": "Information Technology",
    "customer service": "Hospitality and Tourism Management",
    "medical practice": "Medical Science",
    "teaching": "General Studies",
    "nursing": "Nursing",
    "pharmacy": "Pharmacy",
    "marketing": "Marketing",
    "legal practice": "Law",
    "civil site engineer": "Civil Engineering",
    "animation": "Arts",
    "web development": "Software Engineering",
    "database administration": "Information Technology",
    "quality assurance": "Software Engineering",
    "human resources": "Human Resource Management",
    "finance": "Finance",
    "operations": "Business Management",
    "research": "General Studies",
    "consulting": "Business Management",
    "sales": "Marketing",
    "administration": "Business Administration",
    # Add more as needed
}

# Tag each specialization as 'core' or 'non-core'
specialization_tags = {
    # Core technical/subject specializations
    "Computer Science": "core",
    "Artificial Intelligence": "core",
    "Data Science and Analytics": "core",
    "Information Technology": "core",
    "Computer Engineering": "core",
    "Software Engineering": "core",
    "Electronics Engineering": "core",
    "Electrical Engineering": "core",
    "Mechanical Engineering": "core",
    "Civil Engineering": "core",
    "Chemical Engineering": "core",
    "Biotechnology": "core",
    "Life Sciences": "core",
    "Physical Sciences": "core",
    "Mathematics": "core",
    "Physics": "core",
    "Chemistry": "core",
    "Architecture": "core",
    "Pharmacy": "core",
    "Medical Science": "core",
    "Nursing": "core",
    "Physiotherapy": "core",
    "Agricultural Science": "core",
    "Electronics and Communication Engineering": "core",
    "Mechanical and Mechatronics Engineering": "core",
    "Civil and Structural Engineering": "core",
    "Biotechnology and Biomedical Engineering": "core",
    # Core social sciences/humanities
    "Law": "core",
    "Political Science": "core",
    "Psychology": "core",
    "Sociology": "core",
    "Arts": "core",
    "Language and Literature": "core",
    # Non-core/generalist/business/management
    "Business Administration": "non-core",
    "Business Management": "non-core",
    "Finance": "non-core",
    "Accounts": "non-core",
    "Marketing": "non-core",
    "Human Resource Management": "non-core",
    "Economics": "non-core",
    "Commerce": "non-core",
    "Hospitality and Tourism Management": "non-core",
    "General Studies": "non-core",
    "Diploma (General)": "non-core",
    "Computer Information Systems": "non-core",
    "Business Analytics": "non-core",
    "Financial Management": "non-core",
    "Marketing Management": "non-core",
    "Human Resource Development": "non-core",
    "Program/Project Management": "non-core",
}

def get_tag(spec):
    return specialization_tags.get(spec, "non-core")

# Enhanced work roles parameter parsing
def parse_work_roles_param(work_roles_param):
    """
    Parse work roles parameter: 'role1:years1,role2:years2,...'
    """
    roles = []
    if not work_roles_param:
        return roles
    
    for part in work_roles_param.split(','):
        part = part.strip()
        if ':' in part:
            role, years = part.split(':', 1)
            try:
                years = int(years.strip())
            except ValueError:
                years = 0
            roles.append({'role': role.strip(), 'years': years})
        else:
            roles.append({'role': part, 'years': 0})
    
    return roles

# Enhanced recommendation logic with proper work experience weighting
def recommend_course_with_work(education, work_experiences, target, 
                             direct_threshold=100, achievable_threshold=70, 
                             bridge_threshold=50, minimum_threshold=30):
    """
    Enhanced recommendation logic following the specified flow:
    1. Direct Match (100%) - Education or Work Experience exactly matches target
    2. High Relevancy (≥70%) - At least one background has high relevancy to target
    3. Bridge Programs (50-69%) - Find intermediate programs between backgrounds and target
    4. Fallback (<50%) - Show best available path (prioritize work exp with more years)
    """
    
    # Map work experiences to specializations
    mapped_work_specs = []
    for w in work_experiences:
        work_role = w['role'].lower().strip()
        years = w.get('years', 0)
        
        # Try to map from work_to_specialization first
        mapped = work_to_specialization.get(work_role)
        if mapped and mapped in df.index:
            mapped_work_specs.append({'spec': mapped, 'years': years, 'original_role': w['role']})
        # If direct role name exists in matrix
        elif w['role'] in df.index:
            mapped_work_specs.append({'spec': w['role'], 'years': years, 'original_role': w['role']})
        # Try fuzzy matching
        else:
            fuzzy_match = get_closest_valid(w['role'])
            if fuzzy_match:
                mapped_work_specs.append({'spec': fuzzy_match, 'years': years, 'original_role': w['role']})
    
    # Validate inputs
    if education not in df.index:
        suggestion = get_closest_valid(education)
        return {"error": f"Invalid education specialization: {education}. Did you mean: {suggestion}?"}
    
    if target not in df.columns:
        suggestion = get_closest_valid(target)
        return {"error": f"Invalid target specialization: {target}. Did you mean: {suggestion}?"}
    
    # Get relevancy scores
    edu_score = float(df.loc[education, target])
    work_scores = []
    
    for w in mapped_work_specs:
        if w['spec'] in df.index:
            score = float(df.loc[w['spec'], target])
            work_scores.append((w['spec'], score, w['years'], w['original_role']))
    
    # 1. DIRECT MATCH (100% match)
    # Check education first
    if education == target or edu_score >= direct_threshold:
        return {
            "match_type": "direct",
            "category": "Direct Match",
            "score": 100.0 if education == target else round(edu_score, 2),
            "message": f"🎯 {target} is a direct match with your educational background in {education}.",
            "recommendation": target,
            "alternatives": [{"name": target, "tag": get_tag(target)}],
            "bridge_programs": [],
            "source": "education"
        }
    
    # Check work experiences
    for wspec, score, years, original_role in work_scores:
        if wspec == target or score >= direct_threshold:
            years_text = f" ({years} years)" if years > 0 else ""
            return {
                "match_type": "direct",
                "category": "Direct Match",
                "score": 100.0 if wspec == target else round(score, 2),
                "message": f"🎯 {target} is a direct match with your work experience in {original_role}{years_text}.",
                "recommendation": target,
                "alternatives": [{"name": target, "tag": get_tag(target)}],
                "bridge_programs": [],
                "source": "work_experience"
            }
    
    # 2. HIGH RELEVANCY MATCH (≥70% match)
    # Combine all backgrounds with enhanced weighting for work experience
    all_backgrounds = [("Education", education, edu_score, 0, education)]
    
    for wspec, score, years, original_role in work_scores:
        all_backgrounds.append(("Work", wspec, score, years, original_role))
    
    # Filter high relevancy matches
    high_matches = [bg for bg in all_backgrounds if bg[2] >= achievable_threshold]
    
    if high_matches:
        # Sort by score first, then by years (for work experience prioritization)
        # Give higher priority to work experience with more years
        def sort_key(bg):
            score = bg[2]
            years = bg[3]
            # Boost work experience scores based on years
            if bg[0] == "Work":
                year_bonus = min(years * 2, 10)  # Max 10 point bonus for experience
                return (score + year_bonus, years)
            return (score, 0)
        
        high_matches.sort(key=sort_key, reverse=True)
        best = high_matches[0]
        
        years_text = f" ({best[3]} years)" if best[0] == "Work" and best[3] > 0 else ""
        source_text = best[4] if best[0] == "Work" else best[1]
        
        return {
            "match_type": "achievable",
            "category": "High Relevancy Match",
            "score": round(best[2], 2),
            "message": f"🎯 {target} is highly achievable based on your {best[0].lower()} in {source_text}{years_text}. Relevancy score: {round(best[2], 2)}%",
            "recommendation": target,
            "alternatives": [{"name": target, "tag": get_tag(target)}],
            "bridge_programs": [],
            "source": "education" if best[0] == "Education" else "work_experience"
        }
    
    # 3. BRIDGE PROGRAMS (intermediate programs between backgrounds and target)
    bridge_scores = {}
    
    # Create weighted backgrounds for bridge calculation
    weighted_backgrounds = [(education, 1.0)]  # Base weight for education
    
    for w in mapped_work_specs:
        # Progressive weighting based on years of experience
        if w['years'] <= 1:
            weight = 1.2
        elif w['years'] <= 3:
            weight = 1.8
        elif w['years'] <= 5:
            weight = 2.2
        else:
            weight = 2.5
        
        weighted_backgrounds.append((w['spec'], weight))
    
    # Calculate bridge scores for each potential intermediate program
    for prog in df.columns:
        # Skip if program is same as any background or target
        if prog == education or prog == target:
            continue
        if any(w['spec'] == prog for w in mapped_work_specs):
            continue
        
        # Score from bridge program to target
        if prog in df.index and target in df.columns:
            to_target_value = df.loc[prog, target]
            if isinstance(to_target_value, pd.Series):
                to_target_value = to_target_value.iloc[0]
            to_target = float(to_target_value)
        else:
            continue
        
        # Weighted score from backgrounds to bridge program
        weighted_bg_score = 0
        total_weight = 0
        
        for bg_spec, weight in weighted_backgrounds:
            if prog in df.index and bg_spec in df.columns:
                bg_value = df.loc[prog, bg_spec]
                if isinstance(bg_value, pd.Series):
                    bg_value = bg_value.iloc[0]
                bg_score = float(bg_value)
                weighted_bg_score += bg_score * weight
                total_weight += weight
        
        if total_weight > 0:
            avg_bg_score = weighted_bg_score / total_weight
            
            # Only consider as bridge if both directions have reasonable scores
            if to_target >= bridge_threshold and avg_bg_score >= bridge_threshold:
                # Use harmonic mean to favor programs good at both bridging and leading to target
                bridge_score = 2 * (to_target * avg_bg_score) / (to_target + avg_bg_score)
                bridge_scores[prog] = bridge_score
    
    # Return top 5 bridge programs if found
    if bridge_scores:
        top_bridges = sorted(bridge_scores.items(), key=lambda x: x[1], reverse=True)[:5]
        
        bridge_programs = [
            {"name": prog, "score": round(score, 2), "tag": get_tag(prog)} 
            for prog, score in top_bridges
        ]
        
        return {
            "match_type": "bridge",
            "category": "Bridge Programs",
            "score": round(top_bridges[0][1], 2),
            "message": f"No direct high match found. These bridge programs can help transition from your background to {target}:",
            "recommendation": top_bridges[0][0],
            "alternatives": bridge_programs,
            "bridge_programs": bridge_programs,
            "source": "bridge"
        }
    
    # 4. FALLBACK - Show best available path
    # Priority: Work experience with most years OR highest score > Education
    
    best_path = None
    best_score = edu_score
    best_source = "education"
    best_description = education
    
    # Check if any work experience is better than education
    if mapped_work_specs:
        # Find best work experience (prioritize by years, then by score)
        for w in mapped_work_specs:
            if w['spec'] in df.index:
                work_score = float(df.loc[w['spec'], target])
                
                # Work experience is better if:
                # 1. It has more than 2 years of experience, OR
                # 2. It has a higher score than education
                if w['years'] > 2 or work_score > best_score:
                    if best_path is None or w['years'] > best_path['years'] or work_score > best_score:
                        best_path = w
                        best_score = work_score
                        best_source = "work_experience"
                        best_description = f"{w['original_role']} ({w['years']} years)"
    
    if best_path:
        return {
            "match_type": "fallback",
            "category": "Best Available Path (Work Experience)",
            "score": round(best_score, 2),
            "message": f"Limited alignment found. Your work experience in {best_path['original_role']} ({best_path['years']} years) provides the best foundation for transitioning to {target}.",
            "recommendation": best_path['spec'],
            "alternatives": [{"name": best_path['spec'], "tag": get_tag(best_path['spec'])}],
            "bridge_programs": [],
            "source": "work_experience"
        }
    
    # Final fallback to education
    return {
        "match_type": "fallback",
        "category": "Best Available Path (Education)",
        "score": round(best_score, 2),
        "message": f"Limited alignment found. Your educational background in {education} provides the foundation for transitioning to {target}.",
        "recommendation": education,
        "alternatives": [{"name": education, "tag": get_tag(education)}],
        "bridge_programs": [],
        "source": "education"
    }

# Detailed breakdown function
def get_detailed_breakdown(education, work_experiences, target):
    """
    Provides detailed breakdown of how each background relates to target
    """
    breakdown = []
    
    # Education breakdown
    if education in df.index and target in df.columns:
        edu_score = float(df.loc[education, target])
        breakdown.append({
            "type": "Education",
            "specialization": education,
            "original_input": education,
            "score": round(edu_score, 2),
            "years": 0,
            "tag": get_tag(education),
            "match_level": "direct" if edu_score >= 100 else "high" if edu_score >= 70 else "medium" if edu_score >= 50 else "low"
        })
    
    # Work experience breakdown
    for i, w in enumerate(work_experiences):
        work_role = w['role'].lower().strip()
        years = w.get('years', 0)
        
        # Map to specialization
        mapped = work_to_specialization.get(work_role, w['role'])
        if mapped not in df.index:
            mapped = get_closest_valid(w['role'])
        
        if mapped and mapped in df.index and target in df.columns:
            work_score = float(df.loc[mapped, target])
            breakdown.append({
                "type": f"Work Experience {i+1}",
                "specialization": mapped,
                "original_input": w['role'],
                "score": round(work_score, 2),
                "years": years,
                "tag": get_tag(mapped),
                "match_level": "direct" if work_score >= 100 else "high" if work_score >= 70 else "medium" if work_score >= 50 else "low"
            })
    
    return {
        "target": target,
        "target_tag": get_tag(target),
        "breakdown": breakdown,
        "summary": {
            "total_backgrounds": len(breakdown),
            "direct_matches": len([b for b in breakdown if b["match_level"] == "direct"]),
            "high_matches": len([b for b in breakdown if b["match_level"] == "high"]),
            "medium_matches": len([b for b in breakdown if b["match_level"] == "medium"]),
            "low_matches": len([b for b in breakdown if b["match_level"] == "low"])
        }
    }

# API Endpoints
@app.get("/specializations", response_model=List[str])
def get_specializations():
    """Get all available specializations"""
    return sorted(list(df.index))

@app.get("/targets", response_model=List[str])
def get_targets():
    """Get all available target programs"""
    return sorted(list(df.columns))

@app.get("/work_roles", response_model=List[str])
def get_work_roles():
    """Get all available work roles (mapped + direct specializations)"""
    work_roles = set(work_to_specialization.keys())
    all_specs = set(df.index)
    all_roles = sorted(work_roles.union(all_specs))
    return all_roles

@app.get("/recommend")
def recommend(from_spec: str = Query(...), to_spec: str = Query(...)):
    """Original recommendation endpoint (backward compatibility)"""
    return bridge_course_recommendation(from_spec, to_spec)

@app.get("/recommend_multi")
def recommend_multi(
    education_spec: str = Query(..., description="Educational specialization"),
    work_roles: Optional[str] = Query(None, description="Work roles as 'role1:years1,role2:years2'"),
    target_spec: str = Query(..., description="Target specialization")
):
    """
    Enhanced multi-factor recommendation endpoint
    
    Args:
        education_spec: Educational background specialization
        work_roles: Comma-separated work roles with years (format: 'role1:years1,role2:years2')
        target_spec: Target specialization to transition to
    
    Returns:
        Detailed recommendation with match type, score, and alternatives
    """
    work_experiences = parse_work_roles_param(work_roles) if work_roles else []
    return recommend_course_with_work(education_spec, work_experiences, target_spec)

@app.get("/match_breakdown")
def match_breakdown(
    education_spec: str = Query(..., description="Educational specialization"),
    work_roles: Optional[str] = Query(None, description="Work roles as 'role1:years1,role2:years2'"),
    target_spec: str = Query(..., description="Target specialization")
):
    """
    Get detailed breakdown of how each background relates to target
    """
    work_experiences = parse_work_roles_param(work_roles) if work_roles else []
    return get_detailed_breakdown(education_spec, work_experiences, target_spec)

@app.get("/relevancy_breakdown")
def relevancy_breakdown(
    education_spec: str = Query(...),
    work_roles: Optional[str] = Query(None),
    target_spec: str = Query(...)
):
    """Legacy endpoint for backward compatibility"""
    work_roles_list = parse_work_roles_param(work_roles) if work_roles else []
    backgrounds = [("Education", education_spec, 0)] + [(f"Work {i+1}", w['role'], w['years']) for i, w in enumerate(work_roles_list)]
    results = []
    
    for label, bg, years in backgrounds:
        mapped = work_to_specialization.get(bg.lower().strip(), bg)
        if mapped not in df.index:
            suggestion = get_closest_valid(mapped)
            score = None
            tag = None
        else:
            score = float(df.loc[mapped, target_spec]) if target_spec in df.columns else None
            tag = get_tag(mapped)
        
        results.append({
            "source": bg,
            "label": label,
            "score": score,
            "tag": tag,
            "years": years
        })
    
    return {
        "relevancies": results,
        "target": target_spec,
        "target_tag": get_tag(target_spec) if target_spec in df.columns else None
    }

@app.get("/")
def root():
    """Root endpoint with API information"""
    return {
        "message": "Course Recommendation API",
        "version": "2.0",
        "endpoints": {
            "/specializations": "Get all specializations",
            "/targets": "Get all target programs", 
            "/work_roles": "Get all work roles",
            "/recommend_multi": "Get course recommendations based on education and work experience",
            "/match_breakdown": "Get detailed breakdown of background relevancy",
            "/recommend": "Original recommendation endpoint",
            "/relevancy_breakdown": "Legacy relevancy breakdown"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
