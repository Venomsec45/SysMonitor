import psutil
from rich.text import Text
from rich.console import Group
from colors import custom_colors
from cpu.cpu_usage import usage


def monitor():
    return Group(
        Text(f"CPU Usage: ").append(f"{psutil.cpu_percent(interval=1)}%", style=usage(psutil.cpu_percent(interval=1))),
        Text(f"CPU Switches: ").append(f"{psutil.cpu_stats().ctx_switches}", style=custom_colors()[0]),
        Text(f"CPU Interrupts: ").append(f"{psutil.cpu_stats().interrupts}", style=custom_colors()[0]),
        Text(f"CPU Soft interrupts: ").append(f"{psutil.cpu_stats().soft_interrupts}", style=custom_colors()[0]),
        Text(f"CPU Syscalls: ").append(f"{psutil.cpu_stats().syscalls}", style=custom_colors()[0])
    )