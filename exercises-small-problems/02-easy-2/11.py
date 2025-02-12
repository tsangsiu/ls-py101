def center_of(str):
    if len(str) % 2 == 0:
        return str[(len(str) // 2 - 1):(len(str) // 2 + 1)]
    else:
        return str[len(str) // 2]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True