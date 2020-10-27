# Question 4

word = str(input('Enter the string:' ))
maketrans = word.maketrans
word = word.maketrans(maketrans('aeiuoAEIUO','**********'))
print(word)