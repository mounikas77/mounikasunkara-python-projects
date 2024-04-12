import mysql.connector

# create a database connection
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="mounika123",
    database="mounikabujji"
)
cursor=db_connection.cursor()
sql_query="select * from smouni"
cursor.execute(sql_query)
result=cursor.fetchall()
for row in result:
    print(row)
cursor.close()
db_connection.close()



