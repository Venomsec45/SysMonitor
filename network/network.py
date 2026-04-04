from rich.console import Group
from rich.text import Text
from colors import custom_colors
from network.network_traffic import network_input_output
from network.network_adapters import net_adapters

def network():
    return Group(
        Text("Bytes sent: ").append(f"{network_input_output()[0]}", style=custom_colors()[0]),
        Text("Bytes received: ").append(f"{network_input_output()[1]}", style=custom_colors()[0]),
        Text("Packets sent: ").append(f"{network_input_output()[2]}", style=custom_colors()[0]),
        Text("Packets received: ").append(f"{network_input_output()[3]}", style=custom_colors()[0]),
        net_adapters()
    )