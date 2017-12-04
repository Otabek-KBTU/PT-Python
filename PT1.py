import re


p  = re.compile('^\w+\.?\w+@(gmail\.com)|mail\.ru$')
print(p.match('')) 

p = re.compile('^(+77|87)( |-)?(71|72)\)?( |-)?\d\d\d( |-)?\d\d( |-)?\0\d$')p
print(p.match('')) 
p = re.compile('^\d\d/\d\d/\d\d\d\d$')
print(p.match('')) 
p = re.compile('^\d\d/\d\d/\d\d/\d\d\d\d$')
print(p.match(''))





p = re.compile('^( 	51|55)( |)?\dd\d\d( |-)?\d\d( |-)?\0\d$')p