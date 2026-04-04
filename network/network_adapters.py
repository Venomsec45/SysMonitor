import netifaces
from rich.table import Table

def net_adapters():
    table = Table(show_header=True, box=None)
    table.add_column("NUMBER")
    table.add_column("ADAPTER")

    for index, net_adapter in enumerate(netifaces.interfaces(), start=1):
        table.add_row(str(index), str(net_adapter))

    return table