s = input().replace(" ", "")
while True:
	ok = True
	if "()" not in s:
		ok = False
	else:
		i = s.index("()")
		s = s[:i] + s[i + 2:]
		ok =True
	if "{}" not in s:
		ok = False
	else:
		i = s.index("{}")
		s = s[:i] + s[i + 2:]
		ok =True
	if "[]" not in s:
		ok = False
	else:
		i = s.index("[]")
		s = s[:i] + s[i + 2:]
		ok =True
	if not ok:
		break
if len(s) == 0:
	print("yes")
else:
	print("no")

