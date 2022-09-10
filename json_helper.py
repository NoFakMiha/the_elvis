import json
from data_base_helper import SqlHelper

class JsonHelper:
    def __init__(self):
        sql_obj = SqlHelper()
        self.data = sql_obj.get_data()[1]

    def opening_data(self):
        return json.loads(self.data)

    def adding_project(self, title, creation_time):
        sql_obj = SqlHelper()
        new_project = {title:{"date of creation":{creation_time},"last change":creation_time}}
        sql_obj.writing_into_database(new_project)
