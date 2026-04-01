import psutil
import sys
from rich import print as show
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel



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
    # custom_color_2 = "rgb(10,198,245)"

    layout = Layout()
    layout.split_column(
        Layout(name="top", size=9),
        Layout(name="below")
    )

    layout["top"].split_row(
        Layout(name="information")
    )

    layout["below"].split_row(
        Layout(name="left", ratio=1),
        Layout(name="right", ratio=1)
    )

    layout["left"].split_column(
        Layout(name="cpu"),
        Layout(name="memory"),
        Layout(name="disk"),
        Layout(name="network")
    )

    layout["right"].split_column(
        Layout(name="processes")
    )

    layout["information"].update(Panel(sys_information(), title="System information", border_style=custom_color_1))
    layout["cpu"].update(Panel(monitor(), title="CPU", border_style=custom_color_1))
    layout["memory"].update(Panel(memory_monitor(), title="Memory", border_style=custom_color_1))
    layout["disk"].update(Panel(disk(), title="Disk", border_style=custom_color_1))
    layout["network"].update(Panel(network(), title="Network", border_style=custom_color_1))
    layout["processes"].update(Panel(processes(), title="Processes", border_style=custom_color_1))

    return Panel(layout, border_style=border_custom_color, expand=True)

with Live(main()) as live_monitor:
    while True:
        try:
            live_monitor.update(main())

        except psutil.NoSuchProcess:
            pass
    
        except KeyboardInterrupt:
            show("\n[red]Stopped[/red]")
            sys.exit(2)

        