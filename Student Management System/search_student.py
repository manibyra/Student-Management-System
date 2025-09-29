from students_data import students

def search_student():
    if not students:
        print("NO students are there\n")
        return    
    searching_student= input("enter the ID of student to search: ")
    for student in students:
        if student['student_id'] == searching_student:
            print(f"student_id: {student['student_id']}, Name: {student['name']}, Course: {student['course']}, marks: {student['marks']}, Percentage: {student['percentage']}")
            print()
            return
    print("Student not found\n")
