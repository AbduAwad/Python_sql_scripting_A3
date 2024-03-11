import psycopg # import the psycopg module
# Retrieves and displays all the records from the student table in the database.
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
                );""")
            db.commit()
            if cursor.rowcount > 0:
                print("The table was successfully created.")


def populateTable(): # add a new student to the database
    with psycopg.connect("dbname=Assignment_3_DB user=postgres password=postgres") as db: # connect to the database
        with db.cursor() as cursor: # create a cursor object to execute SQL queries
            cursor.execute(
                """
                INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
                    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
                    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
                    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
                """)
            db.commit()
            if cursor.rowcount > 0:
                print("The records were successfully inserted.")

def resetDB():
    with psycopg.connect("dbname=Assignment_3_DB user=postgres password=postgres") as db:
        with db.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS students")
            db.commit()
            print("DATABASE RESTORED TO DEFAULT STATE")

resetDB()
createStudentTable()
populateTable()