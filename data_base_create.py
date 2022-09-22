import psycopg2
import os

USER = os.environ["POSTGRESUER"]
SQL_PW = os.environ["POSTGRESQLPW"]
SQL_IP = os.environ["POSTGRESQLIP"]

con = psycopg2.connect(database="postgres", user=USER, password=SQL_PW, host=SQL_IP,
                       port="5432")
cursor = con.cursor()

cursor.execute('''
   SELECT * FROM projects_and_task
''')
print(cursor.fetchall())
con.commit()
con.close()


