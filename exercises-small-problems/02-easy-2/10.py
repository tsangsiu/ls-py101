from datetime import datetime

year_now = datetime.now().year

current_age = int(input("What is your age? "))
retire_age = int(input("At what age would you like to retire? "))

years_to_go = retire_age - current_age
retirement_year = year_now + years_to_go

print()
print(f"It's {year_now}. You will retire in {retirement_year}. \n"
      f"You have only {years_to_go} years of work to go!")