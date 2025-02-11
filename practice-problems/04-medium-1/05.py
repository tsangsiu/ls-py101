nan_value = float("nan")

print(nan_value == float("nan"))  # False

'''
`nan` (not a number) is a special numeric value that indicates that an operation
that was intended to return a number but failed. Python doesn't let us use `==`
to determine if a value if `nan`.
'''

# To reliably test if a value is `nan`, we can do so by:
import math
print(math.isnan(float("nan")))