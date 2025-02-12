def penultimate(str):
    words = str.split()
    return words[-2]

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

def middle(str):
    if not str.strip():
        return None
    
    words = str.split()

    if len(words) % 2 == 1:
        return words[len(words) // 2]
    else:
        return None

print(middle('') == None)
print(middle(' ') == None)
print(middle('   ') == None)
print(middle('last word') == None)
print(middle('Launch School is great!') == None)
print(middle('Launch School is very great!') == 'is')