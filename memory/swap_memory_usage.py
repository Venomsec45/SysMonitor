import psutil

def swap_memory():
    return [
        f"{psutil.swap_memory().total}",
        f"{psutil.swap_memory().used}",
        f"{psutil.swap_memory().free}"
    ]