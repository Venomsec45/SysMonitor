import psutil

def network_input_output():
    return [
        f"{psutil.net_io_counters().bytes_sent}",
        f"{psutil.net_io_counters().bytes_recv}",
        f"{psutil.net_io_counters().packets_sent}",
        f"{psutil.net_io_counters().packets_recv}"
    ]