import psutil
from rich.console import Group
from rich.text import Text
from rich.table import Table
from colors import custom_colors
from disk.disk_usage import disk_usage

def disk():
    table = Table(expand=True, show_header=True, box=None)
    table.add_column("DISK")
    table.add_column("MOUNTPOINT")

    for disk in psutil.disk_partitions():
        table.add_row(disk.device, disk.mountpoint)

    return Group(
        Text("Total capacity: ").append(f"{disk_usage()[0]}", style=custom_colors()[0]),
        Text("Used capacity: ").append(f"{disk_usage()[1]}", style=custom_colors()[0]),
        Text("Free capacity: ").append(f"{disk_usage()[2]}\n", style=custom_colors()[0]),
        table
    )