# What will the following code do and why? Don't run it until you have tried to answer.

if True:
    my_value = 20

print(my_value)

'''
The above code will print `20`.

It is because variables initialized inside a block is accessible outside of it,
unless the block if never executed.
'''

if False:
    my_new_value = 42

print(my_new_value)

'''
The above code will raise `NameError`.

As the if-condition is always falsy, the if-block is never executed. Although
`my_new_value` is in scope, it is never assigned a value. Hence raising 
`NameError` when we print it.
'''