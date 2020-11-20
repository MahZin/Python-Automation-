# Regex sub() method and Verbose Mode

import re
namesRegex = re.compile(r'Agent \w+')
namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
# ['Agent Alice', 'Agent Bob']

# how to find and replace
namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'REDACTED gave the secret documents to REDACTED.'

# What if, instead of REDACTED, we use 'Agent A', etc.
namesRegex = re.compile(r'Agent (\w)\w*') # 1 or more word char(s) followed by 0 or more other letter char(s)
namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
# ['A', 'B']
namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')
# 'Agent A**** gave the secret documents to Agent B****.'
# using \1, \2, etc. will substitute group 1, 2, etc. in the regex pattern

# Verbose mode
# easier way than: re.compile(r'\(\d\d\d\)(-)?\d\d\d-\d\d\d\d')
# ignores newline, whitespace; allows whitespace and comments in regex string 
re.compile(r'''
(\d\d\d-)| # area code w/o parens, w/dash
(\(\d\d\d\) )  # -or- area code with parens + no dash
\d\d\d    # first 3 digits
-         # second dash
\d\d\d\d  # last 4 digits
\sx\d{2,4}  # extension, i.e x1234''', re.VERBOSE) # can add re.IGNORECASE | re.DOTALL
