# Study Group

## 2025-02-21

### 1

What does the following code print?

```python
print(not '' and 2 < 3)  # True
print('' or [])          # []
print(0 or 2 >= 1.5 and 'c' > 'a')
# => print(0 or True)
# => True
```

#### Note

```python
print(1 or 2 >= 1.5 and 'c' > 'a')  # => 1
```

### 2

What does the following code print?

```python
lst1 = [0, 1, 2, 3]
lst2 = lst1.pop(0) and lst1.pop()

if lst2:
    print(2, lst2)
else:
    print(1, lst1)
```

```
lst1 -> [1, 2, 3]
lst2 -> 0
1 [1, 2, 3]
```

### 3

What does the following code print?

```python
def reverse_list1(lst):
    return lst[::-1]

def reverse_list2(lst):
    return lst.reverse()

lst = ['a', 'b', 'c', 'd']
print(reverse_list1(lst))
print(reverse_list2(lst))
```

```
reverse_list1(lst) -> ['d', 'c', 'b', 'a']
lst = ['d', 'c', 'b', 'a']
reverse_list2(lst) -> None
```

### 4

What does the following code print?

```python
text = 'Hello! I am Eloise.'

def swap(s):
    for char in s:
        s = s.replace(char, char.upper())
    return s

print(swap(text))
print(text)
```

```
HELLO! I AM ELOISE.
Hello! I am Eloise.
```

### 5

#### A

What does the following code print?

```python
greeting = 'Hello'

def greet(greeting):
    greeting += " world"
    print(greeting)

greet(greeting)
print(greeting)
```

```
greeting -> 'Hello'
=> greeting -> 'Hello world'

Hello world
Hello
```

#### B

What does the following code print? What concept does it illustrate?

```python
greeting = 'Hello'

def greet():
    greeting += " world"
    print(greeting)

greet()
print(greeting)
```

```
greeting = greeting + " world"
-> UnboundLocalError

Hello
```

### 6

What does the following code print?

```python
exclamation_marks = '!!!'

def shout(text):
    exclamation_marks = '¡¡¡'
    return text.upper() + exclamation_marks

print(shout('hello') + exclamation_marks)
```

```
HELLO¡¡¡!!!
```

### 7

What does the following code print?

```python
def shout(text):
    global exclamation_marks
    exclamation_marks = '!!!'
    return text.upper() + exclamation_marks

print(shout('hello') + exclamation_marks)
```

```
1. shout('hello')
HELLO!!!

2. exclamation_marks
!!!

HELLO!!!!!!
```

### 8

Write a function that increases all ages by 1.

```python
players = [
    {'name': 'Joe', 'age': 25},
    {'name': 'Andy', 'age': 31},
    {'name': 'Ralph', 'age': 18},
    {'name': 'Mark', 'age': 28},
]

# your code

age_players(players)
print(players)
```

```python
def age_players(lst):
    for player in lst:
        player['age'] += 1
    
    return None
```

### 9

What does the following code print?

```python
def modify_list1(lst):
    lst.append(5)
    return lst

def modify_list2(lst):
    lst = lst + [5]
    return lst

numbers = [1, 2, 3]
result1 = modify_list1(numbers)
result2 = modify_list2(numbers)

print(numbers)
print(result1)
print(result2)
```

```
numbers -> [1, 2, 3, 5] <- result1
result2 -> [1, 2, 3, 5, 5]
```

#### Note

`[1, 2, 3] + [4]` returns `[1, 2, 3, 4]`, but `[] + 4` raises `TypeError`,
because `[]` and `4` are of different types. 

### 10

What does the following code print?

```python
nums = [10, 20, 30, 40]
nums1 = nums.copy()
nums2 = nums.copy()

return_value1 = nums1.remove(30)
del nums2[2]

print(nums1)
print(nums2)

print(return_value1)
```

```
nums = [10, 20, 30, 40]
nums1 = [10, 20, 30, 40] -> [10, 20, 40]
nums2 = [10, 20, 30, 40] -> [10, 20, 40]

None
```

#### Note

As `del` is a statement just like an `if` statement, we cannot do
`print(del nums2[2])`.
