import json


class JasonHelper:
    def __init__(self):
        self.x = '{"The Elvis":{"date of creation":"05.09.2022 | 04:56", "last change":"05.09.2022 | 04:57"}}'

    def opening_data(self):
        return json.loads(self.x)

    def adding_data(self, title, creation_time):
        new_project = {title:{"date of creation":{creation_time},"last change":creation_time}}
        json_data = json.loads(self.x)
        json_data.update(new_project)