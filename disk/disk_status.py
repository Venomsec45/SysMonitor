import psutil
from rich.console import Group
from rich.text import Text
from rich.table import Table
from colors import custom_colors
from disk.disk_usage import disk_usage
from disk.disk_partitions_usage import partitions_usage

def disk():
    table = Table(expand=True, show_header=True, box=None)
    table.add_column("DISK")
    table.add_column("USAGE")

    for disk in psutil.disk_partitions():
        disk_partition_usage = psutil.disk_usage(disk.mountpoint)
        table.add_row(disk.device, f"[{custom_colors()[0]}]{str(disk_partition_usage.percent)}%[/{custom_colors()[0]}]")

    return Group(
        Text("Total capacity: ").append(f"{disk_usage()[0]}", style=custom_colors()[0]),
        Text("Used capacity: ").append(f"{disk_usage()[1]}", style=custom_colors()[0]),
        Text("Free capacity: ").append(f"{disk_usage()[2]}", style=custom_colors()[0]),
        Text("Read bytes: ").append(f"{partitions_usage()[0]}", style=custom_colors()[0]),
        Text("Write bytes: ").append(f"{partitions_usage()[1]}\n", style=custom_colors()[0]),
        table
    )