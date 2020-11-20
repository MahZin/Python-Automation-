# lists with indexes
spam = ['cat',  'bat', 'rat', 'elephant']
spam[0] # cat
spam[1] # bat

# lists in lists
spam2 = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam2[0] # ['cat', 'bat']
spam2[0][1] # bat
spam2[1][4] # 50

# reverse indexes
spam = ['cat',  'bat', 'rat', 'elephant']
spam[-1] # elephant
spam[-2] # rat

# Slice (gets multiple values from a list)
spam[1:3] # ['bat', 'rat']
#e valuates to a new list value

# assigning a new value to a list
spam = [10, 20, 30]
spam[1] = 'Hello'
spam # evaluates to [10, 'Hello', 30]
spam[1:3] = ['CAT', 'DOG', 'MOUSE']
spam # evaluates to [10, 'CAT', 'DOG', 'MOUSE']
# slice replaces values 1:3 (AKA the second and third value)

# can leave slice index empty
spam = ['cat',  'bat', 'rat', 'elephant']
spam[:2] # evaluates to ['cat', 'bat']
spam[1:] # evaluates to ['bat', 'rat', 'elephant']

# deleting values in a list
spam = ['cat',  'bat', 'rat', 'elephant']
del spam[2] # evaluates to spam = ['cat',  'bat', 'elephant']

# operating on strings vs lists
len('Hello') # 5
len([1, 2, 3]) # 3

'Hello' + 'world' # 'Hello world'
[1, 2, 3] + [4, 5, 6] # [1, 2, 3, 4, 5, 6]

'Hello' * 3 # 'HelloHelloHello'
[1, 2, 3] * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]

int('42') # 42
str(42) # '42'
list('Hello') # ['H', 'e', 'l', 'l', 'o']

'howdy' in ['hello', 'hi', 'howdy', 'heyas'] # True
'howdy' not in ['hello', 'hi', 'howdy', 'heyas'] # False


