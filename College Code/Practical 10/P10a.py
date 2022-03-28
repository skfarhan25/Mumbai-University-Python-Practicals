import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",passwd="mysql",database="student",port=3306)
cursor = db.cursor()
sql = "CREATE Table LOGIN (NAME char(20) NOT NULL, PASSWORD char(20))"
cursor.execute(sql)
print("Table Created Successfully")
db.close()