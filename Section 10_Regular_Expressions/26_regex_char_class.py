import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex
re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
resume = '''number is 714-555-1234, and other is 123-456-7890'''
phoneRegex.search(resume)
# <re.Match object; span=(10, 22), match='714-555-1234'>
phoneRegex.findall(resume)
# ['714-555-1234', '123-456-7890']
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneRegex.finadall(resume)
# [('714', '555-1234'), ('123', '456-7890')]
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
phoneRegex.findall(resume)
# [('714-555-1234', '714', '555-1234'), ('123-456-7890', '123', '456-7890')]

digitRegex = re.compile(r'\d')
# \d any numeric digit 0-9
# \D any char that is NOT \d
# \w any letter, numeric digit, or underscore char
# \W any char that is NOT \w
# \s any space, tab, or newline char
# \S any char NOT \s

lyrics = '''12 drummers drumming, 11 pipers piping, 10 lords a leaping,
9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying,
5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and
1 partridge in a pear tree
'''
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall(lyrics)
# ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids',
#  '7 swans', '6 geese', '5 golden', '4 calling', '3 french', '2 turtle',
#  '1 partridge']

# other char classes
regexObj = re.compile(r'[]')
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('Robocop eats baby food')
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
doubleVowelRegex.findall('Robocop eats baby food')
# ['ea', 'oo']

# negative char classes
consonantsRegex =re.compile(r'[^aeiouAEIOU]')
consonantsRegex.findall('Robocop eats baby food')
# ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd']
