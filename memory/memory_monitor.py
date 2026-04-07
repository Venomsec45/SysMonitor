from rich.text import Text
from rich.console import Group
from memory.memory_usage import memory_usage
from memory.swap_memory_usage import swap_memory
from rich.rule import Rule
from colors import custom_colors

def memory_monitor():
    return Group(
        Text("Total RAM: ").append(memory_usage()[0], style=custom_colors()[0]),
        Text("Used RAM: ").append(memory_usage()[1], style=custom_colors()[0]),
        Text("Available RAM: ").append(memory_usage()[2], style=custom_colors()[0]),
        Text("Free RAM: ").append(f"{memory_usage()[3]}\n", style=custom_colors()[0]),
        Text("Total swap: ").append(swap_memory()[0], style=custom_colors()[0]),
        Text("Used swap: ").append(swap_memory()[1], style=custom_colors()[0]),
        Text("Free swap: ").append(swap_memory()[2], style=custom_colors()[0]),
    )