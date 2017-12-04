sentence = 'Kbtu is the best university, but alwasy sunny in Almaty! Hello, my name is Dauren'

words = sentence.replace(",", " ").replace(".", " ").replace("!", " ").split()

new_words = []
for word in words:
	new_word  = ""
	i = 0
	for letter in word:
		if i % 2 == 0:
			new_word = new_word + letter.upper()
		else:
			new_word = new_word + letter.lower()
		i = i + 1
	new_words.append(new_word)
sentence = " ".join(new_words)
print(sentence)


