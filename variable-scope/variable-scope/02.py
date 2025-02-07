# What will the following code print and why? Don't run it until you have tried to answer.

num = 5

def my_func():
    num = 10

my_func()
print(num)

'''
The above code will print `5`.

Inside the definition of the function `my_func`, a new local variable `num` is
initialized to `10`. This local variable `num` is independent of the global 
variable `num` defined on line 3. Hence, when the above code prints `num` on
line 9, it prints `5`, as the variable `num` defined on line 6 is not in scope.
'''