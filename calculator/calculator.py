import json
import os

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

with open('lang_code_to_lang.json', 'r') as file:
    LANG_CODE_TO_LANG = json.load(file)

def message(message_key, lang_code="en"):
    return MESSAGES[lang_code][message_key]

def prompt(msg):
    print(f'==> {msg}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main Program

clear()
while True:
    prompt(message('choose_lang'))
    prompt(message('display_lang_options'))
    lang_code_num = input().strip()

    if lang_code_num in LANG_CODE_TO_LANG.keys():
        break

    prompt(message('display_valid_lang_code_nums'))
LANG_CODE = LANG_CODE_TO_LANG[lang_code_num]

clear()
prompt(message('welcome', LANG_CODE))

while True:
    while True:
        prompt(message('ask_first_number', LANG_CODE))
        number1 = input().strip()

        if not invalid_number(number1):
            break

        prompt(message('invalid_number', LANG_CODE))

    while True:
        prompt(message('ask_second_number', LANG_CODE))
        number2 = input().strip()

        if not invalid_number(number2):
            break

        prompt(message('invalid_number', LANG_CODE))

    while True:
        prompt(message('ask_operation', LANG_CODE))
        prompt(message('display_operation_options', LANG_CODE))
        operation = input().strip()

        if operation in ['+', '-', '*', '/']:
            break

        prompt(message('invalid_operation_option', LANG_CODE))

    try:
        match operation:
            case '+':
                result = float(number1) + float(number2)
            case '-':
                result = float(number1) - float(number2)
            case '*':
                result = float(number1) * float(number2)
            case '/':
                result = float(number1) / float(number2)
    except ZeroDivisionError:
        prompt(message('zero_division_error', LANG_CODE))
    else:
        prompt(message('display_result', LANG_CODE).format(RESULT = result))

    while True:
        prompt(message('ask_calculate_again', LANG_CODE))
        prompt(message('display_yes_no_options', LANG_CODE))
        calculate_again = input().strip()

        if calculate_again in ['0', '1']:
            break

        prompt(message('invalid_yes_no', LANG_CODE))

    if calculate_again == '0':
        clear()
        break

    clear()

prompt(message('goodbye', LANG_CODE))