import io

words = []
# rb - read binary
# wb - write binary
with open('word_rus.txt', 'rb') as file:
	lines = file.readlines()
	for line in lines:
		w = line.decode('utf-8').replace('\n', '').replace('\r', '')
		words.append(w)


anagrams = []
voc = []

for i in range(0, 35):
	voc.append([])

for w in words:
	x = len(w)
	voc[x].append(w)

for j in range(0, 35):
	lwords = voc[j]
	i = 0
	for w1 in lwords:
		for w2 in lwords[i + 1:]:
			if w1 != w2:
				s1 = "".join(sorted(w1))
				s2 = "".join(sorted(w2))
				if s1 == s2:
					anagrams.append([w1, w2])
		i = i + 1


with open("anagrams.txt", "wb") as file:
	for item in anagrams:
		x = ("%s %s\n" % (item[0], item[1])).encode('utf-8')
		file.write(x)
