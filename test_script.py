# import the CRUD.py functions
from Python_sql_scripting_A3.crud_functions import getAllStudents, addStudent, updateStudentEmail, deleteStudent

# Test the CRUD.py functions
getAllStudents()
print("-----------------------------------\n")
addStudent('Jason', 'SMITH', 'newEmail@yahoo.com', '2021-10-01')
print("After adding a new student:\n")
getAllStudents()
print("-----------------------------------\n")
updateStudentEmail(1, 'updatedEmail@cmail.com')
print("After updating the email of the student with student_id 1:\n")
getAllStudents()
print("-----------------------------------\n")
deleteStudent(1)
print("After deleting the student with student_id 1:\n")
getAllStudents()
print("-----------------------------------\n")



