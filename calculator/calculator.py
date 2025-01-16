import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

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

prompt(MESSAGES['welcome'])

while True:
  prompt(MESSAGES['ask_first_number'])
  number1 = input()

  while invalid_number(number1):
      prompt(MESSAGES['invalid_number'])
      number1 = input()

  prompt(MESSAGES['ask_second_number'])
  number2 = input()

  while invalid_number(number2):
      prompt(MESSAGES['invalid_number'])
      number2 = input()

  prompt(MESSAGES['ask_operation'])
  prompt(MESSAGES['show_operation_options'])
  operation = input()

  while operation not in ['1', '2', '3', '4']:
      prompt(MESSAGES['invalid_operation_option'])
      operation = input()

  match operation:
      case '1':
          result = int(number1) + int(number2)
      case '2':
          result = int(number1) - int(number2)
      case '3':
          result = int(number1) * int(number2)
      case '4':
          result = int(number1) / int(number2)

  prompt(MESSAGES['display_result'].format(RESULT = result))

  prompt(MESSAGES['ask_calculate_again'])
  calculate_again = input()

  while invalid_yes_no(calculate_again):
      prompt(MESSAGES['invalid_yes_no'])
      calculate_again = input()

  if calculate_again.casefold().startswith('n'):
      break