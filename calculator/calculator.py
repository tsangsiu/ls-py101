def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def invalid_yes_no(yes_no_str):
    return yes_no_str.lower() not in ['n', 'y', 'no', 'yes']

prompt('Welcome to Calculator!')

while True:
  prompt("What's the first number?")
  number1 = input()

  while invalid_number(number1):
      prompt("Hmm... that doesn't look like a valid number.")
      number1 = input()

  prompt("What's the second number?")
  number2 = input()

  while invalid_number(number2):
      prompt("Hmm... that doesn't look like a valid number.")
      number2 = input()

  prompt('What operation would you like to perform?\n'
         '1) Add 2) Subtract 3) Multiply 4) Divide')
  operation = input()

  while operation not in ['1', '2', '3', '4']:
      prompt("You must choose 1, 2, 3, or 4")
      operation = input()

  match operation:
      case '1':
          output = int(number1) + int(number2)
      case '2':
          output = int(number1) - int(number2)
      case '3':
          output = int(number1) * int(number2)
      case '4':
          output = int(number1) / int(number2)

  prompt(f'The result is: {output}')

  prompt('Would you like to do another calculation?\n'
         '[Y]es or [n]o?')
  calculate_again = input()

  while invalid_yes_no(calculate_again):
      prompt("Hmm... that doesn't look like a valid answer.\n"
             "Please enter [y]es or [n]o")
      calculate_again = input()

  if calculate_again.casefold().startswith('n'):
      break