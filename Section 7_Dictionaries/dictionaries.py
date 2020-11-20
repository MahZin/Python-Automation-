 # dictionaries: uses key-value pairs
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size'] # 'fat'
'My cat has' + myCat['color'] + 'fur.' # 'My cat has gray fur.'

spam = {12345: 'Luggage combination', 42: 'The Answer'}

# dictionaries are different than lists
[1, 2, 3] == [3, 2, 1] # False
# order matters

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'name': 'Zophie', 'age': 8}
eggs == ham # True
# order does not matter

# checking a key that does not exist in the dict
eggs['color'] # KeyError

# to check if a key does exist:
'name' in eggs # True
'name' not in eggs # False

# dictionaries, like lists, are muteable (changeable)
list(eggs.keys()) # ['name', 'species', 'age']
list(eggs.values()) # ['Zophie', 'cat', 8]
list(eggs.items()) # [('name', 'Zophie'), ('Species', 'cat'), ('age', 8)]
# using .items creates paired tuples

# print keys
for k in eggs.keys():
    print(k)
# name
# species
# age

for v in eggs.values():
    print(v)
# Zophie
# cat
# 8

for k, v in eggs.items():
    print(k, v)
# name Zophie
# species cat
# age 8

for i in eggs.items():
    print(i)
# ('name', 'Zophie')
# ('species', 'cat')
# ('age', 8)

# tuples are like lists except that are immuteable and use ()

# checking if a key or value is in a dictionary
'cat' in eggs.values() # True

# it's tedious to check if a key is in dict. Will crash program
# so we can use an 'if' statement
if 'color' in eggs:
    print(eggs['colors'])
# but this is also tedious, so we should use the 'get' method
eggs.get('age', 0) # if age is not in, return 0
eggs.get('color', '') # this returns

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) +
      ' to the picnic.')
# I am bringing 0 to the picnic
# without the 0 option, would result in a KeyError

# adding a key-value pair to a dict IF the key wasn't already in the dict
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
eggs.setdefault('color', 'black')
eggs # {'name': 'Zophie', 'color', 'black', 'species': 'cat', 'age': 8}
# you can not change the color to orange with the same command
