
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.search('My number is 415-555-4242')
# <re.Match object; span=(13, 25), match='415-555-4242'>
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group())
# '415-555-4242'

# to compile into groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group())
# '415-555-4242'
print(mo.group(1))
# '415'
print(mo.group(2))
# '555-4242'

# what if a # has ()
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is (415) 555-4242')
print(mo.group())
# (415) 555-4242

# if u want to find all prefixes
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
# Batmobile
mo = batRegex.search('Batmotorcycle lost a wheel')
print(mo == None)
# True


mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(1))
