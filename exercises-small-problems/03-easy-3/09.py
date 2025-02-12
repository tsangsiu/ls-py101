def clean_up(str):
    output = ""
    for char in str:
        if char.isalpha():
            output += char
        elif not char.isalpha() and not output.endswith(' '):
            output += ' '

    return output

print(clean_up("---what's my +*& line?") == " what s my line ")