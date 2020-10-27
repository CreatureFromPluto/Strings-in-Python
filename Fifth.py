# Question 5

data = 'Bear Cubs are CUTE.'
def swap_case(data):
    result_data = ''
    for item in data:
        if item.isupper():
            result_data += item.lower()
        else:
            result_data += item.upper()
    return result_data
print(swap_case('Bear Cubs are CUTE.'))