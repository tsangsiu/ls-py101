# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)

my_function()

'''
The above code will print `1`.

Upon the invocation of `my_function`, it prints `a`. As `a` is not defined in
the function, Python looks for it in the outer scope, which is the global 
scope on line 3. Hence it prints `1`.
'''