import rich
from rich.console import  Console
from rich.table import Table
import os
from json_helper import JsonHelper
from datetime import datetime
import json



json_data = JsonHelper()
now = datetime.now()

class TheMainConsole:

    def clean_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def loading_json_data(self):
        return json_data.opening_data()

    def showing_the_table(self, data):
        extracting_data = data

        table = Table(title="Your list of projects")
        table.add_column("Title", justify="left", style="cyan", no_wrap=True)
        table.add_column("Created", justify="left", style="magenta")
        table.add_column("Last change", justify="left", )

        for row in extracting_data:
            to_dict = json.loads(row)
            for key in to_dict:
                table.add_row(key, to_dict[key]['date of creation'], to_dict[key]["last change"])
        console = Console()
        console.print(table)

    def showing_task_table(self, data):
        task_table = Table(title="Place Holder Project Name")
        task_table.add_column("To do", justify="left")
        task_table.add_column("Working on", justify="left")
        task_table.add_column("Testing")
        task_table.add_column("Debug")
        task_table.add_column("Done")

        console = Console()
        console.print(task_table)





def run_it():
    running = True
    main_console = TheMainConsole()
    main_console.showing_the_table(data=main_console.loading_json_data())
    running_in_project = True
    while  running:
        user_decision = input("The project: ")
        # commands
        if "close" in user_decision:  # shut down the program
            running = False

        if "new" in user_decision:  # creating new project
            json_data.adding_project(title=user_decision.split("new")[1], # TODO: it is also taking space with it
                                     creation_time=now.strftime("%m.%d.%y | %H:%M:%S"))

            refresh = JsonHelper()
            new_refreshed_data = refresh.opening_data()
            main_console.showing_the_table(data=new_refreshed_data)

        if "check" in user_decision:  # checking the  project
            while running_in_project:
                main_console.showing_task_table(data="Nothing")
                user_decision_in_the_project = input("The task:")

                if "new" in user_decision_in_the_project:
                    pass


                if "close" in user_decision_in_the_project:
                    main_console.showing_the_table(data=main_console.loading_json_data())
                    running_in_project = False

        if "delete" in user_decision:
            title_to_delete = user_decision.split("delete")[1]
            json_data.delete_the_project(title_to_delete=title_to_delete)
            refresh_after_delete = JsonHelper()
            main_console.showing_the_table(refresh_after_delete.opening_data())





if __name__ == '__main__':
    run_it()