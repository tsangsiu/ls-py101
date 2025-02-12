bill = float(input("What is the bill? "))
tip_pct = float(input("What is the tip percentage? "))

tip = bill * tip_pct * 0.01
total = bill + tip

print()
print(f'The tip is ${tip:.2f}')
print(f'The total is ${total:.2f}')