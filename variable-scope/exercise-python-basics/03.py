# What will the following code do and why? Don't run it until you have tried to answer.

def my_function():
    a = 1

    if True:
        print(a)

my_function()

'''
The above code will print `1`.

Upon the invocation of `my_function`. The local variable `a` is initialized
to `1`. As the if-condition is always truthy, the if-block is then executed,
hence printing `1`. It is because variables initialized in the same where a
block begins is accessible inside the block.
'''