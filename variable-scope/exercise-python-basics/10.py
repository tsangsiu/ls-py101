# What will the following code do and why? Don't run it until you have tried to answer.

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

'''
The above code will print `[10, 2, 3]`.

On line 1, the variable `b` in the global scope is assigned to the list
`[1, 2, 3]`.

Upon the invocation of `my_function`, it re-assignment the first element of `b`
to `10`. As `b` is not initialized inside the function, `my_function` looks for
it in the outer scope on line 3. As element re-assignment of list is mutative,
the list referenced by `b` is mutated to `[10, 2, 3]`.

Therefore, when we print `b` on line 9, it prints `[10, 2, 3]`.
'''