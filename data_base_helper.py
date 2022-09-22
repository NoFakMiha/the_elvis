import json

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
        self.cursor.execute(
            '''
            SELECT * FROM projects;
            '''

        )

        return self.cursor.fetchall()

    def writing_into_database(self, data):

        try:

            self.cursor.execute(f'''
            INSERT INTO projects(data)
            VALUES
            ('{data}')
            ''')
            self.commit_()
            self.close_connection()

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def sql_delete_the_project(self, title_to_delete):
        try:
            self.cursor.execute(
                f'''
                UPDATE projects SET data = data - '{title_to_delete}';
                '''
            )
            self.commit_()
            self.close_connection()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def check_the_project(self, data):
        try:
            self.cursor.execute(
                f'''
                SELECT * FROM projects
                WHERE data?'{data}'
                
                '''
            )

            return self.cursor.fetchone()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def adding_task(self, tittle, task_title, new_task):
        self.cursor.execute('''
                SELECT * FROM projects
                WHERE data ? ' the novak'->> 'last change'
                ''')

        print(self.cursor.fetchall())
        self.commit_()
        self.close_connection()

    def commit_(self):
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
