def triangle(size):
    for n_row in range(1, size + 1):
        print(f'{' ' * (size - n_row)}{'*' * n_row}')

triangle(5)
triangle(9)