import psycopg2
import os


USER = os.environ["POSTGRESUSER"]
SQL_PW = os.environ["POSTGRESQLPW"]
SQL_IP = os.environ["POSTGRESQLIP"]


class SqlHelper:
    def __init__(self):

        try:
            self.conn = psycopg2.connect(
                database="postgres", user=USER, password=SQL_PW, host=SQL_IP, port="5432"
            )
            self.cursor = self.conn.cursor()

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)


    def get_data(self):
        return self.cursor.fetchall()



    def writing_into_database(self, data):
        try:

            self.cursor.execute(f'''
            INSERT INTO projects(data)
            VALUES
            ({data})
            ''')
            self.conn.commit()
            self.conn.close()

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)











