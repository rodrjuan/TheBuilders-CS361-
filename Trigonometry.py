import math

def calculate_trig_function(func, angle):
    angle_rad = math.radians(angle)
    
    if func == 'sin':
        return math.sin(angle_rad), math.sin(angle)
    elif func == 'cos':
        return math.cos(angle_rad), math.cos(angle)
    elif func == 'tan':
        return math.tan(angle_rad), math.tan(angle)
    elif func == 'asin':
        return math.degrees(math.asin(angle)), math.asin(angle)
    elif func == 'acos':
        return math.degrees(math.acos(angle)), math.acos(angle)
    elif func == 'atan':
        return math.degrees(math.atan(angle)), math.atan(angle)
    elif func == 'log':
        return math.log10(angle), math.log10(angle)
    elif func == 'ln':
        return math.log(angle), math.log(angle)
    else:
        return None
