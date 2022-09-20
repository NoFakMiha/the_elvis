import rich
from rich.console import Console
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

    @staticmethod
    def showing_task_table(title, filtered_data_till_title):
        task_table = Table(title=f"Your are in project:{title}")
        task_table.add_column("To do")
        task_table.add_column("Working on")
        task_table.add_column("Testing")
        task_table.add_column("Debug")
        task_table.add_column("Done")

        filtered_data_till_title = filtered_data_till_title[1][title]

        for todo_task in filtered_data_till_title["to_do"]:
            task_table.add_row(todo_task)
        for working_on_task in filtered_data_till_title["working_on"]:
            task_table.add_row(working_on_task)
        for testing_task in filtered_data_till_title["testing"]:
            task_table.add_row(testing_task)
        for debug_task in filtered_data_till_title["debug"]:
            task_table.add_row(debug_task)
        for done_task in filtered_data_till_title["done"]:
            task_table.add_row(done_task)

        console = Console()
        console.print(task_table)


def run_it():
    running = True
    main_console = TheMainConsole()
    main_console.showing_the_table(data=main_console.loading_json_data())
    while running:
        user_decision = input("The project: ")
        # commands
        if "close" in user_decision:  # shut down the program
            running = False

        if "new" in user_decision:  # creating new project
            json_data.adding_project(title=user_decision.split("new")[1],  # TODO: it is also taking space with it
                                     creation_time=now.strftime("%m.%d.%y | %H:%M:%S"))

            refresh = JsonHelper()
            new_refreshed_data = refresh.opening_data()
            main_console.showing_the_table(data=new_refreshed_data)

        elif "check" in user_decision:  # checking the  project
            running_in_project = True

            title = user_decision.split("check")[1]
            project_data = json_data.select_project(title)

            while running_in_project:
                main_console.showing_task_table(title=title, filtered_data_till_title=project_data)
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
