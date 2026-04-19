str = input("Enter a string :")

str = list(str)

vowels = 0
consonants = 0

for i in str:
    if i in('a','e','i','o','u'):
        vowels += 1
    else:
        consonants += 1
    
print("v =", vowels)
print("c=" ,consonants)