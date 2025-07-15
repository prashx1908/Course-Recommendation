import sys
sys.path.append('.')
from custom_specialization_matrix_generator import courses
from autofilled_relevancy import relevancy as main_relevancy

# List of all specializations to generate very relevancy for
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

def get_veryrelavancy_value(source, target):
    # Strict, realistic mapping logic
    if source == target:
        return 100
    # Highly related (same domain, e.g. Engineering to Engineering, Business to Business)
    if source in target or target in source:
            return 80
    # Domain-based mapping (customize as needed)
    science = {'Biology', 'Chemistry', 'Physics', 'Mathematics', 'Biotechnology', 'Life Science', 'Microbiology', 'Biochemistry', 'Genetics', 'Zoology', 'Botany', 'Environmental Science', 'Physical Sciences', 'Bioinformatics', 'Biomedical Engineering', 'Biomedical Sciences', 'Medical Science', 'Medical Technology', 'Pharmaceutical Sciences', 'Pharmacy', 'Health Science', 'Healthcare', 'Nursing', 'Dentistry', 'Veterinary Science', 'Agricultural Science', 'Agriculture', 'Plant Science', 'Animal Science', 'Food Science', 'Nutrition', 'Dietetics', 'Horticulture', 'Agronomy', 'Animal Care', 'Marine Biology', 'Fisheries', 'Forestry', 'Immunology', 'Neuroscience', 'Genetics', 'Clinical Sciences', 'Psychiatric Nursing', 'Speech Pathology', 'Occupational Therapy', 'Physiotherapy', 'Public Health', 'Respiratory Care', 'Radiologic Science', 'Lab Technician', 'Medical Radiation Technology', 'Midwifery', 'Gerontology', 'Speech Therapy', 'Therapist Assistant', 'Audiology', 'Cytotechnology', 'Biomechanical Devices', 'Child Care', 'Dairy', 'Poultry', 'Veterinary Science', 'Animal Conservation', 'Wildlife Ecosystem', 'Plant Science', 'Marine Biology', 'Animal Science', 'Zoology', 'Botany', 'Microbiology', 'Biochemistry', 'Genetics', 'Immunology', 'Neuroscience', 'Bioinformatics', 'Biomedical Engineering', 'Biomedical Sciences', 'Medical Science', 'Medical Technology', 'Pharmaceutical Sciences', 'Pharmacy', 'Health Science', 'Healthcare', 'Nursing', 'Dentistry', 'Veterinary Science', 'Agricultural Science', 'Agriculture', 'Plant Science', 'Animal Science', 'Food Science', 'Nutrition', 'Dietetics', 'Horticulture', 'Agronomy', 'Animal Care', 'Marine Biology', 'Fisheries', 'Forestry', 'Immunology', 'Neuroscience', 'Genetics', 'Clinical Sciences', 'Psychiatric Nursing', 'Speech Pathology', 'Occupational Therapy', 'Physiotherapy', 'Public Health', 'Respiratory Care', 'Radiologic Science', 'Lab Technician', 'Medical Radiation Technology', 'Midwifery', 'Gerontology', 'Speech Therapy', 'Therapist Assistant', 'Audiology', 'Cytotechnology', 'Biomechanical Devices', 'Child Care', 'Dairy', 'Poultry', 'Veterinary Science', 'Animal Conservation', 'Wildlife Ecosystem'}
    engineering = {'Mechanical Engineering', 'Mechanical and Mechatronics Engineering', 'Mechatronics', 'Automotive Engineering', 'Aerospace Engineering', 'Aeronautical Engineering', 'Civil Engineering', 'Civil and Structural Engineering', 'Structural Engineering', 'Construction Management', 'Construction', 'Architectural Engineering', 'Architecture', 'Electrical Engineering', 'Electronics Engineering', 'Electronics and Communication Engineering', 'Electronics and Telecommunication Engineering', 'Power Engineering', 'Energy Systems Technology', 'Manufacturing Engineering', 'Industrial Engineering', 'Process Engineering', 'Mining Engineering', 'Metallurgical Engineering', 'Chemical Engineering', 'Nanoscience', 'Material Science', 'Textile Engineering', 'Plastics Engineering', 'Environmental Engineering', 'Geotechnical Engineering', 'Geology', 'Geophysics', 'Petroleum Engineering', 'Mining', 'Spatial Engineering', 'Urban Planning', 'Transportation', 'Engineering Management', 'Technical Management', 'Product Design Engineering', 'Robotics', 'Electromechanical Engineering', 'Instrumentation', 'Heating', 'Paper and Bioprocess', 'Welding and Fabrication', 'Woodworking', 'Carpentry', 'Brewery', 'Winery', 'Dairy', 'Bakery and Pastry Arts', 'Brewery', 'Winery', 'Dairy', 'Bakery and Pastry Arts'}
    business = {'Business Administration', 'Business Management', 'Finance', 'Accounts', 'Marketing', 'Human Resource Management', 'Human Resource Development', 'Economics', 'Commerce', 'Hospitality and Tourism Management', 'Hotel Management', 'Travel and Tourism', 'Event Management', 'Advertising', 'Sales', 'Operations', 'Management Consulting', 'Entrepreneurship', 'International Business', 'Digital Business', 'E-business', 'Business Analytics', 'Business Analysis', 'Financial Management', 'Financial Services', 'Taxation', 'Supply Chain Management', 'Logistics', 'Program/Project Management', 'Project Management', 'Organizational Management', 'Office Administration', 'Property Administration', 'Customer Intelligence', 'Innovation', 'Public Policy', 'Public Affairs', 'International Management', 'Real Estate', 'Public Relations', 'Public Administration'}
    arts = {'Arts', 'Fine Arts', 'Visual Arts', 'Music', 'Drama', 'Theatre', 'Photography', 'Animation', 'Design', 'Interior Design', 'History', 'Language and Literature', 'Political Science', 'Sociology', 'Liberal Arts', 'Journalism', 'Media and Mass Communication', 'Philosophy', 'Cultural Studies', 'Applied Arts', 'Creative Writing', 'Event Management', 'Public Relations', 'Publishing', 'Anthropology', 'Humanities', 'Education Assistance', 'Teacher Education', 'Early Childhood Education', 'Educational Training', 'Community Development', 'Gender Studies', 'Social Work', 'Psychology', 'Behavioral Sciences', 'Public Administration', 'International Relations', 'International Criminology', 'Conflict Analysis', 'Criminology', 'Law', 'Studio Art', 'Sculpture', 'Painting', 'Ceramics', 'Art', 'Oral Science', 'Ethnic Studies', 'Aesthetics', 'Exhibition/Event', 'Museum and Gallery Studies', 'Cinematography', 'Film', 'Broadcasting', 'Multimedia', 'Interactive Media', 'Graphics', 'Web Design', 'Game Design', 'Creative Writing', 'Publishing', 'Photography', 'Music', 'Drama', 'Theatre', 'Dance', 'Sculpture', 'Painting', 'Studio Art', 'Ceramics', 'Art', 'Oral Science', 'Ethnic Studies', 'Aesthetics', 'Exhibition/Event', 'Museum and Gallery Studies', 'Cinematography', 'Film', 'Broadcasting', 'Multimedia', 'Interactive Media', 'Graphics', 'Web Design', 'Game Design'}
    # Strict domain mapping
    if source in science and target in science:
        return 70
    if source in engineering and target in engineering:
        return 70
    if source in business and target in business:
        return 70
    if source in arts and target in arts:
        return 70
    # Related but not same domain
    if (source in science and target in engineering) or (source in engineering and target in science):
            return 40
    if (source in business and target in arts) or (source in arts and target in business):
            return 40
    if (source in business and target in science) or (source in science and target in business):
        return 30
    if (source in engineering and target in business) or (source in business and target in engineering):
        return 30
    if (source in engineering and target in arts) or (source in arts and target in engineering):
        return 30
    # Everything else is weakly related
    return 10

def generate_block(source, file):
    file.write(f"# --- Begin: Veryrelavancy mapping for {source} to all user_courses ---\n")
    file.write(f"{source.lower().replace(' ', '_').replace('&','and').replace('-', '').replace('.', '').replace('/', '')}_veryrelavancy = {{\n")
    for target in courses:
        key = (source, target)
        value = main_relevancy.get(key)
        if value is None:
            value = get_veryrelavancy_value(source, target)
        file.write(f"    {key!r}: {value},\n")
    file.write("}\n")
    file.write(f"# --- End: Veryrelavancy mapping for {source} to all user_courses ---\n\n")

if __name__ == "__main__":
    with open("veryrelavancy_output.txt", "w") as f:
        for src in all_specializations:
            generate_block(src, f) 