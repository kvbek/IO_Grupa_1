def hours_to_min(hours: float):
    try:
        return float(hours) * 60
    except ValueError:
        print("Error: Parameter is not the correct type") 

def inch_to_cm(inch: float):
    try:
        return inch * 2.54
    except ValueError:
        print("Error: Parameter is not the correct type")

def km_to_mile(km: float):
    return km / 1.60934