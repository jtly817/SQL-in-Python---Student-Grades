import pandas as pd
import random

# Generating Student info
student_info_strings = [
    'James Smith Male',
    'Mary Johnson Female',
    'John Williams Male',
    'Patricia Jones Female',
    'Robert Brown Male',
    'Jennifer Davis Female',
    'Michael Miller Male',
    'Linda Wilson Female',
    'William Moore Male',
    'Elizabeth Taylor Female',
    'David Anderson Male',
    'Barbara Thomas Female',
    'Joseph Jackson Male',
    'Susan White Female',
    'Charles Harris Male',
    'Jessica Martin Female',
    'Thomas Thompson Male',
    'Sarah Garcia Female',
    'Daniel Martinez Male',
    'Karen Roberts Female'
]

first_names = []
last_names = []
genders = []

for entry in student_info_strings:
    first, last, gender = entry.split()
    first_names.append(first)
    last_names.append(last)
    genders.append(gender)

# Step 3: Generate IDs and DOBs
student_ids = [f"{i+1:02d}" for i in range(20)]  
birthdays = [f"{random.randint(1, 12):02d}/{random.randint(1, 28):02d}/{random.randint(1985, 2004)}" for _ in range(20)]

# Step 4: Create DataFrame
student_info = {
    "Student_ID": student_ids,
    "First_Name": first_names,
    "Last_Name": last_names,
    "Gender": genders,
    "Date_Of_Birth": birthdays
}

# Create DataFrame for student info and save it to CSV
df_students = pd.DataFrame(student_info)
df_students.to_csv("student_info.csv", index=False)

# Generating student grades for different subjects
subjects = ['Math', 'English', 'Science', 'History', 'Art']
grades_data = []

# Generate random grades for each student and subject
for student_id in student_ids:
    for subject in subjects:
        grade = random.randint(50, 100)  
        date_recorded = f"{random.randint(1, 12):02d}/{random.randint(1, 29):02d}/{"2025"}" 
        grades_data.append([student_id, subject, grade, date_recorded])

# Create DataFrame for student grades and save to CSV
df_grades = pd.DataFrame(grades_data, columns=["Student_ID", "Course_Subject", "Course_Grade", "Date_Recorded"])
df_grades.to_csv("student_grades.csv", index=False)

print("CSV files 'student_info.csv' and 'student_grades.csv'")
