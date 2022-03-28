import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="student",port=3306)
# cursor = db.cursor()

try:
    sql = """SELECT * FROM EMPLOYEE
        WHERE age=19"""
    print ("Data fetched successfully")
except:
    print ("Error: unable to fetch data")   
db.close()

