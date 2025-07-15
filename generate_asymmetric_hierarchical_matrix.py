import pandas as pd

# --- SAMPLE courses_db (replace/expand with your full mapping) ---
courses_db = {
    'Computer Science': {'level': 'undergraduate', 'domain': 'computer_science', 'subdomain': 'software_engineering', 'specialty': 'cs_general'},
    'Project Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'project_management', 'specialty': 'pm_general'},
    'Electronics Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'electronics', 'specialty': 'electronics_general'},
    'Artificial Intelligence': {'level': 'postgraduate', 'domain': 'computer_science', 'subdomain': 'artificial_intelligence', 'specialty': 'ai_general'},
    'Business Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'ba_general'},
    # ... add all your mapped courses here ...
}

course_names = list(courses_db.keys())

# --- SMART, ASYMMETRIC, HIERARCHICAL RELEVANCY FUNCTION ---
def get_relevancy(source, target):
    if source not in courses_db or target not in courses_db:
        return None  # Ignore unmapped
    s = courses_db[source]
    t = courses_db[target]
    if source == target:
        return 100
    # Exact specialty (not same course)
    if s['domain'] == t['domain'] and s['subdomain'] == t['subdomain'] and s['specialty'] == t['specialty']:
        return 95
    # Same subdomain, different specialty (directional)
    if s['domain'] == t['domain'] and s['subdomain'] == t['subdomain']:
        # Technical to management (easier)
        if s['subdomain'] in ['software_engineering', 'data_science'] and t['subdomain'] == 'project_management':
            return 85
        if s['subdomain'] == 'project_management' and t['subdomain'] in ['software_engineering', 'data_science']:
            return 55
        # Science to applied science (easier)
        if s['subdomain'] == 'science' and t['subdomain'] == 'applied_science':
            return 80
        if s['subdomain'] == 'applied_science' and t['subdomain'] == 'science':
            return 60
        return 80
    # Same domain, different subdomain (directional)
    if s['domain'] == t['domain']:
        # CS to AI is easier than AI to CS
        if s['subdomain'] == 'software_engineering' and t['subdomain'] == 'artificial_intelligence':
            return 85
        if s['subdomain'] == 'artificial_intelligence' and t['subdomain'] == 'software_engineering':
            return 65
        # Engineering to management
        if s['subdomain'] in ['engineering', 'technology'] and t['subdomain'] == 'management':
            return 70
        if s['subdomain'] == 'management' and t['subdomain'] in ['engineering', 'technology']:
            return 40
        return 65
    # Cross-domain (directional, bridge logic)
    if s['domain'] in ['engineering', 'computer_science'] and t['domain'] == 'business_management':
        return 60
    if s['domain'] == 'business_management' and t['domain'] in ['engineering', 'computer_science']:
        return 30
    # Science to Health
    if s['domain'] == 'science' and t['domain'] == 'health_sciences':
        return 55
    if s['domain'] == 'health_sciences' and t['domain'] == 'science':
        return 40
    # Social Science to Law/Policy
    if s['domain'] == 'social_sciences' and t['domain'] == 'law_policy':
        return 60
    if s['domain'] == 'law_policy' and t['domain'] == 'social_sciences':
        return 45
    # Arts/Humanities to Social Sciences
    if s['domain'] == 'arts_humanities' and t['domain'] == 'social_sciences':
        return 55
    if s['domain'] == 'social_sciences' and t['domain'] == 'arts_humanities':
        return 45
    # Distant, but possible (directional)
    if s['domain'] != t['domain']:
        if s['domain'] == 'arts_humanities' and t['domain'] == 'engineering':
            return 20
        if s['domain'] == 'engineering' and t['domain'] == 'arts_humanities':
            return 10
        return 15
    return 10

# --- GENERATE THE MATRIX ---
matrix = pd.DataFrame(index=course_names, columns=course_names)
for source in course_names:
    for target in course_names:
        score = get_relevancy(source, target)
        matrix.loc[source, target] = score if score is not None else ''

matrix.to_csv('asymmetric_hierarchical_relevancy_matrix.csv')
print("asymmetric_hierarchical_relevancy_matrix.csv generated.") 