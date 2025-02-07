# What will the following code do and why? Don't run it until you have tried to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

'''
The above code prints `7`.

As integers are immutable, the invocation of `my_function` with `a` passed in
as argument does not alter the value that `a` points to. Hence, when we print
`a` on line 9, it prints `7`.
'''