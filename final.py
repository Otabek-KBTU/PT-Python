s = "Kbtu"
n = len(s) # s.size()
print(s[0]) # >>> K
print(s[-1]) # >>> u
print(s[:2]) # >>> Kb
print(s[-2:]) # >> tu
#s[1] = 'u'
# String is ummutable 
s = s.replace('b', 'u')

s = 'Hello world'
for symbol in s:
	print(ord(symbol)) #ord ascii code
s = 'KBTU, SDU, IITU, KIMEP'
l = s.split(",") # delimiter
ll = []
for item in l:
	ll.append(item.replace(' ', ''))  # remove odd spaces
lll = "\t".join(ll)
print(lll)
reversed_s = s[::-1]
s = 'Hello world'
if s.startswith("Hello"):
	print("yes")
if s.endswith("old"):
	print("Yes")

s = s + "!" # конкатенация CONCAT
s = "  \t a string example\t  "
s = s.strip()
s = s.rstrip()
s = s.lstrip()

name = "Timur"
surname = "Umarov"
age = 48
salary = 100009989.09

s = "Timus Umarov is 48 years old"
s = name + " " + surname + "is " + str(age)+" years old"
s = "%s %s is %d years old with %f"
s = s % (name, surname, age, salary)

s = "{0}-{2} {1} is {2}".format(name, surname, age)

s.upper()
s.lower()	

s = 'Hello World'
s = 'HeLlO WoRlD'