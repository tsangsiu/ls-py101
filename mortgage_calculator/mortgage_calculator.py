import json
import os
import math

RATE_TO_PERCENT = 0.01
MONTHS_PER_YEAR = 12

def message(message_key):
    return MESSAGES[message_key]

def prompt(msg):
    print(f'==> {msg}')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_valid_number(number_str):
    try:
        number = float(number_str)
    except ValueError:
        return False

    return not(math.isnan(number) or math.isinf(number))

def is_valid_int(number_str):
    try:
        int(number_str)
    except ValueError:
        return False

    return True

def is_valid_loan_amount(load_amount_str):
    return is_valid_number(load_amount_str) and float(load_amount_str) >= 0

def is_valid_loan_dur_year(loan_dur_year):
    return is_valid_int(loan_dur_year) and int(loan_dur_year) >= 0

def is_valid_loan_dur_month(loan_dur_month):
    return is_valid_int(loan_dur_month) and int(loan_dur_month) >= 0

def is_valid_apr(apr_str):
    return is_valid_number(apr_str) and float(apr_str) >= 0

def get_loan_amount():
    while True:
        prompt(message('get_loan_amount'))
        loan_amount = input()

        if is_valid_loan_amount(loan_amount):
            break

        prompt(message('invalid_loan_amount'))

    return float(loan_amount)

def get_apr():
    while True:
        prompt(message('get_apr'))
        apr = input()

        if is_valid_apr(apr):
            break

        prompt(message('invalid_apr'))

    return float(apr) * RATE_TO_PERCENT

def get_loan_dur_year():
    while True:
        prompt(message('get_loan_dur_year'))
        loan_dur_year = input()

        if is_valid_loan_dur_year(loan_dur_year):
            break

        prompt(message('invalid_loan_dur_year'))

    return int(loan_dur_year)

def get_loan_dur_month():
    while True:
        prompt(message('get_loan_dur_month'))
        loan_dur_month = input()

        if is_valid_loan_dur_month(loan_dur_month):
            break

        prompt(message('invalid_loan_dur_month'))

    return int(loan_dur_month)

def get_loan_dur():
    """
    To get the loan duration in months.
    """

    while True:
        loan_dur_year = get_loan_dur_year()
        loan_dur_month = get_loan_dur_month()
        loan_dur = loan_dur_year * MONTHS_PER_YEAR + loan_dur_month

        if loan_dur > 0:
            break

        prompt(message('invalid_loan_dur'))

    return loan_dur

def calc_monthly_payment(loan_amount, apr, loan_dur):
    """
    Args:
        loan_amount: The loan amount in dollars.
        apr: The annual percentage rate.
        loan_dur: The loan duration in months.
    """

    if apr == 0:
        monthly_payment = loan_amount / loan_dur
    else:
        monthly_interest_rate = apr / MONTHS_PER_YEAR
        monthly_payment = loan_amount * monthly_interest_rate / \
                          (1 - (1 + monthly_interest_rate)**(-loan_dur))

    return monthly_payment

def ask_calc_again():
    while True:
        prompt(message('ask_calc_again'))
        prompt(message('display_yes_no_options'))
        calc_again = input().strip().upper()

        if calc_again in ['Y', 'N']:
            break

        prompt(message('invalid_yes_no'))

    return calc_again

def run_mortgage_calculator():
    clear()
    prompt(message('welcome'))

    while True:
        loan_amount = get_loan_amount()
        apr = get_apr()
        loan_dur = get_loan_dur()

        monthly_payment = calc_monthly_payment(loan_amount, apr, loan_dur)
        prompt(message('display_monthly_payment').format(monthly_payment))

        calc_again = ask_calc_again()
        clear()
        if calc_again == 'N':
            break

    prompt(message('goodbye'))

# Execution

with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)

run_mortgage_calculator()