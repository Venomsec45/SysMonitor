import psutil
import sys
from rich import print as show
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from colors import custom_colors
from cpu.cpu_monitor import monitor
from memory.memory_monitor import memory_monitor
from disk.disk_status import disk
from system_information.information import sys_information
from network.network import network
from process.system_processes import processes

def main():
    border_custom_color = "rgb(10,217,240)"
    custom_color_1 = "rgb(247,247,247)"

    t = Text()

    # For building the layout
    layout = Layout()

    # To make a top and below columns
    layout.split_column(
        Layout(name="top", size=9),
        Layout(name="below")
    )

    # Filled with the system information
    layout["top"].split_row(
        Layout(name="information")
    )

    # Filled with two rows
    layout["below"].split_row(
        Layout(name="left", ratio=1),
        Layout(name="right", ratio=1)
    )


    # The left column from the below column
    layout["left"].split_column(
        Layout(name="cpu_and_memory", size=11),
        Layout(name="disk_and_memory")
    )

    # Rows from the upper column from the below column
    layout["cpu_and_memory"].split_row(
        Layout(name="cpu"),
        Layout(name="memory")
    )

    # Rows from the lower column from the below column
    layout["disk_and_memory"].split_row(
        Layout(name="disk"),
        Layout(name="network")
    )

    # From the below column
    layout["right"].split_column(
        Layout(name="processes")
    )

    layout["information"].update(Panel(sys_information(), title="[bold]SYSTEM INFORMATION[/bold]", border_style=custom_color_1))
    layout["cpu"].update(Panel(monitor(), title="[bold]CPU[/bold]", border_style=custom_color_1))
    layout["memory"].update(Panel(memory_monitor(), title="[bold]MEMORY[/bold]", border_style=custom_color_1))
    layout["disk"].update(Panel(disk(), title="[bold]DISK[/bold]", border_style=custom_color_1))
    layout["network"].update(Panel(network(), title="[bold]NETWORK[/bold]", border_style=custom_color_1))
    layout["processes"].update(Panel(processes(), title="[bold]PROCESSES[/bold]", border_style=custom_color_1))

    return Panel(layout, border_style=border_custom_color, expand=True)

with Live(main()) as live_monitor:
    while True:
        try:
            live_monitor.update(main())

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
        except KeyboardInterrupt:
            show("\n[red]Stopped[/red]")
            sys.exit(2)

        