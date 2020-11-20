# List and string similarities
name = 'Zophie'
name[0] # 'Z'
name[1:3] # 'op'
name[-2] # 'i'
'Zo' in name # True
'xxx' in name # False
for letter in name:
    print(letter)
# Z
# o
# p
# h
# i
# e

name = 'Zophie the cat'
name[7] # 't'
name[7] = 'X' # TypeError

# Creating new string with slices
name = 'Zophie a cat' 
newName = name[0:7] + 'the' + name[8:12]
newName # 'Zophie the cat'

# list referencing
# in the case of strings...
spam = 42
cheese = spam
spam = 100
spam # 100
cheese # 42
# but this does not work for lists
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello'
cheese # [0, 'Hello', 2, 3, 4, 5]
spam # [0, 'Hello', 2, 3, 4, 5]
# how come cheese and spam are both modified?
# it is because both variables are referencing the same list
# variables contain references to lists, NOT the actual list

# How can you copy a list so you can change the copy?
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
cheese # ['A', 42, 'C', 'D']
spam # ['A', 'B', 'C', 'D']
# here, spam (the main copy) is unchanged

# indentations
spam = ['apples',
        'oranges',
        'bananas',
        'cats']
# slash \ indentation for continuation
print('Four score and seven' + \
      'years ago')
# Four score and sevenyears ago
print('Four score and seven' + 'years ago')
# Four score and sevenyears ago
