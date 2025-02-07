# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

'''
The above code raise `UnboundLocalError`.

Upon the invocation of `my_function`, Python knows that `a` will be initialized
and hence creates a new local variable `a`. By the time when `a` is printed,
it is not assigned a value yet, Hence raising `UnboundLocalError`.
'''