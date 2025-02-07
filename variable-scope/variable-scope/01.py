# What will the following code print and why? Don't run it until you have tried to answer.

num = 5

def my_func():
    print(num)

my_func()

'''
The above code will print `5`.

Variables defined outside of a function can be accessed inside a function, hence
printing `5` when `my_func` is invoked.
'''