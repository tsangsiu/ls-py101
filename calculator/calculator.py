import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

with open('lang_code_to_lang.json', 'r') as file:
    LANG_CODE_TO_LANG = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

# Main Program

prompt(MESSAGES['choose_lang'])
prompt(MESSAGES['display_lang_options'])
lang_code_num = input()

while lang_code_num not in LANG_CODE_TO_LANG.keys():
    prompt(MESSAGES['display_valid_lang_code_nums'])
    lang_code_num = input()
lang_code = LANG_CODE_TO_LANG[lang_code_num]

prompt(MESSAGES[lang_code]['welcome'])

while True:
    prompt(MESSAGES[lang_code]['ask_first_number'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES[lang_code]['invalid_number'])
        number1 = input()

    prompt(MESSAGES[lang_code]['ask_second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES[lang_code]['invalid_number'])
        number2 = input()

    prompt(MESSAGES[lang_code]['ask_operation'])
    prompt(MESSAGES[lang_code]['display_operation_options'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(MESSAGES[lang_code]['invalid_operation_option'])
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

    prompt(MESSAGES[lang_code]['display_result'].format(RESULT = result))

    prompt(MESSAGES[lang_code]['ask_calculate_again'])
    prompt(MESSAGES[lang_code]['display_yes_no_options'])
    calculate_again = input()

    while calculate_again not in ['1', '2']:
        prompt(MESSAGES[lang_code]['invalid_yes_no'])
        calculate_again = input()

    if calculate_again == '2':
        break