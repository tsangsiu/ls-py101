import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

with open('lang_code_to_lang.json', 'r') as file:
    LANG_CODE_TO_LANG = json.load(file)

def message(message_key, lang_code):
    return MESSAGES[lang_code][message_key]

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

# Main Program

lang_code = "en"

prompt(message('choose_lang', lang_code))
prompt(message('display_lang_options', lang_code))
lang_code_num = input()

while lang_code_num not in LANG_CODE_TO_LANG.keys():
    prompt(message('display_valid_lang_code_nums', lang_code))
    lang_code_num = input()
lang_code = LANG_CODE_TO_LANG[lang_code_num]

prompt(message('welcome', lang_code))

while True:
    prompt(message('ask_first_number', lang_code))
    number1 = input()

    while invalid_number(number1):
        prompt(message('invalid_number', lang_code))
        number1 = input()

    prompt(message('ask_second_number', lang_code))
    number2 = input()

    while invalid_number(number2):
        prompt(message('invalid_number', lang_code))
        number2 = input()

    prompt(message('ask_operation', lang_code))
    prompt(message('display_operation_options', lang_code))
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(message('invalid_operation_option', lang_code))
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

    prompt(message('display_result', lang_code).format(RESULT = result))

    prompt(message('ask_calculate_again', lang_code))
    prompt(message('display_yes_no_options', lang_code))
    calculate_again = input()

    while calculate_again not in ['1', '2']:
        prompt(message('invalid_yes_no', lang_code))
        calculate_again = input()

    if calculate_again == '2':
        break