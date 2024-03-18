import psycopg # import the psycopg module
import csv  # import the csv module

# READ FUNCTION: Retrieves and displays all the records from the student table in the database.
def getAllStudents():
    with psycopg.connect("dbname=Assignment_3_DB user=postgres password=postgres") as db: # connect to the database
        with db.cursor() as cursor: # create a cursor object to execute SQL queries
            cursor.execute("SELECT * FROM students") # execute the SQL query
            with open('students.csv', 'w', newline='') as file: # open a file in write mode
                writer = csv.writer(file) # create a csv writer object
                writer.writerow(['student_id', 'first_name', 'last_name', 'email', 'enrollment_date']) # write the header row
                for row in cursor: # iterate over the rows in the cursor
                    writer.writerow(row) # write the row to the file
                    print(row) # print the row to the console


# CREATE FUNCTION: Purpose: Adds a new student to the database.
def addStudent(first_name: str, last_name: str, email: str, enrollment_date: str): # add a new student to the database
    with psycopg.connect("dbname=Assignment_3_DB user=postgres password=postgres") as db: # connect to the database
        with db.cursor() as cursor: # create a cursor object to execute SQL queries
            # Convert the email to lowercase for case-insensitive comparison
            lowercase_email = email.lower() # convert the email to lowercase
            # Check if the email already exists in the database (case-insensitive)
            cursor.execute(f"SELECT * FROM students WHERE LOWER(email) = '{lowercase_email}'") # execute the SQL query
            existing_record = cursor.fetchone() # fetch the first record from the result set

            if existing_record: # if the record exists
                print(f"Student with email '{email}' already exists.") # print a message to the console
                return
            else: # if the record doesn't exist
                # Email doesn't exist, perform insert
                cursor.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')")
                db.commit()  # commits the transaction to the database.
                print(f"Student {first_name} {last_name} added to the database.") # print a message to the console


# UPDATE FUNCTION: Purpose: Updates the email of the student with the given student_id in the database.
def updateStudentEmail(student_id: int, email: str):
    with psycopg.connect("dbname=Assignment_3_DB user=postgres password=postgres") as db: # connect to the database
        with db.cursor() as cursor: # create a cursor object to execute SQL queries
            # check if the student_id exists in the database
            cursor.execute(f"SELECT * FROM students WHERE student_id = {student_id}") # execute the SQL query
            existing_record = cursor.fetchone() # fetch the first record from the result set
            if not existing_record: # if the record doesn't exist
                print(f"Student with student_id {student_id} does not exist.") # print a message to the console
                return
            cursor.execute(f"UPDATE students SET email = '{email}' WHERE student_id = {student_id}") # execute the SQL query
            db.commit() # commits the transaction to the database.
            print(f"Email for student with student_id {student_id} updated to {email}.") # print a message to the console


# DELETE FUNCTION: Purpose: Deletes the student with the given student_id from the database.
def deleteStudent(student_id: int): # delete a student from the database
    with psycopg.connect("dbname=Assignment_3_DB user=postgres password=postgres") as db: # connect to the database
        with db.cursor() as cursor: # create a cursor object to execute SQL queries
            # check if the student_id exists in the database
            cursor.execute(f"SELECT * FROM students WHERE student_id = {student_id}") # execute the SQL query
            existing_record = cursor.fetchone() # fetch the first record from the result set
            if not existing_record: # if the record doesn't exist
                print(f"Student with student_id {student_id} does not exist.") # print a message to the console
                return # exit the function
            else: # if the record exists
                cursor.execute(f"DELETE FROM students WHERE student_id = {student_id}") # execute the SQL query
                db.commit() # commits the transaction to the database.
                print(f"Student with student_id {student_id} deleted.")