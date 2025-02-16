# Questions from SPOT Wiki

## Type Coercions

### 1

Which variable is coerced? Is it an implicit or explicit coercion?

```python
x = 3.5
y = 5
z = x + y
```

The variable `x` is assigned to a float, and the variable `y` is assigned to an
integer. The variable `z` is coerced to a float. It is an implicit coercion
because there is no explicit coercion function used.

### 2

What coercion is happening here? Is it implicit or explicit?

```python
a = 1
b = 2
print(a + b)
```

When an integer is passed into a `print` function, it will be implicitly coerced
to a string before printing. That said, it is an implicit coercion.

### 3

What coercion is happening here? Is it implicit or explicit?

```python
month = "December"
day = int(input("What day is it? "))
print(f"Today is the {day} of {month}")
```

While explicit coercion happens on line 2, implicit coercion happens on line 3.

On line 2, it is expected to receive an input (day) from users. And the `int`
function explicitly coerces the input, which is a string, to an integer.

On line 3, the argument passed to the `print` function is an example of string
interpolation. Python interpolates the value referenced by `day`, which is an
integer, to form a string. It is implicit coercion.

## Numbers

### Basic Questions

- Are intgers and floats mutable or immutable?
  - Immutable
- Are integers and floats primitive or non-primitive?
  - Primitive
- Are integers and floats literals?
  - Literals
- What is a literal?
  - A literal is any syntactic notation that lets us directly represent an
    object in source code. As opposed to objects with no literal forms, we need
    to use a type constructor to create them.

### 1

What does this return and why? What concept does it illustrate?

```python
def convert_to_int(string):
    try:
        converted_integer = int(string)
        return converted_integer
    except ValueError:
        return "That string cannot be converted to an integer"

print(convert_to_int("hello"))
print(convert_to_int("5"))
```

...

### 2

What does this return and why? What concept does this illustrate?

```python
def division(number1, number2):
    numerator = number1
    denominator = number2

    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "The denominator cannot be zero"

print(division(5, 0))
```

...

### 3

What does this print and why? What concept does this demostrate?

```python
def addition(number1, number2):
    number1 += number2

x = 1
y = 2

addition(x, y)
print(f"x is {x}, y is {y}")
```

The above code will print `x is 1, y is 2`.

When we pass `x` and `y` into the function `addition`. The variables `number1`
and `number2` are respectively assigned to `1` and `2`. As both `x` and `y` both
reference an integer, which is immutable, there is no way that both `x` and `y`
are mutated in the function `addition`. Hence, when we print
`f"x is {x}, y is {y}"` on line 8, it prints `x is 1, y is 2`.

This demostrate immutability, and implicit coercion (in the `print` function).

### 4

What does this print and why? What concept does this illustrate? How would you
refactor this to remove the space?

```python
print(2 + 3 * 4, 4 * (3 + 2))
```

The above code prints `14 20`. ...

The concepts illustrated here are precedence and implicit coercion.

To remove the space in the output, we can do
`print(2 + 3 * 4, 4 * (3 + 2)), sep='')`

### 5

What can be used in place of commas to make this more readable?

```python
print(123112940)
```

We can use commas. For example, `print(123_112_940)`.

## Strings

### Basic Questions

- Are strings mutable or immutable?
  - Immutable
- Are strings primitive or non-primitive?
  - Primitive
  - Characters of a string are not stored as objects
- Are strings literals?
  - Yes
- What are text sequences?
  - Text sequences are strings of characters, which could include byte strings.
- What kind of characters are used in a string?
  - Unicode characters
  - A string is a text sequence of Unicode characters.
- Are text sequences the same as ordinary sequence?
  - No. Text sequences contain only characters, while ordinary sequences can 
    contain zero or more different objects.

### 1

What is the output of this code, and why? What is the concept illustrated here?

```python
str1 = "Hello, world!"
sub1 = str1[8:12]
print(sub1)
sub2 = str1[::-1]
print(sub2)
sub3 = str1[::2]
print(sub3)
```

The above code prints `orld`, `!dlrow ,olleH` and `Hlo ol!`.

...

The concept illustrated here is slicing.

### 2

What does this print and why? What concept is this?

```python
print("Hello\nWorld")
```

...

The code above demostrates the escape character `\n`.

### 3

What does this print and why? What concept is this?

```python
name = 'Alexander Graham Bell'
print(name[0])
```

...

The code above demostrates indexing strings.

## f-Strings

### Basic QUestions

- What are f-strings?
  - f-strings mean formatted strings. They are 'f'-prefixed string literals that
    let us interpolates expressions into a string.

### 1

What does this print and why? What is the concept?

```python
name = 'Abraham Lincoln'
print(f'{name} was a President of the US')
```

The above code prints `Abraham Lincoln was a President of the US`.

The argument passed into the `print` function is an f-string. It allows string
interpolation. The part with `{name}` interpolates with the object that `name`
references, which is `'Abraham Lincoln'`. The result string 
`Abraham Lincoln was a President of the US` is then passed into the `print`
function for printing.

## String Methods

### Basic Questions

- How do you identify a method versus a function?
  - A method is what follows after an object identifier or literal and an dot
    (`.`), while a function is what followed by a pair of parentheses, inside
    which is an expression or an object reference.

### 1

What does this print?

```python
mashup = 'thIs is How we type careLEssly'
cleaned = mashup.capitalize()
print(cleaned)
```

`This is how we type carelessly`

### 2

What do these print?

```python
stuff = 'tHIS iS bACKWARDS'
str1 = stuff.swapcase()
str2 = stuff.upper()
str3 = stuff.lower()
print(stuff)
print(str1)
print(str2)
print(str3)
```

```
tHIS is bACKWARDS
This Is Backwards
THIS IS BACKWARDS
this is backwards
```

### 3

What do these print?

```python
s1 = "Hello"
print(s1.isalpha())
s2 = "Hello World"
print(s2.isalpha())
s3 = "Hello!"
print(s3.isalpha())
s4 = "Hello123"
print(s4.isalpha())
s5 = ""
print(s5.isalpha())
s6 = "こんにちは"
print(s6.isalpha())
s7 = "HelloWorld"
print(s7.isalpha())
words = ["apple", "banana", "cherry"]
print(all(word.isalpha() for word in words))
```

```
True
False
False
False
False**
True**
True
True
```

### 4

What do these print?

```python
string1 = "HelloWorld"
string2 = "12345"
string3 = "Hello World"

result1 = string1.isalpha()
result2 = string2.isalpha()
result3 = string3.isalpha()

print("Is '{}' alphabetic?".format(string1), result1)
print("Is '{}' alphabetic?".format(string2), result2)
print("Is '{}' alphabetic?".format(string3), result3)
```

```
Is 'HelloWorld' alphabetic? True
Is '12345' alphabetic? False
Is 'Hello World' alphabetic? False
```

### 5

What do these print?

```python
s1 = "123abc"
print(s1.isdigit())
s2 = "123$%^"
print(s2.isdigit())
s3 = ""
print(s3.isdigit())
s4 = "12345"
print(s4.isdigit())
```

```
False
False
False
True
```

### 6

What do these print?

```python
print("Hello World".isalnum())
print("Hello@World".isalnum())
print("".isalnum())
print("Hello123".isalnum())
```

```
False
False
False
True
```

### 7

What do these print?

```python
name = 'HELLO'

if name.isupper():
    print("WORLD")
else:
    print("world")
```

`WORLD`

### 8

What do these print?

```python
def punctuation_type(str):
    if str.upper():
        print('This is all caps')
    elif str.lower():
        print('This is all lowercase')
    else:
        print('Neither')

str1 = 'HELLO'
str2 = 'yolo'
str3 = 'My Name Is: '

punctuation_type(str1)
punctuation_type(str2)
punctuation_type(str3)
```

```
This is all caps
This is all caps
This is all caps
```

### 9

What do these print?

```python
str1 = "    "
str2 = "  Hello   "
str3 = "Hello World"

print(str1.isspace())
print(str2.isspace())
print(str3.isspace())

sentence = "Hello     World!   How are you?   "
word_count = sum(1 for word in sentence.split() if word.isspace())
print("Number of words in the sentence:", word_count)
```

```
True
False
False
Number of words in the sentence: 0
```

### 10

What do these print?

```python
s = "   Hello, World!   "
print(s.strip())
print(s.strip(" !"))
```

```
Hello, World!
Hello, World
```

### 11

What does this print?

```python
s = "www.example.com"
print(s.lstrip('wcmo.'))
```

`example.com`

### 12

What do these print?

```python
s = 'impatient'
print(s.rstrip('tp'))
print(s.rstrip('p'))
```

```
impatien
impatient
```

### 13

What do these print?

```python
s = "Hello, World!"
print(s.replace("Hello", "Hi"))
print(s.replace("o", "0"))
```

```
Hi, World!
Hell0, W0rld!
```

### 14

What do these print?

```python
sentence = "This is a sample sentence."
words = sentence.split()
print(words)

csv_data = "John,Doe,30,New York"
fields = csv_data.split(",")
print(fields)

sentence = "This is a sample sentence."
words = sentence.split(maxsplit=2)
print(words)
```

```
['This', 'is', 'a', 'sample', 'sentence.']
['John', 'Doe', '30', 'New York']
['This', 'is', 'a sample sentence.']
```

### 15

What do these print?

```python
str1 = "hello world"
str2 = str1.capitalize()
print("Original string:", str1)
print("Capitalized string:", str2)
```

```
Original string: hello world
Capitalized string: Hello world
```

## Boolean vs. Truthiness

### Basic Question

- In Python, what values are considered falsy and what are considered truthy?
  - The following built-in values are considered falsy:
    - False
    - `None`
    - `0`, `0j`, `0.0`
    - `range(0)`
    - `[]`, `()`
    - `set()`, `frozenset()`
    - `{}`
    - `""`
  - All other built-in values are considered truthy.

### 1

What does this print?

```python
truthy_values = [1, 2, 3, "hello", [1, 2, 3], {"a": 1}, True, 0, "", [], {}, None, False]

print('Values:')
for value in truthy_values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")
```

```
Values:
1 is truthy
2 is truthy
3 is truthy
hello is truthy
[1, 2, 3] is truthy
{"a": 1} is truthy
True is truthy
0 is falsy
 is falsy
[] is falsy
{} is falsy
None is falsy
False is falsy
```

### 2

What do these print?

```python
x = 5
y = 10
z = 15

print(x > 0 and y < 20)
print(not x == y)
print(x < y and y < z)
print(x > y or y > z)
print(not (x > y))
```

```
True
True
True
False
True
```

### 3

What do these print?

```python
a = 10
b = 20

print(a < b < 30)
print(a > b or b == 20)
```

```
True
True
```

### 4

What do these print?

```python
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(6 not in my_list)
```

```
True
True
```

### 5

What does this print?

```python
temperature = 25
time_of_day = "morning"

if temperature < 30 and (time_of_day == "morning" or time_of_day == "afternoon"):
    print("It's a pleasant day!")
else:
    print("It's either too hot or not the right time of day.")
```

`It's a pleasant day!`

### 6

What does this print?

```python
num = 12

if num / 3 < 3 and num > 10:
    print("Hello")
elif num >= 8 and num < 6 or num > 4 and num < 16:
    print("Hello 2")
elif num % 4 == 0 or num < 7 and num < 10:
    print("Hello 3")
else:
    print("Buy")
```

`Hello 2`

## Ranges

### Basic Questions

- Is a range primitive or non-primitive?
  - Non-primitive
- Is a range mutable or immutable?
  - Immutable
- Do ranges have a literal form or a type constructor?
  - Type constructor
- Is a range a sequence or a collection?
  - A sequence
- What is the most common use of the range datatype?
  - Iteration
- Are ranges homogenous or heterogeneous?
  - Homogenous
- Why are ranges considered lazy?
  - It is because only the start and end points, and step if available, are
    stored. The individual elements are not created until we need them.

### 1

What do these print?

```python
print(range(0,10))
print(len(range(5, 15)))
print(my_range[1])
print(str(range(3, 7)))
print(list(range(12, 8, -1)))
print(list(range(5, 5, 1)))
print(5 in range(5))
print(5 not in range(5, 10))
```

```
range(0,10)
10
NameError
range(3, 7)
[12, 11, 10, 9]
[]
False
False
```

### 2

What does this print and why?

```python
example = range(0)
if example:
    print(list(example))
else:
    print(example)
```

The above code will print `range(0)`.

As `range(0)` is falsy, the `else`-block is executed, hence printing the object
that `example` references, which is `range(0)`.

### 3

What does this print?

```python
def number_range(number):
    match number:
        case n if n < 0:
            print(f'{number} is less than 0')
        case n if n <= 50:
            print(f'{number} is between 0 and 50')
        case n if n <= 100:
            print(f'{number} is between 51 and 100')
        case _:
            print(f'{number} is greater than 100')
number_range(0)
number_range(25)
```

```
0 is between 0 and 50
25 is between 0 and 50
```

## List and Dictionary Syntax

### Basic Questions

- What categories are lists and dictionaries?
  - They are sequences and mappings respectively.
- Are they mutable or immutable?
  - Mutable
- Are they primitive or non-primitive?
  - Non-primitive
- Are they literals, or do they require type constructors?
  - Literals
- Are they sequences?
  - While lists are sequences, dictionaries are not.
- Does the order of the elements in both matter?
  - The order matters in lists, but not in dictionaries.

## List Methods

### 1

What does this print?

```python
my_list = [1, 2, 3, 4, 5]
length_of_list = len(my_list)
print("Length of the list:", length_of_list)
```

`Length of the list: 5`

### 2

What does this print and why?

```python
lst_one = [0, 1, 2, 3]
lst_two = lst_one.append(4)
if lst_two:
    print(lst_two)
else:
    print(lst_one)
```

The above code prints `[0, 1, 2, 3, 4]`.

On line 1, `lst_one` is initialized to `[0, 1, 2, 3]`.

On line 2, the list referenced by `lst_one` is appended an element `4` at the
end. This operation is mutative. `lst_one.append(4)` returns `None` which is
assigned to `lst_two`. At this point, `lst_one` references `[0, 1, 2, 3, 4]`.

As `lst_two`, which references `None`, is falsy, the `else`-block is executed,
hence printing the object referenced by `lst_one`, which is `[0, 1, 2, 3, 4]`.

### 3

What does this print?

```python
my_list = [1, 2, 3, 4, 5]
ele = my_list.pop()
print("Popped element:", ele)
print("List after popping:", my_list)
ele1 = my_list.pop(1)
print("Popped element at index 1:", ele1)
print("Modified list after popping at index 1:", my_list)
```

```
Popped element: 5
List after popping: [1, 2, 3, 4]
Popped element at index 1: 2
Modified list after popping at index 1: [1, 3, 4]
```

### 4

What does this print?

```python
elements = [0, 1 , 2, "Dima"]
print(elements.reverse())
print(elements)
```

```
None
['Dima', 2, 1, 0]
```

### 5

What does this print?

```python
ages = {
    "dimo": 31,
    "olena": 32,
    "tetiana": 28
}

def get_val_of_dima(info):
    try:
        info['dimo']
        return info['dimo']
    except KeyError:
        return "Typo"

print(get_val_of_dima(ages))
```

`31`

### 6

What does this print?

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)
for key in keys:
    print(key)
```

```
a
b
c
```

### 7

What does this print?

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values)
for value in values:
    print(value)
```

```
1
2
3
```

### 8

What does this print?

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)
for key, value in items:
    print(key, value)
```

```
a 1
b 2
c 3
```

## Variable Scope, `global` Keyword, Variables as Pointers, Variable Shadowing

### 1

What does this print and why?

```python
name = 'John'

def greet():
    print(f"Hello, {name}!")

greet()
```

The above code prints `Hello, John!`.

Variables initialized outside of a function can be accessed inside the function.
Those variables are in the global scope. Therefore, when `greet` is invoked, the
string referenced by `name` is interpolated into the f-string on line 4 to form
`Hello, John!`, which is then printed by the `print` function.

### 2

What does this print and why?

```python
def assign():
    var = 20
    print(var)

assign()
```

The above code prints `20`.

When `assign` is invoked, the variable `var` is initialized to `20`, which is
then printed by the `print` function.

### 3

What does this print and why?

```python
try:
    print(var)
except NameError as e:
    print("Error occurred")
```

The above code prints `Error occurred`.

When the code attempts to print `var`, it raises `NameError` because `var` is
never initialized. The `except` block is executed, hence printing
`Error occurred`.

### 4

What does this print and why?

```python
var = 10

def function1():
    var = 20
    print(var)

function1()

try:
    print(var)
except NameError:
    print("Error occurred")

def function2():
    var += 5
    print(var)

try:
    function2()
except UnboundLocalError:
    print("Error occurred")

def function3():
    global var
    var += 5
    print(var)

function3()
print(var)
```

The above code prints:

```
20
10
Error occurred**
15
15
```

...

### 5

What does this print and why?

```python
var = 10

def function1():
    print(var)

function1()

def function2():
    var = 20
    print(var)

function2()
print(var)
```

The above code prints:

```
10
20
10
```

...

### 6

What does this print and why?

```python
def function1():
  x = 10

  def function2():
      y = 20
      print(x)

  function2()
  print(x)

function1()
print(x)
print(y)
```

The above code prints:

```
10
10
NameError
NameError
```

...

### 7

What does this print and why?

```python
var = 10

def access():
    print(var)
```

The above code prints nothing.

...