def xor(operand1, operand2):
    return operand1 | operand2

def xor(operand1, operand2):
    return bool(operand1) + bool(operand2) == 1

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

'''
The `xor` function does not perform short-circuit evaluation of its operands.
Because it doesn't even make sense. We have to check the truthiness of both
operands to make sure that exactly one of the operands is truthy.
'''