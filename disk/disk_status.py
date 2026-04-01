from rich.console import Group
from rich.text import Text
from colors import custom_colors
from disk.disk_usage import disk_usage

def disk():
    return Group(
        Text("Total disk capacity: ").append(f"{disk_usage()[0]}", style=custom_colors()[0]),
        Text("Used disk capacity: ").append(f"{disk_usage()[1]}", style=custom_colors()[0]),
        Text("Free disk capacity: ").append(f"{disk_usage()[2]}", style=custom_colors()[0])
    )