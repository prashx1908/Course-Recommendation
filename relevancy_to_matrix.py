import pandas as pd
from autofilled_relevancy import relevancy

# List of all specializations (same as in generate_arts_ece_veryrelavancy.py)
all_specializations = [
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
    'Biotechnology', 'Finance', 'Accounts', 'Economics', 'Hospitality and Tourism Management', 'Diploma',
    'Psychology', 'Architecture', 'Pharmaceutical Sciences', 'Medical Science', 'Pharmacy', 'Computer Technology',
    'Electrical Engineering', 'Chemistry', 'Agricultural Science', 'General Studies', 'Nursing', 'Mathematics',
    'Law', 'Artificial Intelligence', 'Marketing', 'Computer Information Systems', 'Electronics Engineering',
    'Physics', 'Chemical Engineering', 'Dentistry', 'Human Resource Management', 'Human Resource Development',
    'Financial Management', 'Data Science and Analytics', 'Language and Literature', 'Political Science',
    'Physiotherapy', 'Sales', 'Microbiology', 'English', 'Biology', 'Computing', 'Aeronautical Engineering',
    'Aerospace Engineering', 'Design', 'International Business', 'Media and Mass Communication', 'Banking',
    'Business Analytics', 'History', 'Food Science', 'Advertising', 'Interior Design', 'Life Science',
    'Biomedical Engineering', 'Health Science', 'Sociology', 'Agribusiness', 'Information Systems',
    'Mechanical and Mechatronics Engineering', 'Instrumentation', 'Statistics', 'Journalism', 'Marketing Management',
    'Biochemistry', 'Animation', 'Zoology', 'Automotive Engineering', 'Mechatronics', 'Business Analysis',
    'Agriculture', 'Geography', 'Architectural Engineering', 'Visual Arts', 'Physical Education', 'Medical Technology',
    'Forensic Science', 'Humanities', 'Operations', 'Geology', 'E-business', 'Digital Business', 'Actuarial Science',
    'Petroleum Engineering', 'Social Work', 'Product Design Engineering', 'Construction Management',
    'Industrial Engineering', 'Process Engineering', 'Cyber Security', 'Environmental Engineering', 'Dietetics',
    'Horticulture', 'Nutrition', 'Agronomy', 'Financial Services', 'Philosophy', 'Bioinformatics', 'Dental Hygiene',
    'Clinical Sciences', 'Supply Chain Management', 'Gender Studies', 'Robotics', 'Travel and Tourism', 'Multimedia',
    'Mining Engineering', 'Film', 'Forestry', 'Logistics', 'Physiology', 'Healthcare', 'Public Health',
    'Public Relations', 'Medical Radiation Technology', 'Project Management', 'Urban Planning', 'Textile',
    'International Relations', 'Manufacturing Engineering', 'Marine Engineering', 'Aviation', 'Industrial Design',
    'Criminology', 'Liberal Arts', 'Metallurgical Engineering', 'Sports Science', 'Fine Arts', 'Health Psychology',
    'Environmental Science', 'Telecommunications Engineering', 'Veterinary Science', 'Culinary Skills', 'Game Design',
    'Engineering Management', 'Power Engineering', 'Graphics', 'Textile Engineering', 'Web Design', 'Taxation',
    'Lab Technician', 'Radiologic Science', 'International Management', 'Structural Engineering', 'Construction',
    'Audiology', 'Teacher Education', 'Genetics', 'Drug Development', 'Fisheries', 'Public Administration',
    'Biomedical Sciences', 'Behavioral Sciences', 'Culinary Arts', 'Material Science', 'Photography', 'Textiles',
    'Sports Management', 'Anthropology', 'Information Security', 'Entrepreneurship', 'IT Business Analytics',
    'Electromechanical Engineering', 'Event Management', 'Programming', 'Meteorology', 'Neuroscience',
    'Management Consulting', 'Technical Management', 'Transportation', 'Physical Sciences', 'Applied Arts',
    'Human Service', 'Plastics Engineering', 'Fire Science', 'Music', 'Machine Learning', 'Occupational Therapy',
    'Nanoscience', 'Sales', 'Animal Science', 'Elementary Education', 'Energy Systems Technology', 'Primary Education',
    'Renewable Energy', 'Education Assistance', 'Early Childhood Education', 'Educational Training',
    'Community Development', 'Dairy', 'Speech Pathology', 'Mobile Communication', 'Poultry', 'Marine Biology',
    'Plant Science', 'Education Counseling', 'Psychiatric Nursing', 'Software Testing', 'Aviation Technology',
    'Public Policy', 'Secondary Education', 'Astronomy', 'Geotechnical Engineering', 'Geophysics', 'Networking',
    'Therapist Assistant', 'Interactive Media', 'Mariculture', 'Legal Assistant', 'Developmental Service Worker',
    'Library', 'Mobile Application', 'Mining', 'Respiratory Care', 'Painting', 'Animal Care', 'Theology',
    'Customer Intelligence', 'Physical Activity', 'Process Engineering', 'Cinematography', 'Organizational Management',
    'Archaeology', 'Broadcasting', 'Ceramics', 'Communicative Disorder', 'Justice and Emergency Services', 'Theatre',
    'Astrophysics', 'Art', 'Oral Science', 'Child and Youth Worker', 'Fishery', 'Real Estate', 'Water Resource',
    'Speech Therapy', 'Animal Conservation', 'Property Administration', 'Biomechanical Devices', 'Child Care',
    'Criminal Science', 'Cytotechnology', 'Exercise', 'Fitness', 'Immunology', 'Innovation', 'Intercultural Communication',
    'Nuclear Engineering', 'Public Affairs', 'Aesthetics', 'Cultural Studies', 'Heating', 'Office Administration',
    'Paper and Bioprocess', 'Studio Art', 'Conflict Analysis', 'Interdisciplinary Studies', 'Police and Public Safety',
    'Publishing', 'Autism', 'Bakery and Pastry Arts', 'Kinesiology', 'Sculpture', 'Spatial Engineering', 'Wine Making',
    'Acupuncture', 'Court Support', 'Creative Writing', 'Drama', 'Exhibition/Event', 'Gerontology', 'Hair Styling',
    'Interdisciplinary Engineering', 'Midwifery', 'Museum and Gallery Studies', 'Wildlife Ecosystem', 'Brewery',
    'Carpentry', 'Esthetic Services', 'Ethnic Studies', 'Firefighting', 'International Criminology', 'Massage Therapy',
    'Military', 'Reading', 'Therapeutic Recreation', 'Welding and Fabrication', 'Winery', 'Woodworking'
]

# Create an empty DataFrame
matrix = pd.DataFrame(index=all_specializations, columns=all_specializations)

# Fill the matrix
for row in all_specializations:
    for col in all_specializations:
        matrix.loc[row, col] = relevancy.get((row, col), 0)

# Save to CSV
matrix.to_csv('relevancy_matrix.csv')
print("Matrix saved to relevancy_matrix.csv") 