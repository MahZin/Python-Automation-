# string methods
spam = 'Hello world!'
spam.upper()
# 'HELLO WORLD!'

# but when you call spam, it returns the original
spam
# 'Hello world!'

# so, we assign spam to a new spam variable
spam = spam.upper()
spam
# 'HELLO WORLD!'

spam.lower()
# 'hello world'

# problem: what if functions to inputs are case-sensitive
answer = input()
# yes
# or:
# YES

if answer == 'yes':
    print('Playing again')
# but the problem is that it is case-sensitive
answer == 'yes'
# False
answer.lower() == 'yes'
# True

if answer.lower() == 'yes':
    print('Playing again')
# Playing again

# isupper and islower return a boolean value
spam = 'Hello world!'
spam.islower()
# False

spam = 'hello world!'
spam.islower()
# True

spam = 'HELLO WORLD!'
spam.isupper()
# True

spam = ''
spam.isupper()
# False
spam.islower()
# False
# need a value to possibly return True

'12345'.islower()
# False

'Hello'.upper().isupper()
# string > string method > another string method
# True

# other 'is' methods

# isalpha() - letters only
'hello'.isalpha()
# True
'hello123'.isalpha()
# False

# isalnum() - letters and numbers only
'hello123'.isalnum()
# True

# isdecimal() - numbers only
'123'.isdecimal()
# True

# isspace() - whitespace only
'    '.isspace()
# True
'Hello world!'.isspace()
# False
'Hello world!'[5].isspace()
# True

# istitle() - titlecase only
'This Is Title Case.'.istitle()
# True

# startwith and endwith methods
'Hello world!'.startswith('H')
# True
'Hello world!'.endswith('!')
# True

# JOIN METHOD
','.join(['cats', 'rats', 'bats'])
# 'cats,rats,bats'
'\n\n'.join(['cats', 'rats', 'bats'])
# 'cats\n\nrats\n\nbats'
print('\n\n'.join(['cats', 'rats', 'bats']))
# cats

# rats

# bats

# SPLIT METHOD
'My name is Simon'.split()
# ['My, 'name', 'is', 'Simon']
'My name is Simon'.split('m')
# ['My na', 'e is Si', 'on']

# ADJUSTING STRINGS
'Hello'.rjust(10)
#'     Hello'
len('     Hello')
# 10

'Hello'.ljust(10)
# 'Hello     '

# can create a new string
'Hello'.rjust(20, '*')
# '***************Hello'
'Hello'.ljust(10, '-')
# 'Hello-----'

'Hello'.center(15)
# '     Hello     '
'Hello'.center(15, '=')
# '=====Hello====='

spam = '     Hello'
spam = spam.strip()
spam
# 'Hello'
'     x     '.strip()
# 'x'
'     x     '.lstrip()
# 'x    '
'     x     '.rstrip()
# '    x'

# REPLACE METHOD
spam = 'Hello'
spam.replace('e', '1')
# 'H1llo'
