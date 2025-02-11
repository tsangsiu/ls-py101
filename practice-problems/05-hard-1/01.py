def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())    # {'prop1': "hi there"}
print(second())   # None

# The above functions do not return the same value.