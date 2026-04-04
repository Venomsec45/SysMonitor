import psutil
from rich.table import Table
from rich.text import Text
from colors import custom_colors

def processes():
    table = Table(expand=True)
    table.add_column("PID")
    table.add_column("Process")
    table.add_column("Username")
    table.add_column("Status")
    table.add_column("CPU Usage")
    table.add_column("Memory Usage")
    table.add_column("Threads")

    processes = [
        process.info
        for process in psutil.process_iter(["pid", "name", "username", "status", "cpu_percent", "memory_percent", "threads"])
    ]

    top_processes = sorted(
        processes,
        key=lambda a: a["cpu_percent"],
        reverse=True
    )

    try:
        for process in top_processes:
            if process["cpu_percent"] >= 80 or process["memory_percent"] >= 80:
                table.add_row(str(process["pid"]), str(process["name"]), str(process["username"]), str(process["status"]), Text(f"{process["cpu_percent"]}%", style=custom_colors()[2]), Text(f"{process["memory_percent"]}%", style=custom_colors()[2]), str(process["threads"]))
            
            elif process["cpu_percent"] >= 48 or process["memory_percent"] >= 48:
                table.add_row(str(process["pid"]), str(process["name"]), str(process["username"]), str(process["status"]), Text(f"{process["cpu_percent"]}%", style=custom_colors()[1]), Text(f"{process["memory_percent"]}%", style=custom_colors()[1]), str(process["threads"]))

            else:
                table.add_row(str(process["pid"]), str(process["name"]), str(process["username"]), str(process["status"]), Text(f"{process["cpu_percent"]}%", style=custom_colors()[0]), Text(f"{process["memory_percent"]}%", style=custom_colors()[0]), str(process["threads"]))        

    except TypeError:
          table.add_row(str(process["pid"]), str(process["name"]), str(process["username"]), str(process["status"]), "Access denied", "Access denied", "Access denied")        

    return table