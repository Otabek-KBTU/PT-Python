s = input() 
l = s.split(' ')
print(l)
a = l[0]
b = l[1]
c = l[2]
ll = []
for x in l:
	ll.append(int(x))
print(ll)
ll = [int(x) for x in l]
# print(ll)
l2 = [x * 2  for x in ll]
# print(l2)