def multisum(number):
    result = 0
    for i in range(3, number + 1):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result
        
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)