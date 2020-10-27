stringA = 'technical'
stringB = 'nicaltech'
def isRotated(stringA,stringB):
    size1 = len(stringA)
    size2 = len(stringB)
    temp = ''
    if size1 != size2:
        return 0
    temp = stringA + stringA
    if (temp.count(stringB)> 0):
        return 1
    else:
        return 0
if isRotated(stringA,stringB):
    print('YES')
else:
    print('NO')
