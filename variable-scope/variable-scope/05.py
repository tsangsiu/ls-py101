# What will the following code do? Don't run it until you have tried to answer.

def my_func():
    num = 10

my_func()
print(num)

'''
The above code will raise `NameError`.

As functions has it own scope, variables initialized inside function are not 
accessible outside of it. Therefore, when we attempt to print `num` on line 7,
`num` is not in scope, hence raising `NameError`.
'''