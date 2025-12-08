from rich.table import Table
from rich.console import Console
from File import read_file


def Table_write():

    console = Console()
    table = Table(title="Tasks")

    table.add_column("No.", style="cyan", no_wrap=True)
    table.add_column("Task", style="magenta")
    table.add_column("Priority", style="yellow")
    table.add_column("Completion", style="bright_white")
    table.add_column("Due_date", justify="right", style="green")

    file_read = read_file("Task.json")
    for i, item in enumerate(file_read):
        completion = "✅" if item.get("Completion") else "❌"
        table.add_row(str(i + 1), str(item.get("Title", "")), str(item.get("Priority", "")), completion, str(item.get("Due_date", "")))

    console.print(table)