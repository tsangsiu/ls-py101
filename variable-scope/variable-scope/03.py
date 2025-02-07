# What will the following code print and why? Don't run it until you have tried to answer.

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

'''
The above code will print 10.

The `global` statement inside the definition of `my_func` tells Python that the
variable `num` defined on line 7 is the same as that on line 3. Therefore, when
`my_func` is invoked, the variable `num` on line 3 is reassigned to `10`. Hence,
when we print `num`, `10` is printed.
''' 