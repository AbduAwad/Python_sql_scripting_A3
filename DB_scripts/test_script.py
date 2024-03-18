# import the CRUD.py functions and test them
from crud_functions import getAllStudents, addStudent, updateStudentEmail, deleteStudent

#import the date and time module

import datetime

def displayDB():
    print("--------------------------------------------------------------")
    print("Student ID | First Name | Last Name | Email | Enrollment Date")
    print("--------------------------------------------------------------")
    getAllStudents()
    print("--------------------------------------------------------------\n")


def menu():
    print("-------------------------")
    print("1. Get all students")
    print("2. Add a new student")
    print("3. Update student email")
    print("4. Delete student")
    print("0. Exit")
    print("-------------------------")
    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        choice = menu()
        if choice == '1':
            getAllStudents()
        elif choice == '2':
            first_name = input("Enter the first name of the student: ")
            last_name = input("Enter the last name of the student: ")
            email = input("Enter the email of the student: ")
            curr_date = datetime.datetime.now().strftime("%Y-%m-%d")
            addStudent(first_name, last_name, email, curr_date)
            displayDB()
        elif choice == '3':
            student_id = input("Enter the student id: ")
            email = input("Enter the new email: ")
            updateStudentEmail(student_id, email)
            displayDB()
        elif choice == '4':
            student_id = input("Enter the student id: ")
            deleteStudent(student_id)
            displayDB()
        elif choice == '0':
            break
        else:
            print("Invalid choice")

main()