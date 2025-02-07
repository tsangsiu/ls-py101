# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

'''
The above code prints `2`.

On line 3, the variable `a` is initialized to `1`.

Upon the invocation of `my_function`, the same variable `a` is re-assigned to
`2` due to the presense of the `global` statement. Python does not create a 
new local variable `a` inside the function and refers to the `a` in the global
scope.

Hence, when we print `a` on line 10, it prints `2`.
'''