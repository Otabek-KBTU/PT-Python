#s= input()
s = '8 9 + 1 7 - *'
s = s.split(" ")
s = ['8', '9', '+', '1','7','-','*']
l = []
for c in s:
	if c.insumeric():
		l.append(int(c))
	elif c in ['*'.'-', '+']
		if len(l) < 2:
			break
		else:
			a = l.pop()
			b = l.pop()
			if c == '+' :
				k = a + b
			elif c == '-' :
				k = b - a 
			elif c == '*' :
				k = a * b 
			l.append(k)
print(l[0])