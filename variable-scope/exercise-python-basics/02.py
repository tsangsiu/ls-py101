# What will the following code do and why? Don't run it until you have tried to answer.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

'''
The above code will raise `UnboundLocalError`.

Upon the invocation of `my_function`, it initializes a new local variable `x`.
This local variable `x` shadows the `x` in the global scope initialized on
line 3. When we assign `x` to `x + 5`, it raises `UnboundLocalError` as the
local variable `x` does not have an assigned value yet.
'''