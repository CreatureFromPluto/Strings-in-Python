
inputStr = str(input("Enter a sentence:"))
inputStr = inputStr.lower()
vowels = ['a','e','i','o','u']
for i in inputStr:
    if i in vowels:
        print("Replacing")
        inputStr = inputStr.replace(i,'*')    

print("Result:",inputStr)
