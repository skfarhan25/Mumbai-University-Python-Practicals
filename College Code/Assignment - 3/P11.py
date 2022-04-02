import mysql.connector

MyDB = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="root"
)

MyCursor = MyDB.cursor()

MyCursor.execute("CREATE DATABASE mydatabase")

MyCursor.execute("""CREATE TABLE EMPLOYEE (
                    FIRST_NAME CHAR(20),
                    LAST_NAME CHAR(20),
                    AGE INT,
                    GENDER CHAR(1),
                    INCOME FLOAT)""")

sql = """INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, GENDER, INCOME)
        VALUES(%v, %v, %v, %v, %v)"""
val = [
    ('John', 'Doe', 21, 'M', 25000)
    ('Khan', 'Kilan', 30, 'M', 20000)
    ('Jane', 'Doe', 30, 'M', 15000)
]

MyCursor.execute(sql, val)

try:
    MyCursor.execute(sql, val)
    print("Data Inserted Successfully")
except:
    print("Error: Data Insertion Failed Successfully")

MyCursor.execute("SHOW TABLE EMPLOYEE")

MyDB.close()