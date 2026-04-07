import psutil
from rich.text import Text
from rich.console import Group
from colors import custom_colors
from cpu.cpu_usage import usage

def monitor():
    return Group(
        Text("Usage: ").append(f"{psutil.cpu_percent(interval=1)}%", style=usage(psutil.cpu_percent(interval=1))),
        Text("Switches: ").append(f"{psutil.cpu_stats().ctx_switches}", style=custom_colors()[0]),
        Text("Interrupts: ").append(f"{psutil.cpu_stats().interrupts}", style=custom_colors()[0]),
        Text("Soft interrupts: ").append(f"{psutil.cpu_stats().soft_interrupts}", style=custom_colors()[0]),
        Text("Syscalls: ").append(f"{psutil.cpu_stats().syscalls}\n", style=custom_colors()[0]),
        Text("User: ").append(f"{psutil.cpu_times().user}", style=custom_colors()[0]),
        Text("System: ").append(f"{psutil.cpu_times().system}", style=custom_colors()[0]),
        Text("Idle: ").append(f"{psutil.cpu_times().idle}", style=custom_colors()[0])
    )