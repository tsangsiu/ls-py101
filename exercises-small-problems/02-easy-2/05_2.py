def prompt(msg):
    return f'==> {msg}'

def calculate(num1, num2, operator):
    match operator:
        case '+':  return num1 + num2
        case '-':  return num1 - num2
        case '*':  return num1 * num2
        case '/':  return num1 / num2
        case '//': return num1 // num2
        case '%':  return num1 % num2
        case '**': return num1 ** num2

num1 = float(input(prompt('Enter the first number:\n')))
num2 = float(input(prompt('Enter the second number:\n')))

operators = ['+', '-', '*', '/', '//', '%', '**']
for operator in operators:
    result = calculate(num1, num2, operator)
    print(prompt(f'{num1} {operator} {num2} = {result}'))