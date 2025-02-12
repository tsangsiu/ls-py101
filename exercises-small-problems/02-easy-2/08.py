def oddities(list):
    return list[0::2]

def oddities(list):
    result = []
    idx = 0
    while idx < len(list):
        if idx % 2 == 0:
            result.append(list[idx])
        idx += 1
    
    return result

def oddities(list):
    result = []
    for idx in range(len(list)):
        if idx % 2 == 0:
            result.append(list[idx])
    
    return result

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

def evenities(list):
    return list[1::2]

print(evenities([2, 3, 4, 5, 6]) == [3, 5])
print(evenities([1, 2, 3, 4]) == [2, 4])
print(evenities(["abc", "def"]) == ['def'])
print(evenities([123]) == [])
print(evenities([]) == [])