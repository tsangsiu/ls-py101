def stringy(num):
    output = "10" * (num // 2)
    if num % 2 == 1:
        output += "1"

    return output

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True