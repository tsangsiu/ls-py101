def multiply(num1, num2):
    return num1 * num2

def square(num):
    return multiply(num, num)

def power(num, power):
    result = 1

    for _ in range(power):
        result *= num
    
    return result

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

print(power(2, 3) == 8)
print(power(-3, 3) == -27)
print(power(2, 10) == 1024)