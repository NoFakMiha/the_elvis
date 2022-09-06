import rich
from rich.console import  Console
from rich.table import Table
import os


running = True

while  running:

    table = Table(title="Your list of projects")


    table.add_column("Created", justify="left", style="cyan", no_wrap=True)
    table.add_column("Tittle",justify="left", style="magenta")
    table.add_column("Last change", justify="left",)

    table.add_row("05.09.2022 | 04:56", "The Elvis project", "05.09.2022 | 04:57")

    console = Console()

    console.print(table)

    user_decision = input("Please chose: ")

    if user_decision == "close":
        running = False
