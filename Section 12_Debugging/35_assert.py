# Assertion

# at a street, northsouth stoplight is grn, eastwest is red
market_2nd = {'ns': 'green', 'ew': 'red'}

# Let's define a function that can switch the lights

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    # assert something that must be true
    assert 'red' in intersection.values(), 'Neither light is red!' +  str(intersection)

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)

# AssertionErrors are for detecting programmer errors meant to be recovered from
# UserErrors should raise Exceptions
