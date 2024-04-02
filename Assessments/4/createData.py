import os
import random
from datetime import datetime, timedelta

# Create folders to store the .txt files
if not os.path.exists("data"):
    os.makedirs("data")

# Define the number of records for each table
num_candidates = 17500
num_requisitions = 15000
num_departments = 10000
num_recruiters = 12500
num_applied_to = 20000
num_interviewed = 10000

# Generate random dates within a reasonable range (date without time)
def generate_random_date(start_date, end_date):
    time_difference = end_date - start_date
    random_days = random.randint(0, time_difference.days)
    random_date = start_date + timedelta(days=random_days)
    return str(random_date.date())

# List of 50 most common names in the USA
common_names = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth",
    "David", "Susan", "Joseph", "Jessica", "Charles", "Sarah", "Thomas", "Karen", "Christopher", "Nancy",
    "Daniel", "Lisa", "Matthew", "Betty", "Anthony", "Dorothy", "Donald", "Sandra", "Mark", "Ashley",
    "Paul", "Kimberly", "Steven", "Donna", "Andrew", "Emily", "Kenneth", "Michelle", "George", "Carol",
    "Joshua", "Amanda", "Kevin", "Melissa", "Brian", "Deborah", "Edward", "Stephanie", "Ronald", "Nadine"
]

# List of education levels
education_levels = ["PhD", "MBA/MS/MA", "BS/BA", "HS/GED"]

# List of common department names
common_departments = [
    "Sales", "Marketing", "Finance", "Human Resources", "Engineering",
    "Customer Support", "Research and Development", "IT", "Operations", "Legal"
]

# List of random states in the USA
random_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

# List of common position titles with associated salary ranges
common_positions = {
    "CEO": (150000, 300000),
    "CFO": (120000, 250000),
    "CTO": (110000, 240000),
    "CMO": (100000, 230000),
    "COO": (100000, 220000),
    "VP of Sales": (90000, 180000),
    "VP of Marketing": (90000, 180000),
    "VP of Finance": (90000, 180000),
    "VP of HR": (90000, 180000),
    "Director": (80000, 160000),
    "Manager": (60000, 120000),
    "Project Manager": (60000, 110000),
    "Software Engineer": (70000, 130000),
    "Data Scientist": (70000, 130000),
    "Marketing Manager": (60000, 120000),
    "Sales Manager": (60000, 120000),
    "HR Manager": (60000, 120000),
    "Financial Analyst": (55000, 100000),
    "Accountant": (50000, 95000),
    "Customer Support Specialist": (40000, 75000),
    "Legal Counsel": (70000, 130000),
    "Researcher": (60000, 120000),
    "IT Specialist": (60000, 120000),
    "Operations Manager": (60000, 120000)
}

# Initialize sets to track used IDs for primary keys
used_candidate_ids = set()
used_requisition_ids = set()
used_department_ids = set()
used_recruiter_ids = set()

# Create and populate Candidates.txt
with open("data/Candidates.txt", "w") as file:
    for can_id in range(1, num_candidates + 1):
        can_id_str = int("{:05d}".format(can_id))
        name = random.choice(common_names)
        education = random.choice(education_levels)
        candidate_data = "c{},{},{}\n".format(can_id_str, name, education)
        file.write(candidate_data)
        used_candidate_ids.add(can_id_str)

# Create and populate Departments.txt
with open("data/Departments.txt", "w") as file:
    for dep_id in range(1, num_departments + 1):
        dep_id_str = int("{:04d}".format(dep_id))
        department_name = random.choice(common_departments)
        manager_name = random.choice(common_names)
        department_data = "d{},{},{}\n".format(dep_id_str, department_name, manager_name)
        file.write(department_data)
        used_department_ids.add(dep_id_str)

# Create and populate Recruiters.txt
with open("data/Recruiters.txt", "w") as file:
    for rec_id in range(1, num_recruiters + 1):
        rec_id_str = int("{:04d}".format(rec_id))
        name = random.choice(common_names)
        location = random.choice(random_states)
        recruiter_data = "r{},{},{}\n".format(rec_id_str, name, location)
        file.write(recruiter_data)
        used_recruiter_ids.add(rec_id_str)

# Create and populate Requisitions.txt
with open("data/Requisitions.txt", "w") as file:
    for req_id in range(1, num_requisitions + 1):
        req_id_str = int("{:05d}".format(req_id))
        date_open = generate_random_date(datetime(2024, 1, 1), datetime(2024, 1, 10))
        date_close = generate_random_date(datetime(2024, 1, 11), datetime(2024, 1, 30))
        position = random.choice(list(common_positions.keys()))
        salary_range = common_positions[position]
        salary = random.randint(salary_range[0], salary_range[1])
        requisition_data = "q{},d{},r{},{},{},{},{}\n".format(
            req_id_str,
            random.choice(list(used_department_ids)),
            random.choice(list(used_recruiter_ids)),
            position,
            salary,
            date_open,
            date_close
        )
        file.write(requisition_data)
        used_requisition_ids.add(req_id_str)

# Create and populate AppliedTo.txt
with open("data/AppliedTo.txt", "w") as file:
    for _ in range(num_applied_to):
        applied_to_data = "c{},q{},{}\n".format(
            random.choice(list(used_candidate_ids)),
            random.choice(list(used_requisition_ids)),
            generate_random_date(datetime(2024, 1, 1), datetime(2024, 1, 20))
        )
        file.write(applied_to_data)

# Create and populate Interviewed.txt
with open("data/Interviewed.txt", "w") as file:
    for _ in range(num_interviewed):
        interviewed_data = "c{},r{},{}\n".format(
            random.choice(list(used_candidate_ids)),
            random.choice(list(used_recruiter_ids)),
            generate_random_date(datetime(2024, 1, 1), datetime(2024, 1, 20))
        )
        file.write(interviewed_data)

print("Data files created and populated in the 'data' folder.")