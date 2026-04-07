import psutil

def partitions_usage():
    pr_usage = psutil.disk_io_counters()
    
    return [
        f"{pr_usage.read_bytes}",
        f"{pr_usage.write_bytes}"
    ]