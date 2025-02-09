numbers = [1, 2, 3, 4, 5]

numbers_reversed = numbers[::-1]
print(numbers)
print(numbers_reversed)

numbers_reversed = []
for number in numbers:
    numbers_reversed.insert(0, number)
print(numbers)
print(numbers_reversed)

numbers_reversed = list(reversed(numbers))
print(numbers)
print(numbers_reversed)