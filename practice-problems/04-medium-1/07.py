munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)

'''
The family's data will get ransacked.

When we invoke `mess_with_demographics`, it iterates every pair of key and value
of the dictionary referenced by `munsters`. Note that every value in the
dictionary is another dictionary. For every pair of key and value, we do element
reassignment, which is mutative operation. This explains why the family's data
will get ransacked.
'''

print(munsters)