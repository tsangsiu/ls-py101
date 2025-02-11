def factors(number):
    divisor = number
    result = []
    while divisor > 0:        
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(-20))
print(factors(60))

'''
What is the purpose of `number % divisor == 0` in that code?

That is to check if `number` is divisble by `divisor`. If the remainder when
`number` divided by `divisor` is 0, it means that `number` is divisible by
`divisor`, and thus `divisor` is a factor of `number`.
'''