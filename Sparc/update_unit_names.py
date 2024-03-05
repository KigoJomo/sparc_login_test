#update_unit_names.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sparc.settings")
django.setup()

from main.models import Unit

electrical_engineering_subjects = [
    "Introduction to Electrical Engineering",
    "Circuit Theory",
    "Digital Signal Processing",
    "Power Systems",
    "Control Systems",
    "Electronics Design",
    "Communication Systems",
    "Electromagnetic Fields",
    "Power Electronics",
    "Renewable Energy Systems",
    "Electric Machines",
    "Instrumentation and Measurements",
    "Microelectronics",
    "Energy Conversion Systems",
    "High Voltage Engineering",
    "Advanced Control Systems",
    "Embedded Systems",
    "RF and Microwave Engineering",
    "VLSI Design",
    "Electric Drives and Automation",
    "Advanced Digital Signal Processing",
    "Nanoelectronics",
    "Power Quality",
    "Robotics",
    "Smart Grids",
    "Digital Control Systems",
    "Antennas and Propagation",
    "Electric Vehicle Technologies",
    "Biomedical Instrumentation",
    "Optical Communication",
    "Power System Protection",
    "Digital Image Processing",
    "FPGA-based Design",
    "Radar Systems",
    "Wireless Sensor Networks",
    "Energy Management Systems",
    "Computer-Aided Design (CAD)",
    "Advanced Power Electronics",
    "Optical Fiber Communication",
    "Control of Renewable Energy Systems",
    "Satellite Communication",
    "Cyber-Physical Systems",
    "Electric Traction Systems",
    "Advanced Embedded Systems",
    "Plasma Engineering",
    "Digital Communication",
    "System-on-Chip (SoC) Design",
    "Intelligent Control Systems",
    "Quantum Electronics",
    "Fault Diagnosis in Electrical Systems",
    "MEMS Technology",
    "Digital System Design with Verilog",
    "Computational Electromagnetics",
    "Electromagnetic Compatibility",
    "Power System Analysis and Optimization",
    "Digital VLSI Testing"
]

computer_science_subjects = [
    "Introduction to Computer Science",
    "Data Structures and Algorithms",
    "Object-Oriented Programming (OOP)",
    "Database Systems",
    "Operating Systems",
    "Computer Networks",
    "Software Engineering",
    "Web Development",
    "Artificial Intelligence",
    "Machine Learning",
    "Cybersecurity",
    "Mobile App Development",
    "Human-Computer Interaction",
    "Compiler Design",
    "Distributed Systems",
    "Cloud Computing",
    "Game Development",
    "Natural Language Processing",
    "Computer Graphics",
    "Big Data Analytics",
    "Cryptography",
    "Information Retrieval",
    "Parallel Computing",
    "Internet of Things (IoT)",
    "Blockchain Technology",
    "Computer Vision",
    "Embedded Systems",
    "Quantum Computing",
    "Evolutionary Algorithms",
    "Network Security",
    "Data Mining",
    "Advanced Databases",
    "Virtual Reality",
    "Wireless Networks",
    "Computational Complexity",
    "Computer Organization and Architecture",
    "Image Processing",
    "Advanced Algorithms",
    "Formal Methods in Software Engineering",
    "Information Security Management",
    "Social Media Analytics",
    "Software Testing and Quality Assurance",
    "Biometric Systems",
    "Operating System Security",
    "Cognitive Computing",
    "Enterprise Systems",
    "Pattern Recognition",
    "Advanced Web Technologies",
    "Bioinformatics",
    "Embedded Linux Systems",
    "Advanced Artificial Intelligence",
    "Quantum Information Science",
    "Embedded Java Programming",
    "Computational Biology",
    "Human-Robot Interaction",
    "Compiler Optimization Techniques"
]

business_information_technology_subjects = [
    "Principles of Management",
    "Business Communication",
    "Financial Accounting",
    "Marketing Strategies",
    "Business Information Systems",
    "Enterprise Resource Planning (ERP)",
    "Database Management",
    "E-Business Technologies",
    "IT Project Management",
    "Business Analytics",
    "Information Security Management",
    "Knowledge Management",
    "Strategic Management",
    "Organizational Behavior",
    "Business Law",
    "Operations Management",
    "Management Information Systems (MIS)",
    "Corporate Finance",
    "Cost Accounting",
    "International Business",
    "Supply Chain Management",
    "Entrepreneurship",
    "Human Resource Management",
    "Business Process Reengineering",
    "Change Management",
    "IT Governance",
    "Risk Management",
    "Strategic Information Systems Planning",
    "Business Ethics",
    "Corporate Social Responsibility",
    "Data Warehousing",
    "Business Intelligence",
    "Decision Support Systems",
    "IT Service Management",
    "Enterprise Architecture",
    "IT Audit and Compliance",
    "Customer Relationship Management (CRM)",
    "Project Portfolio Management",
    "IT Outsourcing",
    "Data Mining for Business",
    "Cloud Computing for Business",
    "Mobile Technologies in Business",
    "Social Media Marketing",
    "Business Process Modeling",
    "Business Continuity Planning",
    "IT Strategy and Policy",
    "IT Innovation",
    "Digital Transformation",
    "Corporate Governance",
    "IT for Sustainable Development",
    "Digital Marketing",
    "Emerging Technologies in Business",
    "Financial Management for IT Projects",
    "IT Entrepreneurship",
    "Global IT Management",
    "Corporate Information Security Governance"
]

information_technology_subjects = [
    "IT Fundamentals",
    "Computer Architecture",
    "System Analysis and Design",
    "Network Administration",
    "Database Design and Management",
    "Web Development Technologies",
    "Cybersecurity Fundamentals",
    "IT Ethics and Professionalism",
    "IT Service Management",
    "Cloud Computing",
    "Mobile Technologies",
    "IT Governance",
    "Operating Systems",
    "Data Structures and Algorithms",
    "Object-Oriented Programming (OOP)",
    "Computer Networks",
    "Software Engineering",
    "Database Systems",
    "Internet of Things (IoT)",
    "Business Information Systems",
    "IT Project Management",
    "Business Analytics",
    "Information Security Management",
    "Knowledge Management",
    "Principles of Management",
    "Business Communication",
    "Financial Accounting",
    "Marketing Strategies",
    "Human Resource Management",
    "Enterprise Resource Planning (ERP)",
    "IT for Sustainable Development",
    "Social Media Analytics",
    "Business Intelligence",
    "Decision Support Systems",
    "IT Audit and Compliance",
    "Mobile App Development",
    "Web Security",
    "Network Security",
    "Wireless Networks",
    "IT Innovation",
    "Digital Transformation",
    "IT Entrepreneurship",
    "Data Mining for Business",
    "Cloud Computing for Business",
    "IT Strategy and Policy",
    "Cybersecurity Governance",
    "IT Outsourcing",
    "Project Portfolio Management",
    "Emerging Technologies in IT",
    "IT Disaster Recovery Planning",
    "Digital Marketing",
    "IT Risk Management",
    "IT for E-commerce",
    "IT Quality Management",
    "IT Change Management",
    "IT Sustainability"
]

def change_unit_names():
    engineering_units = Unit.objects.filter(course="E034")
    cs_units = Unit.objects.filter(course="C028")
    bbit_units = Unit.objects.filter(course="C027")
    it_units = Unit.objects.filter(course="C025")
    eng_counter = 0
    cs_counter = 0
    bbit_counter = 0
    it_counter = 0

    for unit in engineering_units:
        unit.name = electrical_engineering_subjects[eng_counter]
        unit.save()
        eng_counter = eng_counter + 1
        print(f"Updated {unit.name}")

    for unit in cs_units:
        unit.name = computer_science_subjects[cs_counter]
        unit.save()
        cs_counter = cs_counter + 1
        print(f"Updated {unit.name}")

    for unit in bbit_units:
        unit.name = business_information_technology_subjects[bbit_counter]
        unit.save()
        bbit_counter = bbit_counter + 1
        print(f"Updated {unit.name}")

    for unit in it_units:
        unit.name = information_technology_subjects[it_counter]
        unit.save()
        it_counter = it_counter + 1
        print(f"Updated {unit.name}")

if __name__ == "__main__":
    change_unit_names()
