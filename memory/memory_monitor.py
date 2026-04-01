from rich.text import Text
from rich.console import Group
from memory.memory_usage import memory_usage
from colors import custom_colors

def memory_monitor():
    return Group(
        Text("Total RAM: ").append(memory_usage()[0], style=custom_colors()[0]),
        Text("Used RAM: ").append(memory_usage()[1], style=custom_colors()[0]),
        Text(f"Available RAM: ").append(memory_usage()[2], style=custom_colors()[0]),
        Text(f"Free RAM: ").append(memory_usage()[3], style=custom_colors()[0])
    )