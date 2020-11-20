# list methods

spam = ['hello', 'hi', 'howdy' , 'heyas']
spam.index('hello') # evaluates to 0
index(hello) # NameError

spam.index('heyas') # 3
spam.index('sadasdsa') # ValueError

spam = ['Zophie', 'Pooka', 'Fat-Tail', 'Pooka']
spam.index('Pooka') # evaluates to first occurence: 1

# append method adds a value to the end of a list
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam # ['cat', 'dog', 'bat', 'moose']

# how to insert a value to a list at a particular index
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam  # ['cat', 'chicken', 'dog', 'bat']

# can only append and insert values into lists
eggs = 'hello'
eggs.append('world') # AttributeError

# remove method
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
spam # spam = ['cat', 'rat', 'elephant]

spam.remove('bat') # ValueError

# remove vs. del: remove lets you remove a specific value
# remove will remove the first occurence of the specified value

# sort() List method
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam # [-7, 1, 2, 3.14, 5]
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
spam # ['ants', 'badgers', 'cats', 'dogs', 'elephants']
spam.sort(reverse=True)
spam # ['elephants', 'dogs', 'cats', 'badgers', 'ants']

# you can not sort lists that have stringers and integers
spam = [1, 2, 3, 'Alice', 'Bob']
spam.sort() # TypeError

# ASCII-betical Order
spam = ['Alice', 'ants',  'Bob', 'badgers']
spam.sort()
spam # ['Alice', 'Bob', 'ants', 'badgers']
# All the upper-case letters come first. We need to fix this
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam # ['A', 'a', 'Z', 'z']
