# What will the following code print and why? Don't run it until you have tried to answer.

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

'''
The above code will print `Inner 1: 25` and 'Inner 2: 15`, each on its separate
line.

Upon the invocation of `my_func` on line 16, both `inner_func1` and
`inner_func2`, which are defined inside the definition of `my_func`, are
invoked.

When `inner_func1` is executed, it prints `Inner 1: 25`, which is
straightforward.

When `inner_func2` is execited, it prints `"Inner 2:"` and `x`. As `x` is not
defined in `inner_func2`, Python searches for it in the outer scope on line 4.
Hence printing `Inner 2: 15`.
'''