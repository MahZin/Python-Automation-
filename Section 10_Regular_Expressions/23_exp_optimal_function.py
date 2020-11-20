# the real regular expressions

import re

message = 'Call me 234-423-2311 tomorrow, or at 323-354-7654 for my office number.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # create regex object
mo = phoneNumRegex.search(message) # to return a match object
print(mo.group()) # to get matched string

# can use findall method instead
print(phoneNumRegex.findall(message)) # mo = match objects


