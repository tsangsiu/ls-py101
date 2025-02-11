print(0.3 + 0.6)         # 0.8999999999999999
print(0.3 + 0.6 == 0.9)  # False

'''
Most floating point representation used on computers lack a certain amount of 
precision.
'''

import math

print(0.3 + 0.6)
print(math.isclose(0.3 + 0.6, 0.9))