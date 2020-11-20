# 27: More Regex

import re
beginsWithHelloRegex = re.compile(r'^Hello')
beginsWithHelloRegex.search('Hello there!')
# <re.Match object; span=(0, 5), match='Hello'>
beginsWithHelloRegex.search('He said "Hello!"') == None
# True
endsWithWorldRegex = re.compile(r'world!$')
endsWithWorldRegex.search('Hello world!')
# <re.Match object; span=(6, 12), match='world!'>
endsWithWorldRegex.search('Hello world! sakjdksajdksjds')

#
allDigitsRegex = re.compile(r'^\d+$') # begin and end with \d+
allDigitsRegex.search('25874328597234587')				
# <re.Match object; span=(0, 17), match='25874328597234587'>
allDigitsRegex.search('2587432x597234587') # doesnt fit, has a non-digit

# . : means any character except newline
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# ['cat', 'hat', 'sat', 'lat', 'mat'] # notice how lat is matched, not flat
atRegex = re.compile(r'.{1,2}at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# [' cat', ' hat', ' sat', 'flat', ' mat'] # now u can see flat

# .* : any character + 0 or more = anything; any pattern
# a bad example of what to do
'First Name: Al Last Name: Sweigart'
'First Name: Al Last Name: Sweigart'
'First Name: Al Last Name: Sweigart'.find(':')
# 10
'First Name: Al Last Name: Sweigart'.find(':') + 2
# 12
'First Name: Al Last Name: Sweigart'[12:]
# 'Al Last Name: Sweigart'

# better way:
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameRegex.findall('First Name: Al Last Name: Sweigart')
# [('Al', 'Sweigart')] # returns list of tuples

# to use .* in a non-greedy match: .*?
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
nongreedy.findall(serve)
# ['To serve humans']
# to use greedy match
greedy = re.compile(r'<(.*)>')
greedy.findall(serve)
# ['To serve humans> for dinner.']

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)
# Serve the public trust.
# Protect the innocent.
# Upload the law.
dotStar = re.compile(r'.*')
dotStar.search(prime)
# <re.Match object; span=(0, 23), match='Serve the public trust.'>
# it stops at a newline, here's how to match everything:
dotStar = re.compile(r'.*', re.DOTALL)
dotStar.search(prime)
# <re.Match object; span=(0, 61), match='Serve the public trust.\nProtect the innocent.\nU>

vowelRegex = re.compile(r'[aeiou]')
vowelRegex.findall('Al, why does your programming book talk about Robocop so much?')
# ['o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u']
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE) # or re.I
vowelRegex.findall('Al, why does your programming book talk about Robocop so much?')
# ['A', 'o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u']
# to match uppercase as well
