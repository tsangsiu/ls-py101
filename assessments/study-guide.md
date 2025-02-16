# Study Guide

## Naming Conventions

- **idiomatic**
  - Names that follow the naming conventions

- **illegal**
  - Names that will raise `SyntaxError`
    - `is_numeric?`
  - Names that will do something unexpected
    - `str`, which will refine the `str()` function
    - keywords like `return` and `pass`

## Type Coercions

- Explcit
  - `int()`
  - `str()`

- Implicit
  - `x = 3.5; y = 5; z = x + y`
  - `print()`
  - f-strings, string interpolation

## Numbers

## Strings

## f-Strings

## String Methods

- `capitalize`, `swapcase`, `upper`, `lower`
- `isalpha`, `isdigit`, `isalnum`, `islower`, `isupper`, `isspace`
- `strip`, `rstrip`, `lstrip`, `replace`
- `split`, `find`, `rfind`

## Boolean vs. Truthiness

## `None`

## Ranges

## List and Dictionary Syntax

## List Methods

- `len(list)`, `list.append()`, `list.pop()`, `list.reverse()`

## Dictionary Methods

- `dict.keys()`, `dict.values()`, `dict.items()`
  - They return **dictionary view objects**.
- `dict.get()`

## Slicing (Strings, Lists, Tuples)

## Operators

- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%` (**modulo operator**), `**`
- String Operators: `+`
- List Operators: `+`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `and`, `or`, `not`
- Identity: `is`, `is not`
- Operator Precedence

## Mutability and Immutability

## Pass by Object Reference

## Variables

- Naming Conventions
- Initialization, Assignment, and Reassignment
- Scope
- `global` Keyword
- Variables as Pointers
- Variable Shadowing

## Conditionals and Loops

- `for`
- `while`

## `print()` and `input()`

## Exceptions

- `NameError`
- `TypeError`
- `SyntaxError`
- `ValueError`
- `IndexError`
- `KeyError`
- `ZeroDivisionError`

## Functions

- Definitions and Calls
- Return Values
- Parameters vs. Arguments
- Nested Functions
- Output vs. Return Values, Side Effects

## Expressions and Statements
