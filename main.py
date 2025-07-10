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

# Recommendation logic

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

# Enhanced recommend logic for work roles

def parse_work_roles_param(work_roles_param):
    # work_roles_param: 'role1:years1,role2:years2,...'
    roles = []
    if not work_roles_param:
        return roles
    for part in work_roles_param.split(','):
        if ':' in part:
            role, years = part.split(':', 1)
            try:
                years = int(years)
            except Exception:
                years = 0
            roles.append({'role': role.strip(), 'years': years})
        else:
            roles.append({'role': part.strip(), 'years': 0})
    return roles

def recommend_course_with_work(education, work_experiences, target, strong_threshold=90, achievable_threshold=70, bridge_threshold=40, core_bias_margin=5):
    mapped_work_specs = []
    for w in work_experiences:
        work = w['role']
        years = w.get('years', 0)
        mapped = work_to_specialization.get(work.lower().strip())
        if mapped and mapped in df.index:
            mapped_work_specs.append({'spec': mapped, 'years': years})
        elif work in df.index:
            mapped_work_specs.append({'spec': work, 'years': years})
    if education not in df.index:
        suggestion = get_closest_valid(education)
        return {"error": f"Invalid education specialization: {education}. Did you mean: {suggestion}?"}
    if target not in df.columns:
        suggestion = get_closest_valid(target)
        return {"error": f"Invalid target specialization: {target}. Did you mean: {suggestion}?"}
    edu_score = float(df.loc[education, target])
    work_scores = [(w['spec'], float(df.loc[w['spec'], target]), w['years']) for w in mapped_work_specs if w['spec'] in df.index]

    # 1. Direct match
    if education == target or any(w['spec'] == target for w in mapped_work_specs):
        return {
            "match_type": "direct",
            "category": "Direct Match",
            "score": 100.0,
            "message": f"🎯 {target} is a direct match with your background or work experience.",
            "alternatives": [{"name": target, "tag": get_tag(target)}]
        }

    # 2. High match (>= 70)
    if edu_score >= achievable_threshold or any(score >= achievable_threshold for _, score, _ in work_scores):
        best_score = max([edu_score] + [score for _, score, _ in work_scores])
        return {
            "match_type": "achievable",
            "category": "Achievable Match",
            "score": round(best_score, 2),
            "message": f"🎯 {target} is highly achievable based on your background or work experience.",
            "alternatives": [{"name": target, "tag": get_tag(target)}]
        }

    # 3. Fallback: No strong match, show 5 best alternatives (core preferred)
    weighted_scores = {}
    for prog in df.columns:
        if prog == education and prog != target:
            continue  # skip user's own background unless it's the target
        edu_val = float(df.loc[education, prog]) if education in df.index else 0
        work_vals = []
        for w in mapped_work_specs:
            wval = float(df.loc[w['spec'], prog]) if w['spec'] in df.index else 0
            weight = 2.0 if w['years'] > 2 else 1.2
            work_vals.append(wval * weight)
        weighted = edu_val * 1.0 + sum(work_vals)
        weighted_scores[prog] = weighted
    filtered = [(prog, score) for prog, score in weighted_scores.items() if score >= 20]
    if not filtered:
        # 4. Very low match: show only the single best
        best_prog, best_score = max(weighted_scores.items(), key=lambda x: x[1])
        return {
            "match_type": "low",
            "category": "Low Match",
            "score": round(best_score, 2),
            "message": f"No strong or high match found. {best_prog} is the most relevant program to your background.",
            "alternatives": [{"name": best_prog, "tag": get_tag(best_prog)}]
        }
    filtered.sort(key=lambda x: (get_tag(x[0]) != 'core', -x[1]))  # core first, then by score desc
    top_alts = filtered[:5]
    return {
        "match_type": "fallback",
        "category": "Fallback (Core Preferred)",
        "score": round(top_alts[0][1], 2) if top_alts else 0,
        "message": f"No strong or high match found. These programs are most aligned with your background (core programs preferred).",
        "alternatives": [{"name": spec, "tag": get_tag(spec)} for spec, _ in top_alts]
    }

@app.get("/specializations", response_model=List[str])
def get_specializations():
    return list(df.index)

@app.get("/targets", response_model=List[str])
def get_targets():
    return list(df.columns)

@app.get("/recommend")
def recommend(from_spec: str = Query(...), to_spec: str = Query(...)):
    return bridge_course_recommendation(from_spec, to_spec)

@app.get("/recommend_multi")
def recommend_multi(
    education_spec: str = Query(...),
    work_roles: Optional[str] = Query(None),
    target_spec: str = Query(...)
):
    # work_roles is a comma-separated string, each as 'role:years'
    work_experiences = parse_work_roles_param(work_roles) if work_roles else []
    return recommend_course_with_work(education_spec, work_experiences, target_spec)

@app.get("/work_roles", response_model=List[str])
def get_work_roles():
    # All keys from work_to_specialization (user-friendly work roles)
    work_roles = set(work_to_specialization.keys())
    # All unique specializations from the CSV (for advanced users)
    all_specs = set(df.index)
    # Combine and sort
    all_roles = sorted(work_roles.union(all_specs))
    return all_roles

@app.get("/relevancy_breakdown")
def relevancy_breakdown(
    education_spec: str = Query(...),
    work_roles: Optional[str] = Query(None),
    target_spec: str = Query(...)
):
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
            tag = get_tag(target_spec) if target_spec in df.columns else None
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