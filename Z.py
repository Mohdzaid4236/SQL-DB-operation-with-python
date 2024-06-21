import mysql.connector
from mysql.connector import errorcode

# MySQL database credentials
config = {
    'user': 'mohd_zaid',     
    'password': 'zaid@12345', 
    'host': '127.0.0.1',         
}

# Connect to MySQL server
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    print("Connected to MySQL server.")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    exit(1)

# Creating a new database
DB_NAME = 'school'
try:
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print(f"Database {DB_NAME} created successfully.")
except mysql.connector.Error as err:
    print(f"Failed to create database {DB_NAME}: {err}")
    exit(1)

# Connecting to the newly created database
config['database'] = DB_NAME
try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print(f"Database {DB_NAME} does not exist.")
    else:
        print(err)
        exit(1)

# Creating a new table
TABLES = {}
TABLES['students'] = (
    "CREATE TABLE IF NOT EXISTS `students` ("
    "  `student_id` INT AUTO_INCREMENT PRIMARY KEY,"
    "  `first_name` VARCHAR(50) NOT NULL,"
    "  `last_name` VARCHAR(50) NOT NULL,"
    "  `age` INT NOT NULL,"
    "  `grade` DECIMAL(5,2) NOT NULL"
    ") ENGINE=InnoDB")

# Create the table
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print(f"Creating table {table_name}: ", end='')
        cursor.execute(table_description)
        print("OK")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)

# Insert a new student record
add_student = ("INSERT INTO students "
               "(first_name, last_name, age, grade) "
               "VALUES (%s, %s, %s, %s)")
student_data = ('Alice', 'Smith', 18, 95.5)

try:
    cursor.execute(add_student, student_data)
    cnx.commit()
    print("Student record inserted successfully.")
except mysql.connector.Error as err:
    print(f"Failed to insert student record: {err}")

# Update the grade of the student with the first name "Alice"
update_grade = ("UPDATE students "
                "SET grade = %s "
                "WHERE first_name = %s")
new_grade = (97.0, 'Alice')

try:
    cursor.execute(update_grade, new_grade)
    cnx.commit()
    print("Student grade updated successfully.")
except mysql.connector.Error as err:
    print(f"Failed to update student grade: {err}")

# Delete the student with the last name "Smith"
delete_student = ("DELETE FROM students "
                  "WHERE last_name = %s")
last_name = ('Smith',)

try:
    cursor.execute(delete_student, last_name)
    cnx.commit()
    print("Student record deleted successfully.")
except mysql.connector.Error as err:
    print(f"Failed to delete student record: {err}")

# Fetch and display all student records from the "students" table
query = ("SELECT student_id, first_name, last_name, age, grade FROM students")

try:
    cursor.execute(query)
    print("All student records:")
    for (student_id, first_name, last_name, age, grade) in cursor:
        print(f"ID: {student_id}, Name: {first_name} {last_name}, Age: {age}, Grade: {grade}")
except mysql.connector.Error as err:
    print(f"Failed to fetch student records: {err}")

# Close the cursor and connection
cursor.close()
cnx.close()
print("Closed MySQL connection.")
