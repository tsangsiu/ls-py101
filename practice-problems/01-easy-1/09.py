advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

print(advice[:advice.index("house")])
print(advice.split("house")[0])