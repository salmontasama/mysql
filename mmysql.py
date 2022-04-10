import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#######",
    port="3306",
    database="sakila"
)
db_cursor = db.cursor()
db_cursor.execute("select * from actor")
actors = db_cursor.fetchall()
for actor in actors:
    print(actor)