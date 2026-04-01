import psutil
import os

def disk_usage():
    gigabytes = 1024 ** 3
    megabytes = 1024 ** 2
    dk_usage = psutil.disk_usage(os.path.abspath(os.sep))

    if any(usage >= gigabytes for usage in [dk_usage.total, dk_usage.used, dk_usage.free]):
        return [f"{dk_usage.total / gigabytes:.2f} GB", 
                f"{dk_usage.used / gigabytes:.2f} GB", 
                f"{dk_usage.free / gigabytes:.2f} GB"]
    
    elif any(usage >= megabytes for usage in [dk_usage.total, dk_usage.used, dk_usage.free]):
        return [f"{dk_usage.total / megabytes:.2f} MB", 
                f"{dk_usage.used / megabytes:.2f} MB", 
                f"{dk_usage.free / megabytes:.2f} MB"]
    
    else:
        return [f"{dk_usage.total / megabytes:.2f} KB", 
                f"{dk_usage.used / megabytes:.2f} KB", 
                f"{dk_usage.free / megabytes:.2f} KB"]