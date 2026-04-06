import psutil

def partitions_usage():
    old_pr_usage = psutil.disk_io_counters()
    new_pr_usage = psutil.disk_io_counters()
    
    return [
        f"{new_pr_usage.read_bytes - old_pr_usage.read_bytes} %",
        f"{new_pr_usage.write_bytes - old_pr_usage.write_bytes} %"
    ]