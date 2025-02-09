def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

def is_color_valid(color):
    return color == "blue" or color == "green"

def is_color_valid(color):
    return not (color != "blue" and color != "green")

def is_color_valid(color):
    return color in ["blue", "green"]