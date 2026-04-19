# Activity - 2

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels:",count)

# Output:
# Enter a string: Hello World
# Number of vowels: 3


