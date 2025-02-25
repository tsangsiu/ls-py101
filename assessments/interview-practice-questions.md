# Interview Practice Questions

*The following questions are from LSBot

## 1

Explain the difference between mutable and immutable objects in Python. Provide
example of each.

- Mutable objects are objects that can be altered after they are created.
- Immutable objects are objects that can't be altered after they are created.

## 2

What is the purpose of the `range()` function in Python? How would you use it to
create a list of even numbers from 2 to 20, inclusively?

- The `range()` function is the **type constructor** of range objects.
- `list(range(2, 21, 2))`

## 3

Describe the concept of variable scope in Python. What's the difference between
local and global variables?

- The concept of variable scope refers to where in a program a variable is
  accessible.
- Global variables can be accessed anywhere in a program, including inside
  functions.
- Local variables can only be accessed inside a function, but not outside of it.

## 4

Write a function that takes a string as input and returns a new string with all
vowels removed. Explain your approach.

```python
str_ = 'I go to school by bus.'

def remove_vowels(str_):
    vowels = ['a', 'e', 'i', 'o', 'u']

    for vowel in vowels:
        str_ = str_.replace(vowel, '')
        str_ = str_.replace(vowel.upper(), '')

    return str_

print(remove_vowels(str_))
```

## 5

What is the difference between `==` and `is` in Python? Provide an example where
they might produce different results.

- `==` checks for equality, i.e., if two objects concerned are equal in value.
- `is` checks for identity, i.e., if two objects concerned are the same object.

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]

list1 == list2  # True
list1 is list2  # False
```

## 6

Explain the concept of list comprehension in Python. Provide an example of how
you might use it to create a list of squares fo numbers from 1 to 10.

- List comprehension is a way to create lists from existing iterable
  collections.
- `[num**2 for num in range(1, 11)]`

Notes

- List comprehensions in Python are expressions.
- Expressions combine values, objects, operators, and/or calls to function
  to produce a new object.
- Unlike `for` loops, which are statements, they don't produce a new object.

## 7

What is the purpose of the `try`/`except` block in Python? Give an example of
when you might use it in a program.

- The purpose of the `try`/`except` block is for exception handling.
  - To handle potential errors gracefully without crashing the program
  - To allow the program to continue execution even if an error occurs
  - To provide custom error messages or alternative actions when exceptions are
    raised

- We put code that might raise errors in the `try` block. If it raise errors,
  instead of terminating the program, the `except` block is executed instead.
- We can also specify what to execute instead with respect to different types of
  errors.

```python
try:
    num1 = 10
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError:
    print("The divider can't be 0.")
```

## 8*

Describe the difference between a `for` loop and a `while` loop in Python. In
what situations would you prefer to use one over the other?

- `for` loop
  - It is used when we want to iterate over a sequence or any iterable objects.
  - The number of iterations is typically known in advance.
  - Syntax: `for item in interable:`
- `while` loop
  - It is used when we want to repeat a block of code until a certain condition
    is met
  - The number of iterations is not necessarily known in advance
  - Syntax: `while condition:`

## 9

What is the difference between parameters and arguments in Python functions?
Provide an example to illustrate your explanation.

- Parameters act as placeholders for object references that would be passed into
  a function.
- Arguments are object references that are actually passed into a function.

```python
def add_one(num):
    return num + 1

add_one(1)  # 2
```

In the above code, `num` is a parameter of the function `add_one`, while `1` is
the argument that is passed into the function.

## 10*

Explain the concept of string formatting in Python. Compare and contrast the
`.format()` method and f-string. When might you use one over the other?

String formatting in Python allows us to create strings with dynmaic content.

- `.format()` method
  - available in earlier versions
  - uses placeholder `{}` in the string, which are then filled with values
  - syntax: `"string with {} placeholder".format(value)`
- f-strings (formatted string literals)
  - introduced in later Python versions
  - allows us to embed expressions inside string literals
  - prefixed with 'f' or 'F'
  - syntax: `f"string with {expression}"`

- use f-string when we are working with later versions of Python (3.6), as they
  are more readable and generally faster
- use `.format()` when we need backward compatibility with older Python versions


### 11

Is there anything we can do with a `for` loop but not with a comprehension?

- Side effects: Comprehensions are primarily designed for creating new
  collections, not for their side effects.

```python
r = range(10)

for num in r:
    print(r)
```

- Complex Logic: If our loop contains complex conditional statements or
  multiple operations that can't be expressed in a single expression,
  a `for` loop might be more appropriate.

- Breaking out of the loop: Comprehensions don't have a capability.

```python
r = range(10)

for num in r:
    if num == 3:
        break
```

- Accumulating results

```python
r = range(10)
sum_ = 0

for num in r:
    sum_ += num
```

- Nested loops with dependencies

### 12

What is the purpose of using a virtual environment in Python development?

- Manage project-specific dependencies without affecting the global Python
  environment.
- Avoid conflicts between different projects that require different library versions.
- Keep the development environment clean and portable.
- Ensure consistent development environments across different machines

### 13

In Python, what is the difference between a list and a dictionary?

- List: Sequence; Dictionary: Mapping
- List: Access element by indices; Dictionary: Access element by keys
- List: Order is important; Dictionary: Order is not important

### 14

What will be the output of this code, and what concept does it demonstrate?

```python
x = 5
y = 2
print(x // y)
print(x / y)
```

```python
print(x // y)  # 2, integer division
print(x / y)   # 2.5
```

### 15

Analyze this code snippet. What will it print, and what Python feature is being
used?

```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index + 1}: {fruit}")
```

```
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]

1: apple
2: banana
3: cherry
```

### 16

What will be the result of this code, and what concept is it illustrating?

```python
def modify_list(lst):
    lst.append(4)
    lst = [1, 2, 3]

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)
```

```
numbers -> [1, 2, 3, 4]
lst -> [1, 2, 3]

print(numbers) # => [1, 2, 3, 4]
```

### 17

Predict the output of this code and explain the concept it's demonstrating:

```python
x = 10
def func():
    global x
    x = 20
    print(x)

func()
print(x)
```

```
x -> 20
print(x) # => 20
print(x) # => 20
```

### 18

What will this code print, and what Python feature is being used?

```python
text = "Hello, World!"
print(text[::-1])
```

```
!dlroW ,olleH
```

### 19

Analyze this code. What will it output, and what concept is it demonstrating?

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(5)
print(result)
```

```
closure -> inner_function

def inner_function(y):
    return 10 + y

inner_function(5), result -> 15

print(result)  # 15
```

### 20

What will be printed by this code, and what Python feature is being used?

```python
numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers if num % 2 == 0]
print(squared)
```

```
squared -> [4, 16]
```

### 21

Predict the output of this code and explain the concept it's demonstrating:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))
```

```python
print(greet("Alice"))      # Hello, Alice!
print(greet("Bob", "Hi"))  # Hi, Bob!
```

### 22

What will this code print, and what Python feature is being illustrated?

```python
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))
```

```
result -> 24
print(result)  # 24
```

### 23

Analyze this code snippet. What will it output, and what concept is it demonstrating?

```python
original = {"a": 1, "b": 2}
copied = original.copy()
original["c"] = 3
print(copied)
print(original)
```

```
original -> {"a": 1, "b": 2, "c": 3}
copied -> {"a": 1, "b": 2}

{"a": 1, "b": 2}
{"a": 1, "b": 2, "c": 3}
```

### 24

What will be the output of this code?

```python
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)

outer()
```

```
x -> "nonlocal"
inner: nonlocal
outer: nonlocal
```

### 25

What will be the output of this code? What concept is it demonstrating?

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

```
a, b -> [1, 2, 3, 4]
[1, 2, 3, 4]
```

### 26

What will be the output of this code? What concept is it illustrating?

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
```

```
numbers -> [1, 2, 3, 4, 5]
even_numbers -> [2, 4]
```

### 27

What will this code print?

```python
text = "python is awesome"
capitalized = text.title()
print(capitalized)
```

```
text -> 'python is awesome'
capitalized -> 'Python Is Awesome'
```

### 28

What will be the output of this code? What concept is it demonstrating?

```python
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(result)
print(multiply("Hi", 3))
```

```
result -> 12
"Hi" * 3 == "HiHiHi"
```

### 29

Explain the difference between `append()` and `extend()` methods for lists in
Python

```python
lst = [1, 2, 3]

lst.append(4)
print(lst)  # [1, 2, 3, 4]

lst.extend([5])
print(lst)  # [1, 2, 3, 4, 5]
```

### 30*

What will be the output of the following code? Explain why.

```python
def modify_list(lst):
    lst += [4, 5]
    lst = lst + [6, 7]
    return lst

original = [1, 2, 3]
modified = modify_list(original)
print(original)
print(modified)
```

```
original -> [1, 2, 3, 4, 5]
lst, modified -> [1, 2, 3, 4, 5, 6, 7]
```

### 31

What does this code print and why?

```python
x = 10
def foo():
    global x
    x += 1
    y = x
    x = y + 1
    print("x =", x)
    print("y =", y)

foo()
print("x =", x)
```

```
y -> 11
x -> 12

x = 12
y = 11
x = 12
```

### 32

Explain what this code does and its output:

```python
def strange_sum(num):
    if num:
        return num + strange_sum(num - 1)
    return 0

print(strange_sum(5))
```

```
num -> 5
5 + strange_sum(4)
5 + 4 + strange_sum(3)
...
5 + 4 + 3 + 2 + 1 + strange_sum(0)
-> 5 + 4 + 3 + 2 + 1 + 0
-> 15
```

### 33

What will this code output? Explain the behavior of the `sorted()` function
with a key.

```python
words = ['apple', 'Banana', 'cherry', 'Date']
sorted_words = sorted(words, key=lambda x: x.lower())
print(sorted_words)
```

```
words -> ['apple', 'Banana', 'cherry', 'Date']
sorted_words -> ['apple', 'Banana', 'cherry', 'Date']

'A' < 'a'
['Banana', 'Date', 'apple', 'cherry']  # if the keyword parameter `key` were
omitted
```
