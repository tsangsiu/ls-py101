integer = int(input("Please enter an integer greater than 0: "))
operation = input('Enter "s" to compute the sum, '
                  'or "p" to compute the product. ')
print()

if operation == 's':
    result = sum(range(1, integer + 1))
    print(f'The sum of the integers between 1 and {integer} is {result}.')
elif operation == 'p':
    result = 1
    for i in range(1, integer + 1):
        result *= i
    print(f'The product of the integers between 1 and {integer} is {result}.')