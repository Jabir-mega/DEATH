import sqlite3

connection = sqlite3.connect('Mydata.db')

cursor = connection.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS person(
    first_name TEXT
    last_name TEXT
    age INTERGER  
)      
 """)

connection.commit()

connection.close()