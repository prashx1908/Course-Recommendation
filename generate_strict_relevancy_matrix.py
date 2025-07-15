

course_names = [
    "Biotechnology", "Finance", "Accounts", "Economics", "Hospitality and Tourism Management", "Diploma",
    "Psychology", "Architecture", "Pharmaceutical Sciences", "Medical Science", "Pharmacy", "Computer Technology",
    "Electrical Engineering", "Chemistry", "Agricultural Science", "General Studies", "Nursing", "Mathematics",
    "Law", "Artificial Intelligence", "Marketing", "Computer Information Systems", "Electronics Engineering",
    "Physics", "Chemical Engineering", "Dentistry", "Human Resource Management", "Human Resource Development",
    "Financial Management", "Data Science and Analytics", "Language and Literature", "Political Science",
    "Physiotherapy", "Sales", "Microbiology", "English", "Biology", "Computing", "Aeronautical Engineering",
    "Aerospace Engineering", "Design", "International Business", "Media and Mass Communication", "Banking",
    "Business Analytics", "History", "Food Science", "Advertising", "Interior Design", "Life Science",
    "Biomedical Engineering", "Health Science", "Sociology", "Agribusiness", "Information Systems",
    "Mechanical and Mechatronics Engineering", "Instrumentation", "Statistics", "Journalism", "Marketing Management",
    "Biochemistry", "Animation", "Zoology", "Automotive Engineering", "Mechatronics", "Business Analysis",
    "Agriculture", "Geography", "Architectural Engineering", "Visual Arts", "Physical Education", "Medical Technology",
    "Forensic Science", "Humanities", "Operations", "Geology", "E-business", "Digital Business", "Actuarial Science",
    "Petroleum Engineering", "Social Work", "Product Design Engineering", "Construction Management",
    "Industrial Engineering", "Process Engineering", "Cyber Security", "Environmental Engineering", "Dietetics",
    "Horticulture", "Nutrition", "Agronomy", "Financial Services", "Philosophy", "Bioinformatics", "Dental Hygiene",
    "Clinical Sciences", "Supply Chain Management", "Gender Studies", "Robotics", "Travel and Tourism", "Multimedia",
    "Mining Engineering", "Film", "Forestry", "Logistics", "Physiology", "Healthcare", "Public Health",
    "Public Relations", "Medical Radiation Technology", "Project Management", "Urban Planning", "Textile",
    "International Relations", "Manufacturing Engineering", "Marine Engineering", "Aviation", "Industrial Design",
    "Criminology", "Liberal Arts", "Metallurgical Engineering", "Sports Science", "Fine Arts", "Health Psychology",
    "Environmental Science", "Telecommunications Engineering", "Veterinary Science", "Culinary Skills", "Game Design",
    "Engineering Management", "Power Engineering", "Graphics", "Textile Engineering", "Web Design", "Taxation",
    "Lab Technician", "Radiologic Science", "International Management", "Structural Engineering", "Construction",
    "Audiology", "Teacher Education", "Genetics", "Drug Development", "Fisheries", "Public Administration",
    "Biomedical Sciences", "Behavioral Sciences", "Culinary Arts", "Material Science", "Photography", "Textiles",
    "Sports Management", "Anthropology", "Information Security", "Entrepreneurship", "IT Business Analytics",
    "Electromechanical Engineering", "Event Management", "Programming", "Meteorology", "Neuroscience",
    "Management Consulting", "Technical Management", "Transportation", "Physical Sciences", "Applied Arts",
    "Human Service", "Plastics Engineering", "Fire Science", "Music", "Machine Learning", "Occupational Therapy",
    "Nanoscience", "Sales", "Animal Science", "Elementary Education", "Energy Systems Technology", "Primary Education",
    "Renewable Energy", "Education Assistance", "Early Childhood Education", "Educational Training",
    "Community Development", "Dairy", "Speech Pathology", "Mobile Communication", "Poultry", "Marine Biology",
    "Plant Science", "Education Counseling", "Psychiatric Nursing", "Software Testing", "Aviation Technology",
    "Public Policy", "Secondary Education", "Astronomy", "Geotechnical Engineering", "Geophysics", "Networking",
    "Therapist Assistant", "Interactive Media", "Mariculture", "Legal Assistant", "Developmental Service Worker",
    "Library", "Mobile Application", "Mining", "Respiratory Care", "Painting", "Animal Care", "Theology",
    "Customer Intelligence", "Physical Activity", "Process Engineering", "Cinematography", "Organizational Management",
    "Archaeology", "Broadcasting", "Ceramics", "Communicative Disorder", "Justice and Emergency Services", "Theatre",
    "Astrophysics", "Art", "Oral Science", "Child and Youth Worker", "Fishery", "Real Estate", "Water Resource",
    "Speech Therapy", "Animal Conservation", "Property Administration", "Biomechanical Devices", "Child Care",
    "Criminal Science", "Cytotechnology", "Exercise", "Fitness", "Immunology", "Innovation", "Intercultural Communication",
    "Nuclear Engineering", "Public Affairs", "Aesthetics", "Cultural Studies", "Heating", "Office Administration",
    "Paper and Bioprocess", "Studio Art", "Conflict Analysis", "Interdisciplinary Studies", "Police and Public Safety",
    "Publishing", "Autism", "Bakery and Pastry Arts", "Kinesiology", "Sculpture", "Spatial Engineering", "Wine Making",
    "Acupuncture", "Court Support", "Creative Writing", "Drama", "Exhibition/Event", "Gerontology", "Hair Styling",
    "Interdisciplinary Engineering", "Midwifery", "Museum and Gallery Studies", "Wildlife Ecosystem", "Brewery",
    "Carpentry", "Esthetic Services", "Ethnic Studies", "Firefighting", "International Criminology", "Massage Therapy",
    "Military", "Reading", "Therapeutic Recreation", "Welding and Fabrication", "Winery", "Woodworking"
]

# Comprehensive course database with hierarchical structure
courses_db = {
            # ENGINEERING DOMAIN
            ## Computer Science & IT
            'Computer Science': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'core_cs'},
            'Software Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'software_dev'},
            'Computer Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'hardware_software'},
            'Information Technology': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'it_systems'},
            'Software Development': {'level': 'diploma', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'software_dev'},
            'Data Science and Analytics': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'data_science'},
            'Artificial Intelligence': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'ai_ml'},
            'Machine Learning': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'ai_ml'},
            'Cyber Security': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'security'},
            'Information Security': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'security'},
            'Computer Information Systems': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'it_systems'},
            'Information Systems': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'it_systems'},
            'Web Design': {'level': 'diploma', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'web_dev'},
            'Mobile Application': {'level': 'diploma', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'mobile_dev'},
            'Game Design': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'game_dev'},
            'Programming': {'level': 'certificate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'software_dev'},
            'Software Testing': {'level': 'diploma', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'software_dev'},
            'Networking': {'level': 'diploma', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'network_sys'},
            'Database Management': {'level': 'diploma', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'data_management'},
            'Cloud Computing': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'cloud_sys'},
            'DevOps': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'software_dev'},
            'Blockchain Technology': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'emerging_tech'},
            'Internet of Things': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'emerging_tech'},
            'Robotics': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'robotics'},
            'Computer Graphics': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'graphics'},
            'Human-Computer Interaction': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'hci'},
            'Quantum Computing': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'cs_it', 'specialty': 'emerging_tech'},
            
            ## Electronics & Electrical Engineering
            'Electrical Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'power_systems'},
            'Electronics Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'electronics'},
            'Electronics and Communication Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'communication'},
            'Electronics and Telecommunication Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'telecom'},
            'Electrical and Electronic Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'power_electronics'},
            'Power Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'power_systems'},
            'Telecommunications Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'telecom'},
            'Instrumentation': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'instrumentation'},
            'Control Systems': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'control_systems'},
            'Signal Processing': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'signal_processing'},
            'VLSI Design': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'vlsi'},
            'Embedded Systems': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'embedded'},
            'Renewable Energy': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'renewable_energy'},
            'Energy Systems Technology': {'level': 'diploma', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'energy_systems'},
            'Nuclear Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'nuclear'},
            'Microelectronics': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'microelectronics'},
            'Photonics': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'photonics'},
            'Automation Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'electrical', 'specialty': 'automation'},
            
            ## Mechanical & Manufacturing
            'Mechanical Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'mechanical_design'},
            'Mechanical and Mechatronics Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'mechatronics'},
            'Mechatronics': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'mechatronics'},
            'Manufacturing Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'manufacturing'},
            'Industrial Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'industrial'},
            'Automotive Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'automotive'},
            'Aerospace Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'aerospace'},
            'Aeronautical Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'aeronautical'},
            'Marine Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'marine'},
            'Robotics': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'robotics'},
            'Thermal Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'thermal'},
            'Fluid Mechanics': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'fluid_mechanics'},
            'Materials Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'materials'},
            'Nanotechnology': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'nanotechnology'},
            'Additive Manufacturing': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mechanical', 'specialty': 'additive_manufacturing'},
            
            ## Civil & Structural
            'Civil Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'structural'},
            'Structural Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'structural'},
            'Construction Management': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'construction'},
            'Architecture': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'architecture'},
            'Architectural Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'architectural_eng'},
            'Urban Planning': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'urban_planning'},
            'Transportation Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'transportation'},
            'Geotechnical Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'geotechnical'},
            'Environmental Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'environmental'},
            'Water Resources Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'water_resources'},
            'Earthquake Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'earthquake'},
            'Coastal Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'coastal'},
            'Bridge Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'bridge'},
            'Highway Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'civil', 'specialty': 'highway'},
            
            ## Chemical & Process
            'Chemical Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'chemical', 'specialty': 'process'},
            'Process Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'chemical', 'specialty': 'process'},
            'Petroleum Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'chemical', 'specialty': 'petroleum'},
            'Biotechnology': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'chemical', 'specialty': 'biotechnology'},
            'Biomedical Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'chemical', 'specialty': 'biomedical'},
            'Food Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'chemical', 'specialty': 'food_processing'},
            'Pharmaceutical Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'chemical', 'specialty': 'pharmaceutical'},
            'Polymer Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'chemical', 'specialty': 'polymer'},
            'Environmental Process Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'chemical', 'specialty': 'environmental_process'},
            'Biochemical Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'chemical', 'specialty': 'biochemical'},
            
            ## Mining & Materials
            'Mining Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'mining', 'specialty': 'extraction'},
            'Metallurgical Engineering': {'level': 'undergraduate', 'domain': 'engineering', 'subdomain': 'mining', 'specialty': 'metallurgy'},
            'Materials Science': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mining', 'specialty': 'materials_science'},
            'Mineral Processing': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mining', 'specialty': 'mineral_processing'},
            'Geological Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mining', 'specialty': 'geological'},
            'Ceramics Engineering': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mining', 'specialty': 'ceramics'},
            'Composite Materials': {'level': 'postgraduate', 'domain': 'engineering', 'subdomain': 'mining', 'specialty': 'composites'},
            
            # SCIENCE & HEALTH DOMAIN
            ## Pure Sciences
            'Physics': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'physics'},
            'Chemistry': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'chemistry'},
            'Mathematics': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'mathematics'},
            'Statistics': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'statistics'},
            'Applied Mathematics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'applied_math'},
            'Theoretical Physics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'theoretical_physics'},
            'Quantum Physics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'quantum_physics'},
            'Astrophysics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'astrophysics'},
            'Astronomy': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'astronomy'},
            'Geophysics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'geophysics'},
            'Geology': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'geology'},
            'Meteorology': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'meteorology'},
            'Actuarial Science': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'actuarial'},
            'Computational Mathematics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'computational_math'},
            'Data Analytics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'pure_sciences', 'specialty': 'data_analytics'},
            
            ## Life Sciences
            'Biology': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'general_biology'},
            'Biotechnology': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'biotechnology'},
            'Biochemistry': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'biochemistry'},
            'Microbiology': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'microbiology'},
            'Genetics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'genetics'},
            'Molecular Biology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'molecular_biology'},
            'Cell Biology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'cell_biology'},
            'Developmental Biology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'developmental_biology'},
            'Immunology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'immunology'},
            'Neuroscience': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'neuroscience'},
            'Bioinformatics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'bioinformatics'},
            'Genomics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'genomics'},
            'Proteomics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'proteomics'},
            'Biophysics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'biophysics'},
            'Structural Biology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'structural_biology'},
            'Systems Biology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'systems_biology'},
            'Synthetic Biology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'synthetic_biology'},
            'Pharmacology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'pharmacology'},
            'Toxicology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'toxicology'},
            
            ## Medical Sciences
            'Medicine': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'general_medicine'},
            'Surgery': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'surgery'},
            'Cardiology': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'cardiology'},
            'Neurology': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'neurology'},
            'Oncology': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'oncology'},
            'Pediatrics': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'pediatrics'},
            'Psychiatry': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'psychiatry'},
            'Radiology': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'radiology'},
            'Anesthesiology': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'anesthesiology'},
            'Pathology': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'pathology'},
            'Clinical Research': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'clinical_research'},
            'Medical Technology': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'medical_technology'},
            'Medical Laboratory Science': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'lab_science'},
            'Emergency Medicine': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'emergency_medicine'},
            'Sports Medicine': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'sports_medicine'},
            'Forensic Medicine': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'forensic_medicine'},
            'Public Health': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'public_health'},
            'Epidemiology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'epidemiology'},
            'Biostatistics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'biostatistics'},
            'Health Informatics': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'health_informatics'},
            'Telemedicine': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'telemedicine'},
            
            ## Allied Health
            'Nursing': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'nursing'},
            'Physiotherapy': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'physiotherapy'},
            'Occupational Therapy': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'occupational_therapy'},
            'Pharmacy': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'pharmacy'},
            'Dentistry': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'dentistry'},
            'Veterinary Science': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'veterinary'},
            'Optometry': {'level': 'professional', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'optometry'},
            'Audiology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'audiology'},
            'Speech Therapy': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'speech_therapy'},
            'Nutrition': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'nutrition'},
            'Dietetics': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'dietetics'},
            'Health Psychology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'health_psychology'},
            'Clinical Psychology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'clinical_psychology'},
            'Counseling Psychology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'counseling_psychology'},
            'Rehabilitation Science': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'rehabilitation'},
            'Respiratory Therapy': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'respiratory_therapy'},
            'Radiologic Technology': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'radiologic_technology'},
            'Medical Imaging': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'medical_imaging'},
            'Prosthetics and Orthotics': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'prosthetics_orthotics'},
            'Biomedical Technology': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'biomedical_technology'},
            
            ## Environmental & Earth Sciences
            'Environmental Science': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'environmental_science'},
            'Environmental Engineering': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'environmental_engineering'},
            'Climate Science': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'climate_science'},
            'Conservation Biology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'conservation_biology'},
            'Marine Science': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'marine_science'},
            'Oceanography': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'oceanography'},
            'Atmospheric Science': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'atmospheric_science'},
            'Ecology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'ecology'},
            'Wildlife Biology': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'wildlife_biology'},
            'Forestry': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'forestry'},
            'Agriculture': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'agriculture'},
            'Agronomy': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'agronomy'},
            'Soil Science': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'soil_science'},
            'Plant Science': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'plant_science'},
            'Animal Science': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'animal_science'},
            'Aquaculture': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'aquaculture'},
            'Sustainable Development': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'sustainable_development'},
            'Renewable Energy Technology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'renewable_energy'},
            
            # BUSINESS & MANAGEMENT DOMAIN
            ## Core Business
            'Business Administration': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'general_management'},
            'Business Management': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'general_management'},
            'Management Studies': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'management_studies'},
            'Strategic Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'strategic_management'},
            'Operations Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'operations'},
            'Project Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'project_management'},
            'Organizational Behavior': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'organizational_behavior'},
            'Change Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'change_management'},
            'Innovation Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'innovation_management'},
            'Quality Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'quality_management'},
            'Risk Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'risk_management'},
            'Performance Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'performance_management'},
            'Leadership Studies': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'leadership'},
            'Executive Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'executive_management'},
            
            ## Finance & Accounting
            'Finance': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'corporate_finance'},
            'Accounting': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'accounting'},
            'Financial Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'financial_management'},
            'Investment Banking': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'investment_banking'},
            'Corporate Finance': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'corporate_finance'},
            'Financial Analysis': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'financial_analysis'},
            'Portfolio Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'portfolio_management'},
            'Risk Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'financial_risk'},
            'Insurance': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'insurance'},
            'Banking': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'banking'},
            'Financial Planning': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'financial_planning'},
            'Taxation': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'taxation'},
            'Auditing': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'auditing'},
            'Forensic Accounting': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'forensic_accounting'},
            'International Finance': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'international_finance'},
            'Financial Technology': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'fintech'},
            'Cryptocurrency': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'cryptocurrency'},
            'Quantitative Finance': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'quantitative_finance'},
            'Real Estate Finance': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'real_estate_finance'},
            'Behavioral Finance': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'behavioral_finance'},
            
            ## Marketing & Sales
            'Marketing': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'general_marketing'},
            'Digital Marketing': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'digital_marketing'},
            'Brand Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'brand_management'},
            'Consumer Behavior': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'consumer_behavior'},
            'Market Research': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'market_research'},
            'Sales Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'sales_management'},
            'Advertising': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'advertising'},
            'Public Relations': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'public_relations'},
            'Social Media Marketing': {'level': 'diploma', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'social_media_marketing'},
            'Content Marketing': {'level': 'diploma', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'content_marketing'},
            'E-commerce': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'ecommerce'},
            'Retail Management': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'retail_management'},
            'Customer Relationship Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'crm'},
            'International Marketing': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'international_marketing'},
            'Services Marketing': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'services_marketing'},
            'Sports Marketing': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'sports_marketing'},
            'Healthcare Marketing': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'healthcare_marketing'},
            'Event Marketing': {'level': 'diploma', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'event_marketing'},
            'Influencer Marketing': {'level': 'diploma', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'influencer_marketing'},
            'Growth Marketing': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'growth_marketing'},
            
            ## Human Resources
            'Human Resource Management': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'hr_management'},
            'Human Resource Development': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'hr_development'},
            'Talent Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'talent_management'},
            'Compensation and Benefits': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'compensation_benefits'},
            'Training and Development': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'training_development'},
            'Performance Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'performance_management'},
            'Employee Relations': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'employee_relations'},
            'Organizational Development': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'organizational_development'},
            'Recruitment and Selection': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'recruitment_selection'},
            'HR Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'hr_analytics'},
            'Diversity and Inclusion': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'diversity_inclusion'},
            'Labor Relations': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'labor_relations'},
            'Workplace Psychology': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'workplace_psychology'},
            'HR Technology': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'hr_technology'},
            'Change Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'human_resources', 'specialty': 'change_management'},
            
            ## International Business
            'International Business': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'international_business'},
            'Global Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'global_management'},
            'International Trade': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'international_trade'},
            'Export-Import Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'export_import'},
            'Cross-Cultural Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'cross_cultural_management'},
            'International Economics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'international_economics'},
            'Global Supply Chain': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'global_supply_chain'},
            'International Marketing': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'international_marketing'},
            'Foreign Direct Investment': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'foreign_investment'},
            'International Finance': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'international_finance'},
            'Multinational Corporation Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'mnc_management'},
            'International Business Law': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'international_business_law'},
            'Global Strategy': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'global_strategy'},
            'International Negotiations': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'international_negotiations'},
            'Emerging Markets': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'emerging_markets'},
            
            ## Entrepreneurship & Innovation
            'Entrepreneurship': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'startup_management'},
            'Innovation Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'innovation_management'},
            'Venture Capital': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'venture_capital'},
            'Business Model Innovation': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'business_model_innovation'},
            'Startup Incubation': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'startup_incubation'},
            'Technology Transfer': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'technology_transfer'},
            'Social Entrepreneurship': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'social_entrepreneurship'},
            'Corporate Entrepreneurship': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'corporate_entrepreneurship'},
            'Digital Entrepreneurship': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'digital_entrepreneurship'},
            'Lean Startup': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'lean_startup'},
            'Product Development': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'product_development'},
            'Business Plan Development': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'business_plan_development'},
            'Intellectual Property Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'ip_management'},
            'Innovation Strategy': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'innovation_strategy'},
            'Startup Financing': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'entrepreneurship', 'specialty': 'startup_financing'},
            
            ## Supply Chain & Operations
            'Supply Chain Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'supply_chain'},
            'Operations Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'operations_management'},
            'Logistics Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'logistics'},
            'Procurement Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'procurement'},
            'Inventory Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'inventory_management'},
            'Quality Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'quality_management'},
            'Lean Manufacturing': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'lean_manufacturing'},
            'Six Sigma': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'six_sigma'},
            'Production Planning': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'production_planning'},
            'Warehouse Management': {'level': 'diploma', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'warehouse_management'},
            'Transportation Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'transportation_management'},
            'Demand Forecasting': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'demand_forecasting'},
            'Supplier Relationship Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'supplier_relationship'},
            'Distribution Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'distribution_management'},
            'Operations Research': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'operations_research'},
            
            ## Analytics & Data Science
            'Business Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'business_analytics'},
            'Data Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'data_analytics'},
            'Predictive Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'predictive_analytics'},
            'Marketing Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'marketing_analytics'},
            'Financial Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'financial_analytics'},
            'Operations Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'operations_analytics'},
            'Customer Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'customer_analytics'},
            'Digital Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'digital_analytics'},
            'Social Media Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'social_media_analytics'},
            'Web Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'web_analytics'},
            'Big Data Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'big_data_analytics'},
            'Text Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'text_analytics'},
            'Sentiment Analysis': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'sentiment_analysis'},
            'Data Visualization': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'data_visualization'},
            'Business Intelligence': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'business_intelligence'},
            
            # ARTS & HUMANITIES DOMAIN
            ## Literature & Languages
            'English Literature': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'english_literature'},
            'Comparative Literature': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'comparative_literature'},
            'Creative Writing': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'creative_writing'},
            'Linguistics': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'linguistics'},
            'Applied Linguistics': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'applied_linguistics'},
            'Translation Studies': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'translation_studies'},
            'Technical Writing': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'technical_writing'},
            'Copywriting': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'copywriting'},
            'Content Writing': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'content_writing'},
            'Scriptwriting': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'scriptwriting'},
            'Poetry': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'poetry'},
            'Drama': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'drama'},
            'Literary Criticism': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'literary_criticism'},
            'Digital Humanities': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'digital_humanities'},
            'World Literature': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'literature', 'specialty': 'world_literature'},
            
            ## Visual Arts
            'Fine Arts': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'fine_arts'},
            'Painting': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'painting'},
            'Sculpture': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'sculpture'},
            'Drawing': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'drawing'},
            'Photography': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'photography'},
            'Digital Art': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'digital_art'},
            'Graphic Design': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'graphic_design'},
            'Art History': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'art_history'},
            'Art Therapy': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'art_therapy'},
            'Museum Studies': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'museum_studies'},
            'Art Conservation': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'art_conservation'},
            'Printmaking': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'printmaking'},
            'Ceramics': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'ceramics'},
            'Textile Arts': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'textile_arts'},
            'Jewelry Design': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'jewelry_design'},
            
            ## Performing Arts
            'Music': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'music'},
            'Music Performance': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'music_performance'},
            'Music Composition': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'music_composition'},
            'Music Production': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'music_production'},
            'Music Theory': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'music_theory'},
            'Music Therapy': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'music_therapy'},
            'Dance': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'dance'},
            'Choreography': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'choreography'},
            'Theatre': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'theatre'},
            'Acting': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'acting'},
            'Theatre Direction': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'theatre_direction'},
            'Stage Design': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'stage_design'},
            'Sound Design': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'sound_design'},
            'Lighting Design': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'lighting_design'},
            'Costume Design': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'performing_arts', 'specialty': 'costume_design'},
            
            ## Media & Communication
            'Journalism': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'media', 'specialty': 'journalism'},
            'Broadcast Journalism': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'media', 'specialty': 'broadcast_journalism'},
            'Print Journalism': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'media', 'specialty': 'print_journalism'},
            'Digital Journalism': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'media', 'specialty': 'digital_journalism'},
            'Investigative Journalism': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'media', 'specialty': 'investigative_journalism'},
            'Sports Journalism': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'media', 'specialty': 'sports_journalism'},
            'Accounts': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'accounts'},
'Economics': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'economics', 'specialty': 'economics'},
'Hospitality and Tourism Management': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'hospitality', 'specialty': 'hospitality_tourism'},
'Diploma': {'level': 'diploma', 'domain': 'general', 'subdomain': 'general', 'specialty': 'general_diploma'},
'Psychology': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'psychology', 'specialty': 'psychology'},
'Pharmaceutical Sciences': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'pharmacy', 'specialty': 'pharmaceutical_sciences'},
'Medical Science': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'medical_science'},
'Computer Technology': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'computer', 'specialty': 'computer_technology'},
'Agricultural Science': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'agricultural_science'},
'General Studies': {'level': 'undergraduate', 'domain': 'general', 'subdomain': 'general', 'specialty': 'general_studies'},
'Law': {'level': 'undergraduate', 'domain': 'law', 'subdomain': 'law', 'specialty': 'law'},
'Language and Literature': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'language_literature', 'specialty': 'language_literature'},
'Political Science': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'political_science', 'specialty': 'political_science'},
'Sales': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'sales'},
'English': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'language_literature', 'specialty': 'english'},
'Computing': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'computer', 'specialty': 'computing'},
'Design': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'design', 'specialty': 'design'},
'Media and Mass Communication': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'media', 'specialty': 'media_mass_communication'},
'History': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'history', 'specialty': 'history'},
'Food Science': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'food_science', 'specialty': 'food_science'},
'Interior Design': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'design', 'specialty': 'interior_design'},
'Life Science': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'life_science'},
'Health Science': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'health_sciences', 'specialty': 'health_science'},
'Sociology': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'sociology', 'specialty': 'sociology'},
'Agribusiness': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'agribusiness', 'specialty': 'agribusiness'},
'Marketing Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'marketing_management'},
'Animation': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'animation', 'specialty': 'animation'},
'Zoology': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'zoology'},
'Business Analysis': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'business_analysis'},
'Geography': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'geography'},
'Visual Arts': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'visual_arts'},
'Physical Education': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'physical_education', 'specialty': 'physical_education'},
'Forensic Science': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'forensics', 'specialty': 'forensic_science'},

'Humanities': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'humanities', 'specialty': 'humanities'},
'Operations': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'operations', 'specialty': 'operations'},
'E-business': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'digital_business', 'specialty': 'e_business'},
'Digital Business': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'digital_business', 'specialty': 'digital_business'},
'Social Work': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'social_work', 'specialty': 'social_work'},
'Product Design Engineering': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'design_engineering', 'specialty': 'product_design_engineering'},
'Horticulture': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'horticulture'},
'Financial Services': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'finance', 'specialty': 'financial_services'},
'Philosophy': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'philosophy', 'specialty': 'philosophy'},
'Dental Hygiene': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'dental_hygiene'},
'Clinical Sciences': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'clinical_sciences'},
'Gender Studies': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'gender_studies', 'specialty': 'gender_studies'},
'Travel and Tourism': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'hospitality', 'specialty': 'travel_tourism'},
'Multimedia': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'media', 'specialty': 'multimedia'},
'Film': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'media', 'specialty': 'film'},
'Logistics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'supply_chain', 'specialty': 'logistics'},
'Physiology': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'physiology'},
'Healthcare': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'health_sciences', 'specialty': 'healthcare'},
'Medical Radiation Technology': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'medical_radiation_technology'},
'Textile': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'textile', 'specialty': 'textile'},
'International Relations': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'international_relations', 'specialty': 'international_relations'},
'Aviation': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'aviation', 'specialty': 'aviation'},
'Industrial Design': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'design_engineering', 'specialty': 'industrial_design'},
'Criminology': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'criminology', 'specialty': 'criminology'},
'Liberal Arts': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'liberal_arts', 'specialty': 'liberal_arts'},
'Sports Science': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'sports', 'specialty': 'sports_science'},
'Culinary Skills': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'culinary_arts', 'specialty': 'culinary_skills'},
'Engineering Management': {'level': 'postgraduate', 'domain': 'engineering_technology', 'subdomain': 'management', 'specialty': 'engineering_management'},
'Graphics': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'design', 'specialty': 'graphics'},
'Textile Engineering': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'textile', 'specialty': 'textile_engineering'},
'Lab Technician': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'lab_technician'},
'Radiologic Science': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'radiologic_science'},
'International Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'international', 'specialty': 'international_management'},
'Construction': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'construction', 'specialty': 'construction'},
'Teacher Education': {'level': 'undergraduate', 'domain': 'education', 'subdomain': 'teacher_education', 'specialty': 'teacher_education'},
'Drug Development': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'pharmacy', 'specialty': 'drug_development'},
'Fisheries': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'fisheries'},
'Public Administration': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'public_administration', 'specialty': 'public_administration'},
'Biomedical Sciences': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'biomedical_sciences'},
'Behavioral Sciences': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'behavioral_sciences', 'specialty': 'behavioral_sciences'},
'Culinary Arts': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'culinary_arts', 'specialty': 'culinary_arts'},
'Material Science': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'materials', 'specialty': 'material_science'},
'Textiles': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'textile', 'specialty': 'textiles'},
'Sports Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'sports', 'specialty': 'sports_management'},
'Anthropology': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'anthropology', 'specialty': 'anthropology'},
'IT Business Analytics': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'it_business_analytics'},
'Electromechanical Engineering': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'electromechanical', 'specialty': 'electromechanical_engineering'},
'Event Management': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'event_management', 'specialty': 'event_management'},
'Management Consulting': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'consulting', 'specialty': 'management_consulting'},
'Technical Management': {'level': 'postgraduate', 'domain': 'engineering_technology', 'subdomain': 'management', 'specialty': 'technical_management'},
'Transportation': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'transportation', 'specialty': 'transportation'},
'Physical Sciences': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'physical_sciences', 'specialty': 'physical_sciences'},
'Applied Arts': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'applied_arts', 'specialty': 'applied_arts'},
'Human Service': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'human_services', 'specialty': 'human_service'},
'Plastics Engineering': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'materials', 'specialty': 'plastics_engineering'},
'Fire Science': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'emergency_services', 'specialty': 'fire_science'},
'Nanoscience': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'physical_sciences', 'specialty': 'nanoscience'},
'Sales': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'marketing', 'specialty': 'sales'},
'Elementary Education': {'level': 'undergraduate', 'domain': 'education', 'subdomain': 'elementary_education', 'specialty': 'elementary_education'},
'Primary Education': {'level': 'undergraduate', 'domain': 'education', 'subdomain': 'primary_education', 'specialty': 'primary_education'},
'Education Assistance': {'level': 'diploma', 'domain': 'education', 'subdomain': 'support', 'specialty': 'education_assistance'},
'Early Childhood Education': {'level': 'undergraduate', 'domain': 'education', 'subdomain': 'early_childhood', 'specialty': 'early_childhood_education'},
'Educational Training': {'level': 'postgraduate', 'domain': 'education', 'subdomain': 'training', 'specialty': 'educational_training'},
'Community Development': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'community_development', 'specialty': 'community_development'},
'Dairy': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'food_science', 'specialty': 'dairy'},
'Speech Pathology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'speech_pathology'},
'Mobile Communication': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'communications', 'specialty': 'mobile_communication'},
'Poultry': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'poultry'},
'Marine Biology': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'life_sciences', 'specialty': 'marine_biology'},
'Education Counseling': {'level': 'postgraduate', 'domain': 'education', 'subdomain': 'counseling', 'specialty': 'education_counseling'},
'Psychiatric Nursing': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'psychiatric_nursing'},
'Aviation Technology': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'aviation', 'specialty': 'aviation_technology'},
'Public Policy': {'level': 'postgraduate', 'domain': 'social_sciences', 'subdomain': 'public_policy', 'specialty': 'public_policy'},
'Secondary Education': {'level': 'undergraduate', 'domain': 'education', 'subdomain': 'secondary_education', 'specialty': 'secondary_education'},
'Therapist Assistant': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'therapist_assistant'},
'Interactive Media': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'media', 'specialty': 'interactive_media'},
'Mariculture': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'mariculture'},
'Legal Assistant': {'level': 'diploma', 'domain': 'law', 'subdomain': 'legal_support', 'specialty': 'legal_assistant'},
'Developmental Service Worker': {'level': 'diploma', 'domain': 'social_sciences', 'subdomain': 'human_services', 'specialty': 'developmental_service_worker'},
'Library': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'library_science', 'specialty': 'library'},
'Mining': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'mining', 'specialty': 'mining'},
'Respiratory Care': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'respiratory_care'},
'Animal Care': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'veterinary', 'specialty': 'animal_care'},
'Theology': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'theology', 'specialty': 'theology'},
'Customer Intelligence': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'analytics', 'specialty': 'customer_intelligence'},
'Physical Activity': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'sports', 'specialty': 'physical_activity'},
'Cinematography': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'media', 'specialty': 'cinematography'},
'Organizational Management': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'organizational_management'},
'Archaeology': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'archaeology', 'specialty': 'archaeology'},
'Broadcasting': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'media', 'specialty': 'broadcasting'},
'Communicative Disorder': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'communicative_disorder'},
'Justice and Emergency Services': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'justice', 'specialty': 'justice_emergency_services'},
'Art': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'art'},
'Oral Science': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'oral_science'},
'Child and Youth Worker': {'level': 'diploma', 'domain': 'social_sciences', 'subdomain': 'human_services', 'specialty': 'child_youth_worker'},
'Fishery': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'fishery'},
'Real Estate': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'real_estate', 'specialty': 'real_estate'},
'Water Resource': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'water_resource'},
'Animal Conservation': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'animal_conservation'},
'Property Administration': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'real_estate', 'specialty': 'property_administration'},
'Biomechanical Devices': {'level': 'postgraduate', 'domain': 'engineering_technology', 'subdomain': 'biomedical', 'specialty': 'biomechanical_devices'},
'Child Care': {'level': 'diploma', 'domain': 'social_sciences', 'subdomain': 'human_services', 'specialty': 'child_care'},
'Criminal Science': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'criminology', 'specialty': 'criminal_science'},
'Cytotechnology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'medical', 'specialty': 'cytotechnology'},
'Exercise': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'sports', 'specialty': 'exercise'},
'Fitness': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'sports', 'specialty': 'fitness'},
'Innovation': {'level': 'postgraduate', 'domain': 'business_management', 'subdomain': 'core_business', 'specialty': 'innovation'},
'Intercultural Communication': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'communication', 'specialty': 'intercultural_communication'},
'Public Affairs': {'level': 'postgraduate', 'domain': 'social_sciences', 'subdomain': 'public_affairs', 'specialty': 'public_affairs'},
'Aesthetics': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'aesthetics', 'specialty': 'aesthetics'},
'Cultural Studies': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'cultural_studies', 'specialty': 'cultural_studies'},
'Heating': {'level': 'diploma', 'domain': 'engineering_technology', 'subdomain': 'mechanical', 'specialty': 'heating'},
'Office Administration': {'level': 'undergraduate', 'domain': 'business_management', 'subdomain': 'administration', 'specialty': 'office_administration'},
'Paper and Bioprocess': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'process_engineering', 'specialty': 'paper_bioprocess'},
'Studio Art': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'visual_arts', 'specialty': 'studio_art'},
'Conflict Analysis': {'level': 'postgraduate', 'domain': 'social_sciences', 'subdomain': 'conflict_studies', 'specialty': 'conflict_analysis'},
'Interdisciplinary Studies': {'level': 'undergraduate', 'domain': 'general', 'subdomain': 'interdisciplinary', 'specialty': 'interdisciplinary_studies'},
'Police and Public Safety': {'level': 'undergraduate', 'domain': 'social_sciences', 'subdomain': 'justice', 'specialty': 'police_public_safety'},
'Publishing': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'publishing', 'specialty': 'publishing'},
'Autism': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'autism'},
'Bakery and Pastry Arts': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'culinary_arts', 'specialty': 'bakery_pastry_arts'},
'Kinesiology': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'sports', 'specialty': 'kinesiology'},
'Spatial Engineering': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'spatial', 'specialty': 'spatial_engineering'},
'Wine Making': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'food_science', 'specialty': 'wine_making'},
'Acupuncture': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'acupuncture'},
'Court Support': {'level': 'diploma', 'domain': 'law', 'subdomain': 'legal_support', 'specialty': 'court_support'},
'Exhibition/Event': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'event_management', 'specialty': 'exhibition_event'},
'Gerontology': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'gerontology'},
'Hair Styling': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'personal_care', 'specialty': 'hair_styling'},
'Interdisciplinary Engineering': {'level': 'undergraduate', 'domain': 'engineering_technology', 'subdomain': 'interdisciplinary', 'specialty': 'interdisciplinary_engineering'},
'Midwifery': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'midwifery'},
'Museum and Gallery Studies': {'level': 'postgraduate', 'domain': 'arts_humanities', 'subdomain': 'museum_studies', 'specialty': 'museum_gallery_studies'},
'Wildlife Ecosystem': {'level': 'undergraduate', 'domain': 'science_health', 'subdomain': 'environmental', 'specialty': 'wildlife_ecosystem'},
'Brewery': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'food_science', 'specialty': 'brewery'},
'Carpentry': {'level': 'diploma', 'domain': 'engineering_technology', 'subdomain': 'construction', 'specialty': 'carpentry'},
'Esthetic Services': {'level': 'diploma', 'domain': 'arts_humanities', 'subdomain': 'personal_care', 'specialty': 'esthetic_services'},
'Ethnic Studies': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'ethnic_studies', 'specialty': 'ethnic_studies'},
'Firefighting': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'emergency_services', 'specialty': 'firefighting'},
'International Criminology': {'level': 'postgraduate', 'domain': 'social_sciences', 'subdomain': 'criminology', 'specialty': 'international_criminology'},
'Massage Therapy': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'massage_therapy'},
'Military': {'level': 'undergraduate', 'domain': 'general', 'subdomain': 'military', 'specialty': 'military'},
'Reading': {'level': 'undergraduate', 'domain': 'arts_humanities', 'subdomain': 'language_literature', 'specialty': 'reading'},
'Therapeutic Recreation': {'level': 'postgraduate', 'domain': 'science_health', 'subdomain': 'allied_health', 'specialty': 'therapeutic_recreation'},
'Welding and Fabrication': {'level': 'diploma', 'domain': 'engineering_technology', 'subdomain': 'manufacturing', 'specialty': 'welding_fabrication'},
'Winery': {'level': 'diploma', 'domain': 'science_health', 'subdomain': 'food_science', 'specialty': 'winery'},
'Woodworking': {'level': 'diploma', 'domain': 'engineering_technology', 'subdomain': 'manufacturing', 'specialty': 'woodworking'},



    # ... (your full mapping as shown above) ...
}

def get_relevancy(source, target, courses_db):
    if source not in courses_db or target not in courses_db:
        return None  # Ignore unmapped

    s = courses_db[source]
    t = courses_db[target]

    # 1. Exact match
    if source == target:
        return 100

    # 2. Exact specialty (but not same course)
    if s['domain'] == t['domain'] and s['subdomain'] == t['subdomain'] and s['specialty'] == t['specialty']:
        return 95

    # 3. Same subdomain, different specialty (directional)
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

    # 4. Same domain, different subdomain (directional)
    if s['domain'] == t['domain']:
        # CS to AI is easier than AI to CS
        if s['subdomain'] == 'computer_science' and t['subdomain'] == 'artificial_intelligence':
            return 85
        if s['subdomain'] == 'artificial_intelligence' and t['subdomain'] == 'computer_science':
            return 65
        # Engineering to management
        if s['subdomain'] in ['engineering', 'technology'] and t['subdomain'] == 'management':
            return 70
        if s['subdomain'] == 'management' and t['subdomain'] in ['engineering', 'technology']:
            return 40
        return 65

    # 5. Cross-domain (directional, bridge logic)
    # Tech/Engineering to Business/Management
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

    # 6. Distant, but possible (directional)
    if s['domain'] != t['domain']:
        # Allow some transitions, penalize reverse
        if s['domain'] == 'arts_humanities' and t['domain'] == 'engineering':
            return 20
        if s['domain'] == 'engineering' and t['domain'] == 'arts_humanities':
            return 10
        return 15

    # 7. Default
    return 10


import pandas as pd

courses = list(courses_db.keys())

matrix = pd.DataFrame(index=courses, columns=courses)
for source in course_names:
    for target in course_names:
        score = get_relevancy(source, target, courses_db)
        matrix.loc[source, target] = score if score is not None else ''

matrix.to_csv('hierarchical_relevancy_matrix.csv')
print("hierarchical_relevancy_matrix.csv generated.")