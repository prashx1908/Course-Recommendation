from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from difflib import get_close_matches
from typing import List, Optional
import numpy as np

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
MATRIX_PATH = "mapp_matrix.csv"
df = pd.read_csv(MATRIX_PATH, index_col=0)
df.columns = df.columns.str.strip()
df.index = df.index.str.strip()

# Map common work roles to matrix-compatible specializations
work_to_specialization = {
    "software engineering": "Software Development",
    "software development": "Software Development",
    "web development": "Web Design",
    "mobile development": "Mobile Application",
    "data analysis": "Data Science and Analytics",
    "data science": "Data Science and Analytics",
    "machine learning": "Machine Learning",
    "artificial intelligence": "Artificial Intelligence",
    "project management": "Project Management",
    "business analysis": "Business Analysis",
    "networking": "Networking",
    "cybersecurity": "Cyber Security",
    "database administration": "Information Technology",
    "quality assurance": "Software Testing",
    "human resources": "Human Resource Management",
    "marketing": "Marketing",
    "sales": "Sales",
    "finance": "Finance",
    "accounting": "Accounts",
    "teaching": "General Studies",
    "nursing": "Nursing",
    "pharmacy": "Pharmacy",
    "civil engineering": "Civil Engineering",
    "mechanical engineering": "Mechanical Engineering",
    "electrical engineering": "Electrical Engineering",
    "electronics engineering": "Electronics Engineering",
    "chemical engineering": "Chemical Engineering",
    "research": "General Studies",
    "consulting": "Business Management",
    "operations": "Operations",
    "administration": "Business Administration",
}

# Utility functions
def get_closest_valid(spec):
    all_specs = list(df.index)
    match = get_close_matches(spec, all_specs, n=1, cutoff=0.6)
    return match[0] if match else None

def parse_work_roles_param(work_roles_param):
    """Parse work roles parameter: 'role1:years1,role2:years2,...'"""
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
            roles.append({'role': part.strip(), 'years': 0})
    
    return roles

def get_specialization_score(from_spec, to_spec):
    """Get score between two specializations"""
    if from_spec not in df.index or to_spec not in df.columns:
        return 0
    
    try:
        score = df.loc[from_spec, to_spec]
        return float(score) if not pd.isna(score) else 0
    except:
        return 0

def recommend_course_with_work(education, work_experiences, target):
    """
    Enhanced recommendation logic following exact requirements:
    1. Direct Match (100%) - Show target only
    2. High Relevancy (≥75%) - Show target only 
    3. Bridge Programs (50 < score < 74) - Show 5 bridge programs
    4. Fallback (≤50) - Show best from education/work experience
    """
    
    # Input validation
    if education not in df.index:
        suggestion = get_closest_valid(education)
        return {
            "error": f"Invalid education specialization: {education}",
            "suggestion": suggestion
        }
    
    if target not in df.columns:
        suggestion = get_closest_valid(target)
        return {
            "error": f"Invalid target specialization: {target}",
            "suggestion": suggestion
        }
    
    # Map work experiences to specializations
    mapped_work_specs = []
    for w in work_experiences:
        work_role = w['role'].lower().strip()
        years = w.get('years', 0)
        
        # Try mapping from work_to_specialization
        mapped = work_to_specialization.get(work_role)
        if mapped and mapped in df.index:
            mapped_work_specs.append({
                'spec': mapped, 
                'years': years, 
                'original_role': w['role']
            })
        # Try direct match
        elif w['role'] in df.index:
            mapped_work_specs.append({
                'spec': w['role'], 
                'years': years, 
                'original_role': w['role']
            })
        # Try fuzzy matching
        else:
            fuzzy_match = get_closest_valid(w['role'])
            if fuzzy_match:
                mapped_work_specs.append({
                    'spec': fuzzy_match, 
                    'years': years, 
                    'original_role': w['role']
                })
    
    # Get all relevancy scores
    edu_score = get_specialization_score(education, target)
    work_scores = []
    
    for w in mapped_work_specs:
        score = get_specialization_score(w['spec'], target)
        work_scores.append({
            'spec': w['spec'],
            'score': score,
            'years': w['years'],
            'original_role': w['original_role']
        })
    
    # Combine all backgrounds
    all_backgrounds = [{'type': 'education', 'spec': education, 'score': edu_score, 'years': 0}]
    for w in work_scores:
        all_backgrounds.append({
            'type': 'work', 
            'spec': w['spec'], 
            'score': w['score'], 
            'years': w['years'],
            'original_role': w['original_role']
        })
    
    # 1. DIRECT MATCH (>= 75% match)
    direct_matches = [bg for bg in all_backgrounds if bg['score'] >= 75]
    if direct_matches:
        best_direct = max(direct_matches, key=lambda x: x['score'])
        if best_direct['type'] == 'education':
            message = f"🎯 Perfect match! {target} directly aligns with your educational background in {education}."
        else:
            years_text = f" ({best_direct['years']} years)" if best_direct['years'] > 0 else ""
            message = f"🎯 Perfect match! {target} directly aligns with your work experience in {best_direct['original_role']}{years_text}."
        return {
            "match_type": "direct",
            "category": "Direct Match",
            "score": round(best_direct['score'], 2),
            "message": message,
            "recommendation": target,
            "alternatives": [],
            "bridge_programs": [],
            "source": best_direct['type']
        }

    # 2. BRIDGE PROGRAMS (50 <= score <= 75)
    bridge_matches = [bg for bg in all_backgrounds if 50 <= bg['score'] <= 75]
    if bridge_matches:
        bridge_programs = []
        for bridge_spec in df.columns:
            if bridge_spec == target or bridge_spec == education:
                continue
            if any(w['spec'] == bridge_spec for w in mapped_work_specs):
                continue
            bridge_to_target = get_specialization_score(bridge_spec, target)
            if bridge_to_target <= 60:
                continue
            valid_backgrounds = []
            for bg in all_backgrounds:
                bg_to_bridge = get_specialization_score(bg['spec'], bridge_spec)
                if bg_to_bridge > 60:
                    valid_backgrounds.append(bg_to_bridge)
            if valid_backgrounds:
                avg_background_score = sum(valid_backgrounds) / len(valid_backgrounds)
                composite_score = (avg_background_score + bridge_to_target) / 2
                if composite_score > 55:
                    bridge_programs.append({
                        'name': bridge_spec,
                        'composite_score': round(composite_score, 2),
                        'relevance_to_target': round(bridge_to_target, 2),
                        'relevance_from_background': round(max(valid_backgrounds), 2)
                    })
        bridge_programs.sort(key=lambda x: x['composite_score'], reverse=True)
        bridge_programs = bridge_programs[:5]
        if bridge_programs:
            best_bridge_score = max(bg['score'] for bg in bridge_matches)
            return {
                "match_type": "bridge",
                "category": "Bridge Programs",
                "score": round(best_bridge_score, 2),
                "message": f"Consider these bridge programs to transition from your background to {target}:",
                "recommendation": bridge_programs[0]['name'],
                "alternatives": bridge_programs,
                "bridge_programs": bridge_programs,
                "source": "bridge"
            }
    
    # 4. FALLBACK (≤50) - Show best from education/work
    # Find the best available path
    best_background = max(all_backgrounds, key=lambda x: (x['score'], x['years'] if x['type'] == 'work' else 0))
    
    if best_background['type'] == 'education':
        message = f"Limited alignment found. Your educational background in {education} provides the best foundation."
        recommendation = education
    else:
        years_text = f" ({best_background['years']} years)" if best_background['years'] > 0 else ""
        message = f"Limited alignment found. Your work experience in {best_background['original_role']}{years_text} provides the best foundation."
        recommendation = best_background['spec']
    
    return {
        "match_type": "fallback",
        "category": "Best Available Path",
        "score": round(best_background['score'], 2),
        "message": message,
        "recommendation": recommendation,
        "alternatives": [{"name": recommendation}],
        "bridge_programs": [],
        "source": best_background['type']
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
    """Get all available work roles"""
    work_roles = set(work_to_specialization.keys())
    all_specs = set(df.index)
    return sorted(list(work_roles.union(all_specs)))

@app.get("/recommend_multi")
def recommend_multi(
    education_spec: str = Query(..., description="Educational specialization"),
    work_roles: Optional[str] = Query(None, description="Work roles as 'role1:years1,role2:years2'"),
    target_spec: str = Query(..., description="Target specialization")
):
    """Multi-factor recommendation endpoint"""
    work_experiences = parse_work_roles_param(work_roles) if work_roles else []
    return recommend_course_with_work(education_spec, work_experiences, target_spec)

@app.get("/match_breakdown")
def match_breakdown(
    education_spec: str = Query(..., description="Educational specialization"),
    work_roles: Optional[str] = Query(None, description="Work roles as 'role1:years1,role2:years2'"),
    target_spec: str = Query(..., description="Target specialization")
):
    """Get detailed breakdown of background relevancy"""
    work_experiences = parse_work_roles_param(work_roles) if work_roles else []
    
    breakdown = []
    
    # Education breakdown
    if education_spec in df.index and target_spec in df.columns:
        edu_score = get_specialization_score(education_spec, target_spec)
        breakdown.append({
            "type": "Education",
            "specialization": education_spec,
            "score": round(edu_score, 2),
            "years": 0,
            "match_level": "direct" if edu_score >= 100 else "high" if edu_score >= 80 else "medium" if edu_score >= 50 else "low"
        })
    
    # Work experience breakdown
    for i, w in enumerate(work_experiences):
        work_role = w['role'].lower().strip()
        years = w.get('years', 0)
        
        mapped = work_to_specialization.get(work_role, w['role'])
        if mapped not in df.index:
            mapped = get_closest_valid(w['role'])
        
        if mapped and mapped in df.index:
            work_score = get_specialization_score(mapped, target_spec)
            breakdown.append({
                "type": f"Work Experience {i+1}",
                "specialization": mapped,
                "original_input": w['role'],
                "score": round(work_score, 2),
                "years": years,
                "match_level": "direct" if work_score >= 100 else "high" if work_score >= 80 else "medium" if work_score >= 50 else "low"
            })
    
    return {
        "target": target_spec,
        "breakdown": breakdown,
        "summary": {
            "total_backgrounds": len(breakdown),
            "direct_matches": len([b for b in breakdown if b["match_level"] == "direct"]),
            "high_matches": len([b for b in breakdown if b["match_level"] == "high"]),
            "medium_matches": len([b for b in breakdown if b["match_level"] == "medium"]),
            "low_matches": len([b for b in breakdown if b["match_level"] == "low"])
        }
    }

@app.get("/")
def root():
    """Root endpoint with API information"""
    return {
        "message": "Course Recommendation API",
        "version": "3.0",
        "endpoints": {
            "/specializations": "Get all specializations",
            "/targets": "Get all target programs", 
            "/work_roles": "Get all work roles",
            "/recommend_multi": "Get course recommendations",
            "/match_breakdown": "Get detailed breakdown"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
