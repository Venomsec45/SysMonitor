from datetime import datetime
from rich.console import Group
from rich.text import Text
import platform


def sys_information():
    date_and_time = datetime.now().strftime("%m/%d/%Y_%H:%M:%S")
    return Group(
        Text(f"Hostname: {platform.node()}"),
        Text(f"System OS: {platform.platform()}"),
        Text(f"Version: {platform.system()} {platform.release()}"),
        Text(f"Machine: {platform.machine()}"),
        Text(f"Processor: {platform.processor()}"),
        Text(f"Architecture: {", ".join(list(platform.architecture()))}"),
        Text(f"Date and time: {date_and_time}")
    )