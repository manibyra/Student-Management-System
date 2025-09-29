from add_students import add_students
from delete_student import delete_student
from search_student import search_student
from view_students import view_students
from update_details import update_details

def student_management_system():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit\n")        
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_students()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            update_details()
        elif choice == '6':
            print("End of Student Management System ")
            break
        else:
            print("Invalid choice, try again!\n")

student_management_system()