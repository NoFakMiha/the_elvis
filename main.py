import rich
from rich.console import Console
from rich.table import Table
import os
from json_helper import JsonHelper
from datetime import datetime


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
            table.add_row(row[1], str(row[2]), str(row[3]))
        console = Console()
        console.print(table)

    @staticmethod
    def showing_task_table(title, filtered_data_till_title):
        task_table = Table(title=f"Project:{title}")

        try:
            for row in filtered_data_till_title:
                column_tittles = row[0].keys()
                for tittle in column_tittles:
                    task_table.add_column(tittle)

        except:
            print(f"Your are in the Project: {title} but there are no column`s created! Crate new column!")


        console = Console()
        console.print(task_table)
#

def run_it():
    running = True
    main_console = TheMainConsole()
    main_console.showing_the_table(data=main_console.loading_json_data())
    while running:
        # Main Page
        user_decision = input("The project: ")
        # commands
        if "close" in user_decision:  # shut down the program
            running = False

        if "new" in user_decision:  # creating new project
            json_data.adding_project(tittle=user_decision.split("new")[1].replace(" ", ""),  # TODO: it is also taking space with it
                                     creation_time=now.strftime("%m.%d.%y | %H:%M:%S"))

            refresh = JsonHelper()
            new_refreshed_data = refresh.opening_data()
            main_console.showing_the_table(data=new_refreshed_data)
        # Task page
        elif "check" in user_decision:  # checking the  project
            running_in_project = True

            title = user_decision.split("check")[1].replace(" ", "")
            project_data = json_data.select_project(title)

            while running_in_project:
                main_console.showing_task_table(title=title, filtered_data_till_title=project_data)
                user_decision_in_the_project = input("The task:")

                if "new" in user_decision_in_the_project:
                    column_with_tittle = user_decision_in_the_project.split("new")[1]


                    try:
                        split_tittle_task = column_with_tittle.split()

                        json_data.adding_task(project_title=title, column_tittle=split_tittle_task[0],
                                              task=split_tittle_task[1])
                    except IndexError:
                        print("You forgot ether  give a name to the task or to which column the task should be assign "
                              "to")
                        pass
                if "close" in user_decision_in_the_project:
                    main_console.showing_the_table(data=main_console.loading_json_data())
                    running_in_project = False

        if "delete" in user_decision:
            title_to_delete = user_decision.split("delete")[1].replace(" ", "")
            json_data.delete_the_project(title_to_delete=title_to_delete)
            refresh_after_delete = JsonHelper()
            main_console.showing_the_table(refresh_after_delete.opening_data())


if __name__ == '__main__':
    run_it()
