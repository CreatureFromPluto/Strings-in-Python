# Question 2

word = str(input('Enter the string:' ))


def shortest_word(word_list):
    shortest_word = ''
    size = 1
    for word in word_list:
        if len(word) <= size:
            shortest_word = word
            size = len(word)
    return shortest_word


word_list = word.split()
output = shortest_word(word_list)
print(output)