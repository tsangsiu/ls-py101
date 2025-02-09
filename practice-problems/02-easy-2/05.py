numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers) is list)
print(type(table) is list)

print(type(numbers).__name__ == "list")
print(type(table).__name__ == "list")

print(isinstance(numbers, list))
print(isinstance(table, list))