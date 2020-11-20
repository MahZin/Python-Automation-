# more string syntax
'That is Alice's cat'
# problem is that the apostrophe is shared
# so we can use quotation marks
"That is Alice's cat."
# can also use an escape character \' for single quotes
# \" double quote
# \t tab
# \n newline (line break)
# \\ backslash
'Say hi to Bob\'s mother.'

# to separate lines in a string:
print('Hello there!\nHow are you?\nI\'m fine.')
# Hello there!
# How are you?
# I'm fine.

# can use raw strings
# raw strings literally print any backslashes
# raw strings ignore escape characters
r'Hello'
# 'Hello'

r'That is Carol\'s cat.'
# "That is Carol\\'s cat."
# ^ this is a regular, non-raw string value

print(r'That is Carol\'s cat.')
# That is Carol\'s cat.

# To utilize multiline strings, consider triple quotes:
print("""Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary,
and extortion.
Sincerely,
Bob.""")
# separating by newlines don't matter for triple quotes

# List commands can be used for strings
# indexes, slices, in and not in operators
spam = 'Hello world!'
spam[0]
# 'H'
spam[1:5]
# 'ello'
spam[-1]
# '!'

'Hello' in spam
# True
'x' in spam
# False
