a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))  # True

'''
Note: `id(a) == id(b) == id(c)` is equivalent to
`(id(a) == id(b)) and (id(b) == id(c))` 
'''