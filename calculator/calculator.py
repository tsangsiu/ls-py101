import json

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

# Main Program

prompt(message('choose_lang'))
prompt(message('display_lang_options'))
lang_code_num = input()

while lang_code_num not in LANG_CODE_TO_LANG.keys():
    prompt(message('display_valid_lang_code_nums'))
    lang_code_num = input()
LANG_CODE = LANG_CODE_TO_LANG[lang_code_num]

prompt(message('welcome', LANG_CODE))

while True:
    prompt(message('ask_first_number', LANG_CODE))
    number1 = input()

    while invalid_number(number1):
        prompt(message('invalid_number', LANG_CODE))
        number1 = input()

    prompt(message('ask_second_number', LANG_CODE))
    number2 = input()

    while invalid_number(number2):
        prompt(message('invalid_number', LANG_CODE))
        number2 = input()

    prompt(message('ask_operation', LANG_CODE))
    prompt(message('display_operation_options', LANG_CODE))
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(message('invalid_operation_option', LANG_CODE))
        operation = input()

    match operation:
        case '1':
            result = float(number1) + float(number2)
        case '2':
            result = float(number1) - float(number2)
        case '3':
            result = float(number1) * float(number2)
        case '4':
            result = float(number1) / float(number2)

    prompt(message('display_result', LANG_CODE).format(RESULT = result))

    prompt(message('ask_calculate_again', LANG_CODE))
    prompt(message('display_yes_no_options', LANG_CODE))
    calculate_again = input()

    while calculate_again not in ['1', '2']:
        prompt(message('invalid_yes_no', LANG_CODE))
        calculate_again = input()

    if calculate_again == '2':
        break

prompt(message('goodbye', LANG_CODE))