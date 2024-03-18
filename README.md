## Assignment 3 Q1 - Python SQL Scripting

- Name: Abdulrahman Awad
- Student ID: 101256090


### Install the required packages:

In order to connect to the database you need to install the `psycopg` package. You can install it using the following command:
```bash
pip install --upgrade pip           # upgrade pip to at least 20.3
pip install "psycopg[binary]"       # remove [binary] for PyPy
```

### Step 1: Reset and Create the database student table:

You can reset (delete existing tables) and create the database from scratch and the student table as well as populate the student table with initial values using the following command:

cd into the `DB_scripts` directory and run the `DB_create.py` file using the following command:

```bash
cd DB_scripts
python DB_create.py
```

### Step 2: Test CRUD operations on the student table:

cd into the `DB_scripts` directory and run the `test_script.py` file using the

following command:

```bash
cd DB_scripts
python test_script.py
```

### Project Structure (FILES):

- `DB_scripts/DB_create.py`: This file is used to create the database and the student table.
- `DB_scripts/crud_functions.py`: This file contains the CRUD functions that preform the crud operations on the student table by connecting to the database using psycopg.
- `DB_scripts/test_script.py`: This file is used to test the CRUD functions on the student table by calling the crud functions and displaying the records after each operation
- `README.md`: This file contains the instructions and information about the project.
- `DDL_Students.sql`: This file contains the DDL statements to create and insert into the student table.

### GITHUB Repository Link:
https://github.com/AbduAwad/Python_sql_scripting_A3

### Youtube Video Link:
https://youtu.be/gsQPT6gmXo8
