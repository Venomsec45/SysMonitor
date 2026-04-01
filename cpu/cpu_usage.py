from colors import custom_colors

def usage(usage: int) -> str:
    if usage >= 80:
        return custom_colors()[2]
    
    elif usage >= 48:
        return custom_colors()[1]
    
    else:
        return custom_colors()[0]