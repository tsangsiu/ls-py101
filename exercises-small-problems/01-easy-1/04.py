SQ_METERS_TO_SQ_FEET = 10.7639

length_meters = float(input("What is the length of the room in meters? "))
width_meters = float(input("What is the width of the room in meters? "))

area_sq_meters = length_meters * width_meters
area_sq_feet = area_sq_meters * SQ_METERS_TO_SQ_FEET

print()
print(f"The room's area in square meters is {area_sq_meters:.2f}.")
print(f"The room's area in square feet is {area_sq_feet:.2f}.")