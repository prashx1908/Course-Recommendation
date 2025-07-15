import csv
from autofilled_relevancy import relevancy as autofilled_relevancy

# Cleaned, deduplicated list of unique courses/specializations
courses = [
    "Science",
    "Commerce",
    "Computer Science",
    "Mechanical Engineering",
    "Software Development",
    "Civil Engineering",
    "Business Management",
    "Business Administration",
    "Computer Engineering",
    "Software Engineering",
    "Electronics and Telecommunication Engineering",
    "Information Technology",
    "Electrical and Electronic Engineering",
    "Arts",
    "Electronics and Communication Engineering",
    "Biotechnology",
    "Finance",
    "Accounts",
    "Economics",
    "Hospitality and Tourism Management",
    "Diploma",
    "Psychology",
    "Architecture",
    "Pharmaceutical Sciences",
    "Medical Science",
    "Pharmacy",
    "Computer Technology",
    "Electrical Engineering",
    "Chemistry",
    "Agricultural Science",
    "General Studies",
    "Nursing",
    "Mathematics",
    "Law",
    "Artificial Intelligence",
    "Marketing",
    "Computer Information Systems",
    "Electronics Engineering",
    "Physics",
    "Chemical Engineering",
    "Dentistry",
    "Human Resource Management",
    "Human Resource Development",
    "Financial Management",
    "Data Science and Analytics",
    "Language and Literature",
    "Political Science",
    "Physiotherapy",
    "Sales",
    "Microbiology",
    "English",
    "Biology",
    "Computing",
    "Aeronautical Engineering",
    "Aerospace Engineering",
    "Design",
    "International Business",
    "Media and Mass Communication",
    "Banking",
    "Business Analytics",
    "History",
    "Food Science",
    "Advertising",
    "Interior Design",
    "Life Science",
    "Biomedical Engineering",
    "Health Science",
    "Sociology",
    "Agribusiness",
    "Information Systems",
    "Mechanical and Mechatronics Engineering",
    "Instrumentation",
    "Statistics",
    "Journalism",
    "Marketing Management",
    "Biochemistry",
    "Animation",
    "Zoology",
    "Automotive Engineering",
    "Mechatronics",
    "Business Analysis",
    "Agriculture",
    "Geography",
    "Architectural Engineering",
    "Visual Arts",
    "Physical Education",
    "Medical Technology",
    "Forensic Science",
    "Humanities",
    "Operations",
    "Geology",
    "E-business",
    "Digital Business",
    "Actuarial Science",
    "Petroleum Engineering",
    "Social Work",
    "Product Design Engineering",
    "Construction Management",
    "Industrial Engineering",
    "Process Engineering",
    "Cyber Security",
    "Environmental Engineering",
    "Dietetics",
    "Horticulture",
    "Nutrition",
    "Agronomy",
    "Financial Services",
    "Philosophy",
    "Bioinformatics",
    "Dental Hygiene",
    "Clinical Sciences",
    "Supply Chain Management",
    "Gender Studies",
    "Robotics",
    "Travel and Tourism",
    "Multimedia",
    "Mining Engineering",
    "Film",
    "Forestry",
    "Logistics",
    "Physiology",
    "Healthcare",
    "Public Health",
    "Public Relations",
    "Medical Radiation Technology",
    "Project Management",
    "Urban Planning",
    "Textile",
    "International Relations",
    "Manufacturing Engineering",
    "Marine Engineering",
    "Aviation",
    "Industrial Design",
    "Criminology",
    "Liberal Arts",
    "Metallurgical Engineering",
    "Sports Science",
    "Fine Arts",
    "Health Psychology",
    "Environmental Science",
    "Telecommunications Engineering",
    "Veterinary Science",
    "Culinary Skills",
    "Game Design",
    "Engineering Management",
    "Power Engineering",
    "Graphics",
    "Textile Engineering",
    "Web Design",
    "Taxation",
    "Lab Technician",
    "Radiologic Science",
    "International Management",
    "Structural Engineering",
    "Construction",
    "Audiology",
    "Teacher Education",
    "Genetics",
    "Drug Development",
    "Fisheries",
    "Public Administration",
    "Biomedical Sciences",
    "Behavioral Sciences",
    "Culinary Arts",
    "Material Science",
    "Photography",
    "Textiles",
    "Sports Management",
    "Anthropology",
    "Information Security",
    "Entrepreneurship",
    "IT Business Analytics",
    "Electromechanical Engineering",
    "Event Management",
    "Programming",
    "Meteorology",
    "Neuroscience",
    "Management Consulting",
    "Technical Management",
    "Transportation",
    "Physical Sciences",
    "Applied Arts",
    "Human Service",
    "Plastics Engineering",
    "Fire Science",
    "Music",
    "Machine Learning",
    "Occupational Therapy",
    "Nanoscience",
    "Sales",
    "Animal Science",
    "Elementary Education",
    "Energy Systems Technology",
    "Primary Education",
    "Renewable Energy",
    "Education Assistance",
    "Early Childhood Education",
    "Educational Training",
    "Community Development",
    "Dairy",
    "Speech Pathology",
    "Mobile Communication",
    "Poultry",
    "Marine Biology",
    "Plant Science",
    "Education Counseling",
    "Psychiatric Nursing",
    "Software Testing",
    "Aviation Technology",
    "Public Policy",
    "Secondary Education",
    "Astronomy",
    "Geotechnical Engineering",
    "Geophysics",
    "Networking",
    "Therapist Assistant",
    "Interactive Media",
    "Mariculture",
    "Legal Assistant",
    "Developmental Service Worker",
    "Library",
    "Mobile Application",
    "Mining",
    "Respiratory Care",
    "Painting",
    "Animal Care",
    "Theology",
    "Customer Intelligence",
    "Physical Activity",
    "Process Engineering",
    "Cinematography",
    "Organizational Management",
    "Archaeology",
    "Broadcasting",
    "Ceramics",
    "Communicative Disorder",
    "Justice and Emergency Services",
    "Theatre",
    "Astrophysics",
    "Art",
    "Oral Science",
    "Child and Youth Worker",
    "Fishery",
    "Real Estate",
    "Water Resource",
    "Speech Therapy",
    "Animal Conservation",
    "Property Administration",
    "Biomechanical Devices",
    "Child Care",
    "Criminal Science",
    "Cytotechnology",
    "Exercise",
    "Fitness",
    "Immunology",
    "Innovation",
    "Intercultural Communication",
    "Nuclear Engineering",
    "Public Affairs",
    "Aesthetics",
    "Cultural Studies",
    "Heating",
    "Office Administration",
    "Paper and Bioprocess",
    "Studio Art",
    "Conflict Analysis",
    "Interdisciplinary Studies",
    "Police and Public Safety",
    "Publishing",
    "Autism",
    "Bakery and Pastry Arts",
    "Kinesiology",
    "Sculpture",
    "Spatial Engineering",
    "Wine Making",
    "Acupuncture",
    "Court Support",
    "Creative Writing",
    "Drama",
    "Exhibition/Event",
    "Gerontology",
    "Hair Styling",
    "Interdisciplinary Engineering",
    "Midwifery",
    "Museum and Gallery Studies",
    "Wildlife Ecosystem",
    "Brewery",
    "Carpentry",
    "Esthetic Services",
    "Ethnic Studies",
    "Firefighting",
    "International Criminology",
    "Massage Therapy",
    "Military",
    "Reading",
    "Therapeutic Recreation",
    "Welding and Fabrication",
    "Winery",
    "Woodworking"
]

BATCH_SIZE = 50

def get_batches(lst, batch_size):
    for i in range(0, len(lst), batch_size):
        yield lst[i:i + batch_size]

batches = list(get_batches(courses, BATCH_SIZE))

# Set this to the batch you want to work on (0-based)
batch_num = 1  # Now set to 1 for the next batch
current_batch = batches[batch_num]

print(f"Batch {batch_num + 1} of {len(batches)}:")
for course in current_batch:
    print(course)

# Print the current batch as a Python list for easy copy-paste
print("\n# Copy-paste this for batch mapping:")
print("batch_courses = [")
for course in current_batch:
    print(f'    "{course}",')
print("]\n")

# --- Auto-generated pair template for this batch ---
print("# All possible (row, col) pairs for this batch:")
print("# batch_pairs = [")
for row in current_batch:
    for col in current_batch:
        print(f'#     ("{row}", "{col}"),')
print("# ]\n")
print("# Example: Fill in values for these pairs in the relevancy dictionary:")
print("# relevancy = {")
for row in current_batch:
    for col in current_batch:
        print(f'#     ("{row}", "{col}"): ,')
print("# }")
# --- End auto-generated pair template ---

# --- Batch 2 Template (batch_num = 1) ---
# Use this template to fill in relevancy for this batch:
# batch_courses = [
#     "Computing",
#     "Aeronautical Engineering",
#     "Aerospace Engineering",
#     "Design",
#     "International Business",
#     "Media and Mass Communication",
#     "Banking",
#     "Business Analytics",
#     "History",
#     "Food Science",
#     "Advertising",
#     "Interior Design",
#     "Life Science",
#     "Biomedical Engineering",
#     "Health Science",
#     "Sociology",
#     "Agribusiness",
#     "Information Systems",
#     "Mechanical and Mechatronics Engineering",
#     "Instrumentation",
#     "Statistics",
#     "Journalism",
#     "Marketing Management",
#     "Biochemistry",
#     "Animation",
#     "Zoology",
#     "Automotive Engineering",
#     "Mechatronics",
#     "Business Analysis",
#     "Agriculture",
#     "Geography",
#     "Architectural Engineering",
#     "Visual Arts",
#     "Physical Education",
#     "Medical Technology",
#     "Forensic Science",
#     "Humanities",
#     "Operations",
#     "Geology",
#     "E-business",
#     "Digital Business",
#     "Actuarial Science",
#     "Petroleum Engineering",
#     "Social Work",
#     "Product Design Engineering",
#     "Construction Management",
#     "Industrial Engineering",
#     "Process Engineering",
#     "Cyber Security",
#     "Environmental Engineering",
#     "Dietetics",
#     "Horticulture",
#     "Nutrition",
# ]
# Example:
# relevancy = {
#     ("Computing", "Business Analytics"): 80,
#     ("Business Analytics", "Computing"): 75,
#     # ...add more for this batch
# }
# --- End Batch 2 Template ---

# Example: batch-wise relevancy mapping (fill in for each batch)
# Only add/override mappings for the current batch here
relevancy = {
    # Add your batch-by-batch mappings here
}

# --- Hardcoded mappings for specified courses to all courses ---
specified_courses = [
    "Financial Management",
    "Data Science and Analytics",
    "Language and Literature",
    "Political Science",
    "Physiotherapy",
    "Sales",
]

for src in specified_courses:
    for tgt in courses:
        if src == tgt:
            val = 100
        elif tgt in specified_courses:
            val = 80
        elif src in tgt or tgt in src:
            val = 60
        else:
            val = 40
        relevancy[(src, tgt)] = val
# --- End Hardcoded mappings ---

DEFAULT_SCORE = 0

def merge_relevancy(autofilled, manual):
    merged = dict(autofilled)
    merged.update(manual)  # manual/batch values take precedence
    return merged

final_relevancy = merge_relevancy(autofilled_relevancy, relevancy)

# --- Begin: Insert hardcoded mappings for 8 new specializations only if value is 0 or missing ---
hardcoded_new_relevancy = {
    # English
    ('English', 'Science'): 40,
    ('English', 'Commerce'): 40,
    ('English', 'Computer Science'): 40,
    ('English', 'Mechanical Engineering'): 40,
    ('English', 'Software Development'): 40,
    ('English', 'Civil Engineering'): 40,
    ('English', 'Business Management'): 40,
    ('English', 'Business Administration'): 40,
    ('English', 'Computer Engineering'): 40,
    ('English', 'Software Engineering'): 40,
    ('English', 'Electronics and Telecommunication Engineering'): 40,
    ('English', 'Information Technology'): 40,
    ('English', 'Electrical and Electronic Engineering'): 40,
    ('English', 'Arts'): 60,
    ('English', 'Electronics and Communication Engineering'): 40,
    ('English', 'Biotechnology'): 40,
    ('English', 'Finance'): 40,
    ('English', 'Accounts'): 40,
    ('English', 'Economics'): 40,
    ('English', 'Hospitality and Tourism Management'): 40,
    ('English', 'Diploma'): 40,
    ('English', 'Psychology'): 40,
    ('English', 'Architecture'): 40,
    ('English', 'Pharmaceutical Sciences'): 40,
    ('English', 'Medical Science'): 40,
    ('English', 'Pharmacy'): 40,
    ('English', 'Computer Technology'): 40,
    ('English', 'Electrical Engineering'): 40,
    ('English', 'Chemistry'): 40,
    ('English', 'Agricultural Science'): 40,
    ('English', 'General Studies'): 40,
    ('English', 'Nursing'): 40,
    ('English', 'Mathematics'): 40,
    ('English', 'Law'): 40,
    ('English', 'Artificial Intelligence'): 40,
    ('English', 'Marketing'): 40,
    ('English', 'Computer Information Systems'): 40,
    ('English', 'Electronics Engineering'): 40,
    ('English', 'Physics'): 40,
    ('English', 'Chemical Engineering'): 40,
    ('English', 'Dentistry'): 40,
    ('English', 'Human Resource Management'): 40,
    ('English', 'Human Resource Development'): 40,
    ('English', 'Financial Management'): 40,
    ('English', 'Data Science and Analytics'): 40,
    ('English', 'Language and Literature'): 80,
    ('English', 'Political Science'): 40,
    ('English', 'Physiotherapy'): 40,
    ('English', 'Sales'): 40,
    ('English', 'Microbiology'): 40,
    ('English', 'English'): 100,
    ('English', 'Biology'): 40,
    ('English', 'Computing'): 40,
    ('English', 'Aeronautical Engineering'): 40,
    ('English', 'Aerospace Engineering'): 40,
    ('English', 'Design'): 60,
    ('English', 'International Business'): 40,
    ('English', 'Media and Mass Communication'): 60,
    ('English', 'Banking'): 40,
    ('English', 'Business Analytics'): 40,
    ('English', 'History'): 40,
    ('English', 'Food Science'): 40,
    ('English', 'Advertising'): 40,
    ('English', 'Interior Design'): 40,
    ('English', 'Life Science'): 40,
    ('English', 'Biomedical Engineering'): 40,
    ('English', 'Health Science'): 40,
    ('English', 'Sociology'): 40,
    ('English', 'Agribusiness'): 40,
    ('English', 'Information Systems'): 40,
    ('English', 'Mechanical and Mechatronics Engineering'): 40,
    ('English', 'Instrumentation'): 40,
    ('English', 'Statistics'): 40,
    ('English', 'Journalism'): 40,
    ('English', 'Marketing Management'): 40,
    ('English', 'Biochemistry'): 40,
    ('English', 'Animation'): 40,
    ('English', 'Zoology'): 40,
    ('English', 'Automotive Engineering'): 40,
    ('English', 'Mechatronics'): 40,
    ('English', 'Business Analysis'): 40,
    ('English', 'Agriculture'): 40,
    ('English', 'Geography'): 40,
    ('English', 'Architectural Engineering'): 40,
    ('English', 'Visual Arts'): 40,
    ('English', 'Physical Education'): 40,
    ('English', 'Medical Technology'): 40,
    ('English', 'Forensic Science'): 40,
    ('English', 'Humanities'): 40,
    ('English', 'Operations'): 40,
    ('English', 'Geology'): 40,
    # ...repeat for all 8 new specializations and all 80 courses
}

# Update final_relevancy only if value is 0 or missing
for k, v in hardcoded_new_relevancy.items():
    if final_relevancy.get(k, 0) == 0:
        final_relevancy[k] = v
# --- End: Insert hardcoded mappings for 8 new specializations ---

# --- Begin: Use hardcoded/expanded mappings from autofilled_relevancy.py only if value is 0 or missing ---
# Import the full relevancy dictionary from autofilled_relevancy.py

with open("custom_specialization_matrix.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([""] + courses)
    for row_course in courses:
        row = [row_course]
        for col_course in courses:
            if (row_course, col_course) in autofilled_relevancy:
                score = autofilled_relevancy[(row_course, col_course)]
            else:
                score = relevancy.get((row_course, col_course), 0)
            row.append(score)
        writer.writerow(row)
# --- End: Use hardcoded/expanded mappings from autofilled_relevancy.py only if value is 0 or missing ---

print("Matrix written to custom_specialization_matrix.csv")
print(f"Reminder: To work on the next batch, increment batch_num (currently {batch_num}) and rerun the script.") 