import psycopg # import the psycopg module

# Purpose: Creates a new student table in the database.
def createStudentTable():
    with psycopg.connect("dbname=Assignment_3_DB user=postgres password=postgres") as db: # connect to the database
        with db.cursor() as cursor: # create a cursor object to execute SQL queries
            cursor.execute("""  
                CREATE TABLE students (
                    student_id SERIAL PRIMARY KEY,
                    first_name VARCHAR(255) NOT NULL,
                    last_name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    enrollment_date DATE
                );""") # execute the SQL query to create the student table in the database
            db.commit() # commits the transaction to the database.
            if cursor.rowcount > 0: # if the number of rows affected is greater than 0
                print("The table was successfully created.") # print a message to the console if the table was created

# Purpose: Populates the student table with sample data.
def populateTable(): # add a new student to the database
    with psycopg.connect("dbname=Assignment_3_DB user=postgres password=postgres") as db: # connect to the database
        with db.cursor() as cursor: # create a cursor object to execute SQL queries
            cursor.execute( 
                """
                INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
                    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
                    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
                    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
                """) # execute the SQL query to insert the records into the student table
            db.commit() # commits the transaction to the database.
            if cursor.rowcount > 0: # if the number of rows affected is greater than 0
                print("The records were successfully inserted.") # print a message to the console if the records were inserted

# Purpose: Drops the student table and recreates it with the default schema.
def resetDB():
    with psycopg.connect("dbname=Assignment_3_DB user=postgres password=postgres") as db: # connect to the database
        with db.cursor() as cursor: # create a cursor object to execute SQL queries
            cursor.execute("DROP TABLE IF EXISTS students") # execute the SQL query to drop the student table
            db.commit() # commits the transaction to the database.
            print("DATABASE RESTORED TO DEFAULT STATE") # print a message to the console

resetDB() # reset the database to the default state
createStudentTable() # create the student table
populateTable() # populate the student table with sample data