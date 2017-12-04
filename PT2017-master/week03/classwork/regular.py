# ^ . * $ * + ? { } [] \ | ()


# Regular expressions
# ^ - start line
# $ - end line
"^[abc]$"
"^[a-p]$"
"^[0-3]$"

# [set] any character from set
# . any character

# 30-08-1990

# [0-9] = \d
# [^0-9] = [все не цифры] = \D
# [a-zA-Z0-9_] = [альфанумерик] =\w 
# '\s' - whitespace пробел табуляция

p = re.compile("^\d\d\.\d\d\.\d\d\d\d$")


# yesdauren@gmail.com

# + one or more
# ? one or none
# {n} n times
# dd.mm.yyyy
# mm.dd.yyyy
# (x | y) x or y
p = re.compile("^\w+\.?\w+@gmail\.com$")
p = re.compile("^\w+\.?\w+@(gmail\.com|mail\.ru)$")

# +7 (701) 520 9278
p = re.compile("^(7|\+7|8|)( |-)?\(?(700|701|702|705|707|708|747|771|775|778|777)\)?( |-)?\d\d\d( |-)?\d\d( |-)?\d\d$")



import re
p = re.compile('[abc]')
p = re.compile('[a-c]')
p = re.compile('\d') # [0-9] digit
p = re.compile('\D') # [^0-9] non-digit
p = re.compile('\s') # whitespace [ \t\n\r]
p = re.compile('\S') # non whitespace [^ \t\n\r]
p = re.compile('[a-zA-Z]')
p = re.compile('\w') = re.compile('[a-zA-Z0-9') #alphanumric  
p = re.compile('\W') # non-alphanumeric

p = re.compile('.') # any character

p = re.compile('\d\d')
p = re.compile('^\d\d$')
# ^ string begin
# $ string end
# 30/08/1990

p = re.compile('^\d\d/\d\d/\d\d\d\d$')
# + one or more
# ? one or none
p = re.compile('^\w+@gmail\.com$')

p = re.compile('^(\+7|8)-?(\((701|702)\)|(701|702))-?\d\d\d( |-)\d\d-?\d\d$')
