import json
from data_base_helper import SqlHelper


class JsonHelper:
    def __init__(self):
        sql_obj = SqlHelper()

        self.data = sql_obj.get_data()  # get the data from data_base_helper | get data function

        self.list_clean_data = [json.dumps(x[1]) for x in self.data]

    def opening_data(self):
        return self.list_clean_data

    @staticmethod
    def adding_project(title, creation_time):
        sql_obj = SqlHelper()
        new_project = json.dumps({f"{title}": {"date of creation": creation_time, "last change": creation_time,
                                               "to_do": [], "working_on": [], "testing": [], "debug": [], "done": []}})
        sql_obj.writing_into_database(new_project)

    @staticmethod
    def delete_the_project(title_to_delete):
        sql_obj = SqlHelper()
        sql_obj.sql_delete_the_project(title_to_delete=title_to_delete)

    @staticmethod
    def select_project(data):
        sql_obj = SqlHelper()
        return sql_obj.check_the_project(data)

    @staticmethod
    def adding_task(project_title, task_title, new_task):
        sql_bj = SqlHelper()
        sql_bj.adding_task(tittle=project_title,task_title=task_title,new_task=new_task)
        print(project_title, task_title, new_task)
