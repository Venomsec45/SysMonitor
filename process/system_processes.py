import psutil
from rich.table import Table
from rich.text import Text
from colors import custom_colors

def processes():
    table = Table(expand=True)
    table.add_column("PID")
    table.add_column("Process")
    # table.add_column("Date started")
    table.add_column("Status")
    table.add_column("Usage")

    processes = [
        process.info
        for process in psutil.process_iter(["pid", "name", "status", "cpu_percent"])
    ]

    top_processes = sorted(
        processes,
        key=lambda a: a["cpu_percent"],
        reverse=True
    )

    for process in top_processes:
        if process["cpu_percent"] >= 80:
            table.add_row(str(process["pid"]), str(process["name"]), str(process["status"]), Text(f"{process["cpu_percent"]}%", style=custom_colors()[2]))
        
        elif process["cpu_percent"] >= 48:
            table.add_row(str(process["pid"]), str(process["name"]), str(process["status"]), Text(f"{process["cpu_percent"]}%", style=custom_colors()[1]))

        else:
            table.add_row(str(process["pid"]), str(process["name"]), str(process["status"]), Text(f"{process["cpu_percent"]}%", style=custom_colors()[0]))        

    return table