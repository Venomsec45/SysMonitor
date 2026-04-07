import psutil

def swap_memory():
    sw_memory = psutil.swap_memory()
    gigabytes = 1024 ** 3
    megabytes = 1024 ** 2
    kilobytes = 1024

    if any(mem >= gigabytes for mem in [sw_memory.total, sw_memory.used, sw_memory.free]):
        return [
            f"{psutil.swap_memory().total / gigabytes:.2f} GB",
            f"{psutil.swap_memory().used / gigabytes:.2f} GB",
            f"{psutil.swap_memory().free / gigabytes:.2f} GB"
        ]
    
    elif any(mem >= megabytes for mem in [sw_memory.total, sw_memory.used, sw_memory.free]):
        return [
            f"{psutil.swap_memory().total / megabytes:.2f} MB",
            f"{psutil.swap_memory().used / megabytes:.2f} MB",
            f"{psutil.swap_memory().free / megabytes:.2f} MB"
        ]
    
    else:
        return [
            f"{psutil.swap_memory().total / kilobytes:.2f} KB",
            f"{psutil.swap_memory().used / kilobytes:.2f} KB",
            f"{psutil.swap_memory().free / kilobytes:.2f} KB"
        ]