def print_in_box(str_):
    str_len = len(str_)

    print(f'+{'-' * (str_len + 2)}+')
    print(f'|{' ' * (str_len + 2)}|')
    print(f'| {str_} |')
    print(f'|{' ' * (str_len + 2)}|')
    print(f'+{'-' * (str_len + 2)}+')

print_in_box('To boldly go where no one has gone before.')
print_in_box('')

# Further Exploration

def print_in_box(str_, box_width = None):
    if box_width is None:
        box_inner_width = len(str_)
    else:
        box_inner_width = box_width - 4

    horizontal_line = f'+-{'-' * box_inner_width}-+'
    empty_line = f'| {' ' * box_inner_width} |'

    print(horizontal_line)
    print(empty_line)
    print(f'| {str_[:box_inner_width]} |')
    print(empty_line)
    print(horizontal_line)

print_in_box('To boldly go where no one has gone before.')
print_in_box('To boldly go where no one has gone before.', box_width=20)
print_in_box('')

# Further Exploration

# assuming the length of each word in `str` does not exceed `max_len`
def wrap_str(str_, max_len):
    wrap_str_ = []

    _temp = []
    words = str_.split()
    for word in words:
        if len(' '.join(_temp + [word])) <= max_len:
            _temp.append(word)
        else:
            wrap_str_.append(' '.join(_temp))
            _temp = [word]

    if _temp:
        wrap_str_.append(' '.join(_temp))

    return wrap_str_

def print_in_box(str_, box_width=None):
    if box_width is None:
        box_inner_width = len(str_)
    else:
        box_inner_width = box_width - 4

    horizontal_line = f'+-{'-' * box_inner_width}-+'
    empty_line = f'| {' ' * box_inner_width} |'
    wrap_strs = wrap_str(str_, box_inner_width)

    print(horizontal_line)
    print(empty_line)
    for wrap_str_ in wrap_strs:
        print(f'| {wrap_str_}{' ' * (box_inner_width - len(wrap_str_))} |')
    print(empty_line)
    print(horizontal_line)

print_in_box('To boldly go where no one has gone before.')
print_in_box('To boldly go where no one has gone before.', box_width=30)
print_in_box('To boldly go where no one has gone before.', box_width=20)
print_in_box('To boldly go where no one has gone before.', box_width=12)
print_in_box('')