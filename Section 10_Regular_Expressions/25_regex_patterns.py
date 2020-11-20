# matching a specific number of repetitions
import re

# ? means can appear 0 or 1 times
batRegex = re.compile(r'Bat(wo)?man') 
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
# 'Batman'
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
# 'Batwoman'
mo = batRegex.search('The Adventures of Batwowowowowoman')
mo == None
# True
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())
# 415-555-1234
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
mo == None
# True
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
# <_sre.SRE_Match object; span=(19,31), match='415-555-1234'>
phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
# <_sre.SRE_Match object; span=(19, 27), match='555-1234'>

# if you want regex obj for "dinner?", call: re.compile(r'dinner\?')
# it's like using ''' for quotes with ' and ''

# * : appears 0 or more times
batRegex = re.compile(r'Bat(wo)*man') 
batRegex.search('The Adventures of Batman')
# <_sre.SRE_Match object; span=(18, 24), match='Batman'>
batRegex.search('The Adventures of Batwoman')
# <_sre.SRE_Match object; span=(18, 26), match='Batwoman'>
batRegex.search('The Adventures of Batwowowowowowoman')
# <_sre.SRE_Match object; span=(18, 38), match='Batwowowowowowoman'>

# + : appears at least once or returns nothing
batRegex = re.compile(r'Bat(wo)+man')
batRegex.search('The Adventures of Batman') == None
# True
batRegex.search('The Adventures of Batwoman')
# <_sre.SRE_Match object; span=(18, 26), match='Batwoman'>
batRegex.search('The Adventures of Batwowowowowowoman')
# <_sre.SRE_Match object; span=(18, 38), match='Batwowowowowowoman'>

# if there is a + in your pattern, use \+

# escaping +, ?, and *
regex = re.compile(r'\+\*\?')
regex.search('I learned about +*? regex syntax')
# <_sre.SRE_Match object; span=(16, 19), match='+*?'>
regex = re.compile(r'(\+\*\?)+')
regex.search('I learned about +*?+*?+*?+*?+*? regex syntax')
# <_sre.SRE_Match object; span=(16, 19), match='+*?+*?+*?+*?+*?'>

# finding an exact # of a pattern. use {}
haRegex = re.compile(r'(Ha){3}') # same as haRegex = re.compile(r'HaHaHa')
haRegex.search('He said "HaHaHa"')
# <sre.SRE_Match object; span(9, 15), match='HaHaHa'>
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-000'>)
# <sre.SRE_Match object; span(15, 49), match=415-555-1234,555-4242,212-555-000'>
    
# finding 'at least x, at most y' {x,y}
haRegex = re.compile(r'(Ha){3,5}')
haRegex.search('He said "HaHaHa"')
# <sre.SRE_Match object; span(9, 15), match='HaHaHa'>
haRegex.search('He said "HaHaHaHaHa"')
# <sre.SRE_Match object; span(9, 19), match='HaHaHaHaHa'>
haRegex.search('He said "HaHaHaHaHaHaHa"')
# <sre.SRE_Match object; span(9, 19), match='HaHaHaHaHa'>
# any more 'Ha's will only match the first 5 'Ha's
haRegex = re.compile(r'(Ha){3,)') # at least 3
haRegex = re.compile(r'(Ha){,5)') # 0 to 5
                    

digitRegex = re.compile(r'(\d){3,5}')
digitRegex.search('1234567890')
# <sre.SRE_Match object; span(0, 5), match='12345'> # greedy match (longest possible string)
digitRegex = re.compile(r'(\d){3,5}?') # ? 
digitRegex.search('1234567890')
# <sre.SRE_Match object; span(0, 3), match='123'> # non-greedy match (shortest possible string)

