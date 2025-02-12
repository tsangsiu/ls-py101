def ordinal_suffix(num):
    num_str = str(num)

    if num_str[-2:] in ["11", "12", "13"]:
        return "th"
    elif num_str[-1] == '1':
        return "st"
    elif num_str[-1] == '2':
        return "nd"
    elif num_str[-1] == '3':
        return "rd"
    else:
        return "th"
    
def century(year):
    century = year // 100
    if year % 100 != 0:
        century += 1
    
    return f'{century}{ordinal_suffix(century)}'

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True