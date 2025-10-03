from students_data import students

def view_students():
    if not students:
        print("NO students are there\n")
        return
    for i, student in enumerate(students, 1):
        print(f"{i}. student_id: {student['student_id']}, Name: {student['name']}, Course: {student['course']}, marks:{student['marks']}, Percentage: {student['percentage']} ")
    print()

