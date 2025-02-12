from random import randint

name = input('What is your name? ').strip()
name = 'Teddy' if not name else name

age = randint(20, 100)
print(f'{name} is {age} years old!')