student_details = {
    'raman': 85,
    'reena': 90,
    'runnu': 56,
    'brandon': 100
}

entered_name = input("Enter the student's name: ").strip().lower()

if entered_name in student_details:
    print(f"{entered_name.title()}'s marks: {student_details[entered_name]}")
else:
    print("Student not found.")
