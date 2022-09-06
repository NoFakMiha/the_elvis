import psycopg2
import os


user = os.environ["POSTGRESUSER"]
sql_pw = os.environ["POSTGRESQLPW"]
sql_ip = os.environ["POSTGRESQLIP"]

conn = psycopg2.connect(
    database="postgres", user=user, password=sql_pw, host=sql_ip, port="8080"
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()