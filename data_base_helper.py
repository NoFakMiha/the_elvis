import psycopg2
import os
from  sql_commands import commands


user = os.environ["POSTGRESUSER"]
sql_pw = os.environ["POSTGRESQLPW"]
sql_ip = os.environ["POSTGRESQLIP"]


try:

    conn = psycopg2.connect(
        database="postgres", user=user, password=sql_pw, host=sql_ip, port="5432"
    )

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Executing an MYSQL function using the execute() method
    cursor.execute("select version()")

    for command in commands:
        cursor.execute(command)


    conn.commit()
    conn.close()

except(Exception, psycopg2.DatabaseError) as error:
    print(error)
