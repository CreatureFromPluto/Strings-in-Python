# Question 3

b = 'aFoxjumpsovertheWallTosaveanant'
count = 0
def article(b):
    articles = ['a','an','the']
    print([letter for letter in b if letter in articles])
article('aFoxjumpsovertheWallTosaveanant')
count = count+1