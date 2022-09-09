import rich
from rich.console import  Console
from rich.table import Table
import os
from json_helper import JasonHelper
from datetime import datetime



json_data = JasonHelper()
now = datetime.now()

class TheMainConsole:

    def clean_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def loading_json_data(self):
        return json_data.opening_data()

    def showing_the_table(self, data):
        extracting_data = data
        table = Table(title="Your list of projects")
        table.add_column("Created", justify="left", style="cyan", no_wrap=True)
        table.add_column("Title", justify="left", style="magenta")
        table.add_column("Last change", justify="left", )
        for row in extracting_data:
            table.add_row(row, extracting_data[row]['date of creation'], extracting_data[row]["last change"])
        console = Console()
        console.print(table)




def run_it():
    running = True
    main_console = TheMainConsole()
    main_console.showing_the_table(data=main_console.loading_json_data())
    while  running:
        user_decision = input("Please chose: ")

        if "close" in user_decision:
            running = False

        if "new" in user_decision:
            json_data.adding_data(title=user_decision.split("new")[1],
                                  creation_time=now.strftime("%m.%d.%y | %H:%M:%S"))
            main_console.showing_the_table(data=main_console.loading_json_data())



        if "check" in user_decision:
            print(user_decision.split("check")[1])



if __name__ == '__main__':
    run_it()