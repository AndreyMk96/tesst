import mysql.connector
import datetime
mydb = mysql.connector.connect(
    host = "localhost", user = "Andrey", password = "12345678",database = "workbase"
)

cursor = mydb.cursor()
#cursor.execute("CREATE DATABASE workbase")
"""cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)"""
#cursor.execute("CREATE TABLE my_table (name VARCHAR(255))")
temp = "test data"
#cursor.execute("INSERT INTO other_info(data) VALUES '%s'", temp)
cursor.execute("""INSERT INTO other_info(data, other_info)
                     VALUES ('%s','%s')
                     """ % (temp, str(datetime.datetime.now())))

mydb.commit()