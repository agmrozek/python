>>> import re

# using [A-Z0-9] instead of \w because that would also match an underscore (_)
>>> pat = re.compile(r'^PB(-[A-Z0-9]{8}){4}$')

>>> pat.match('PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4')
<re.Match object; span=(0, 38), match='PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4'>

# ^$ = end-to-end match, so adding an extra space, no match
>>> pat.match('PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4 ')

# replacing a character with an underscore, no match
>>> pat.match('PB-U_N435EH-PG65PW87-IXPWQG5T-898XSZI4 ')

# leaving the leading PB- off, no match
>>> pat.match('U8N435EH-PG65PW87-IXPWQG5T-898XSZI4')