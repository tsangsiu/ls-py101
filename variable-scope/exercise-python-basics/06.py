# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    a = 2

my_function()
print(a)

'''
The above code will print `1`.

Although `a` is initialized to `2` in `my_function`, it is not accessible in
the outer scope as it is confined in the function (function scope). Therefore,
when we print `a` on line 9, only the variable `a` initialized on line 1 is in
scope, hence printing `1`.
'''