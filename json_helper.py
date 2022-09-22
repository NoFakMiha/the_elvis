import json
from data_base_helper import SqlHelper


class JsonHelper:
    def __init__(self):
        sql_obj = SqlHelper()

        self.data = sql_obj.get_data()  # get the data from data_base_helper | get data function

        self.list_clean_data = [json.dumps(x[1]) for x in self.data]

    def opening_data(self):
        return self.data

    @staticmethod
    def adding_project(tittle, creation_time):
        sql_obj = SqlHelper()
        sql_obj.writing_into_database(tittle=tittle, timestamp=creation_time)

    @staticmethod
    def delete_the_project(title_to_delete):
        sql_obj = SqlHelper()
        sql_obj.sql_delete_the_project(title_to_delete=title_to_delete)

    @staticmethod
    def select_project(data):
        sql_obj = SqlHelper()
        return sql_obj.check_the_project(data)

    @staticmethod
    def adding_task(project_title, column_tittle):
        sql_bj = SqlHelper()
        column_tittle = json.dumps({column_tittle:[]})
        sql_bj.adding_task(tittle=project_title, column_tittle=column_tittle)
        #print(project_title, task_title, new_task)
