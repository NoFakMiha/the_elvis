import json
from data_base_helper import SqlHelper

class JsonHelper:
    def __init__(self):
        sql_obj = SqlHelper()

        self.data = sql_obj.get_data()  # get the data from data_base_helper | get data function

        self.list_clean_data = [json.dumps(x[1]) for x in self.data]

    def opening_data(self):

        return self.list_clean_data

    def adding_project(self, title, creation_time):
        sql_obj = SqlHelper()
        new_project = {title:{"date of creation":{creation_time},"last change":creation_time}}
        sql_obj.writing_into_database(new_project)
