for i in range(1, 100, 2):
    print(i)

start_int = int(input("Please specify the starting value of the odd number to be printed: "))
end_int = int(input("Please specify the ending value of the odd number to be printed: "))
start_int = (start_int + 1 if start_int % 2 == 0 else start_int)
for i in range(start_int, end_int + 1, 2):
    print(i)