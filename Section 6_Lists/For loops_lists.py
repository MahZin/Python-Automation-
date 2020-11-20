# for loops

range(4) # is the same as
range(0,4)

for i in [0, 1, 2, 3]:
    print(i)

# to make a long list of values...
list(range(4))
# space out by 2
list(range(0, 100, 2))
# assigning the list to a variable
spam = list(range(0, 100, 2))

# using i as an index to go through a list
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# assignment of variables in a list
cat = ['fat', 'orange', ' loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
# but there is a more efficient method
size, color, disposition = cat
# assigning multiple variables to multiple values
size, color, disposition = 'skinny', 'black', 'quiet'

# swapping variables
a = 'AAA'
b = 'BBB'
a, b = b, a

# augmented assignment operators
spam = 42
spam = 42 + 1
spam += 1 # this is the augmented operator
spam -= 1
spam /= 2
spam *= 2
spam %= 2
