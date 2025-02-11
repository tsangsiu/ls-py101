def is_an_ip_number(word):
    return word.isdigit() and int(word) in range(256)

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    
    if len(dot_separated_words) != 4:
        return False
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

print(is_dot_separated_ip_address('255.255.255.255'))
print(is_dot_separated_ip_address('4.5.5'))
print(is_dot_separated_ip_address('1.2.3.4.5'))