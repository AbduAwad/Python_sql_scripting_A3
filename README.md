### Install the required packages:

In order to connect to the database you need to install the `psycopg` package. You can install it using the following command:
```bash
pip install --upgrade pip           # upgrade pip to at least 20.3
pip install "psycopg[binary]"       # remove [binary] for PyPy
```

### Step 1: Reset and Create the database student table:

You can reset (delete existing tables) and create the database from scratch and the student table as well as populate the student table with initial values using the following command:
```bash
python DB_create.py
```

### Step 2: Test CRUD operations on the student table:

You can run the `crud.py` file to test the functions. You can run it using the following command:
```bash
python test_script.py


### Youtube Video Link:
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/1zvzW3J3l4E/0.jpg)](https://www.youtube.com/watch?v=1zvzW3J3l4E)