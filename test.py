import datetime
import mysql.connector

cnx = mysql.connector.connect(user='Andrey', password = '12345678', database='sakila')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name FROM actor ")
        # "WHERE actor_id BETWEEN 10 AND 20")


cursor.execute(query)#, (hire_start, hire_end))
for (first_name, last_name) in cursor:
  print(last_name, first_name)

#cursor.close()
#cnx.close()