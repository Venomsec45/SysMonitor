import psutil

def memory_usage():
    gigabytes = 1024 ** 3
    megabytes = 1024 ** 2
    mem_usage = psutil.virtual_memory()

    if any(mem >= gigabytes for mem in [mem_usage.total, mem_usage.used, mem_usage.available, mem_usage.free]):
        return [f"{mem_usage.total / gigabytes:.2f} GB",
                f"{mem_usage.used / gigabytes:.2f} GB",
                f"{mem_usage.available / gigabytes:.2f} GB",
                f"{mem_usage.free / gigabytes:.2f} GB"]
    
    elif any(mem >= megabytes for mem in [mem_usage.total, mem_usage.used, mem_usage.available, mem_usage.free]):
        return [f"{mem_usage.total / megabytes:.2f} MB",
                f"{mem_usage.used / megabytes:.2f} MB",
                f"{mem_usage.available / megabytes:.2f} MB",
                f"{mem_usage.free / megabytes:.2f} MB"]
    
    else:
        return [f"{mem_usage.total / 1024:.2f} KB",
                f"{mem_usage.used / 1024:.2f} KB",
                f"{mem_usage.available / 1024:.2f} KB",
                f"{mem_usage.free / 1024:.2f} KB"]