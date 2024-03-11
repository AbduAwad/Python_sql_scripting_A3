# import the CRUD.py functions and test them
from crud_functions import getAllStudents, addStudent, updateStudentEmail, deleteStudent

# Test the CRUD.py functions
print("TEST 1: GET ALL STUDENTS\n")
print("-----------------------------------\n")
getAllStudents() # get all students from the database
print("-----------------------------------\n")

print("TEST 2: ADD A NEW STUDENT\n")
print("-----------------------------------\n")
addStudent('Jason', 'SMITH', 'newEmail2@yahoo.com', '2021-10-01') # add a new student to the database
getAllStudents() # get all students from the database
print("-----------------------------------\n") 

print("TEST 3: UPDATE STUDENT EMAIL\n")
print("-----------------------------------\n")
updateStudentEmail(1, 'updatedEmail@cmail.com') # update the email of the student with student_id 1
print("After updating the email of the student with student_id 1:\n")
getAllStudents() # get all students from the database
print("-----------------------------------\n")

print("TEST 4: DELETE STUDENT\n")
print("-----------------------------------\n")
deleteStudent(1) # delete the student with student_id 1
print("After deleting the student with student_id 1:\n")
getAllStudents() # get all students from the database
print("-----------------------------------\n")



