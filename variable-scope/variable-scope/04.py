# What will the following code print and why? Don't run it until you have tried to answer.

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

'''
The above code will print `Hello World`.

Upon the invocation of `outer`, `inner`, which is defined inside the method 
definition of `outer`, is invoked.

Upon the invocation of `inner`, it is instruction to print `outer_var` and
`inner_var`. As `outer_var` is not initialized inside `inner`, Python searches
for it in the outer scope on line 4, hence printing `Hello World`.
'''