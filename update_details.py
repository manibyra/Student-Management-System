from students_data import students

def  update_details():
    searching_student= input("Enter the ID of student to update: ")
    for student in students:
        if student['student_id'] == searching_student:    
            
            while True:
                print("Choose what you want to update\n a. Name \n b. Course \n c. Marks \n d. exit\n")
                
                choice = input("Your choice: ")

                if choice == 'a':
                    student['name'] = input("Enter new name: ")
                    print(f"Name updated successfully as {student['name']}\n")
                    
                elif choice == 'b':
                    student['course']= input("Enter new course: ")
                    print(f"Course updated successfully as {student['course']} \n")
                    
                elif choice == 'c':
                    while True:
                        print("Which subject you want to update \n i. maths \n ii. physics \n iii. chemistry \n'x' to exit marks updates\n")
                        subject_to_change = input(" Enter the subject no: ")
                        if subject_to_change == 'i':
                            student['marks']['maths'] = int(input("Enter new marks for Maths: "))
                        elif subject_to_change == 'ii':
                            student['marks']['physics'] = int(input("Enter new marks for Physics: "))
                        elif subject_to_change == 'iii':
                            student['marks']['chemistry'] = int(input("Enter new marks for Chemistry: "))
                        elif subject_to_change == 'x':
                            break
                        else:
                            print("choose correct subject ")
                            
                        student['percentage'] = round(sum(student['marks'].values())/300 * 100, 2)
                        print("Marks updated successfully\n")

                elif choice == 'd':
                    print("Exiting form updates \n")
                    return
                else:
                    print("Invalid choice!!, choosen a vaild choice ")
        
    print("Student not found\n")
   