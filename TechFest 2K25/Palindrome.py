num = int(input("Enter a number :"))

sum = 0
while num>0:
    remainder = num % 10
    sum = (sum*10) + remainder
    num = num//10

if num == sum:
    print("It's a Palindrome.")
else:
    print("It's not a Palindrome.")


# For string

str = input("Enter a string :")

if((str[::-1]) == str):
    print("It's a palindrome.")