from students_data import students

def delete_student():
    searching_student= input("Enter the ID of student to Delete: ")
    for student in students:
        if student['student_id'] == searching_student: 
            students.remove(student)
            print(f"Student {searching_student} Deleted successfully \n")
            return
    print("student not found")   