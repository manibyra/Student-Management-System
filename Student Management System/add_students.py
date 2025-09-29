from students_data import students

def add_students():
    student_id = input("Enter Id: ")
    for roll_no in students:
        if roll_no['student_id'] == student_id :
            print(f"Student_id {student_id} 3is taken. Try again \n")
            return students
        
    name = input("Enter Name: ")
    course = input("Enter course: ")
    maths = int(input("Enter maths marks out of 100: "))
    physics = int(input("Enter physics marks out of 100: "))
    chemistry = int(input("Enter chemistry marks out of 100: " ))
    marks= {
        "maths": maths,
        "physics": physics,
        "chemistry": chemistry
    }
    percentage = round(( maths + physics + chemistry )/300 * 100, 2)
    student = {
        "student_id" : student_id,
        "name": name,
        "course": course,
        "percentage": percentage,
        "marks": marks
    }
    students.append(student)
    print(f"Student {name} added successfully \n")
    return students

