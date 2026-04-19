# Activity-3:

number = input("Enter a number: ")

digit_sum = 0

i = 0
while i < len(number):
    digit_sum += int(number[i])
    i += 1

print("The sum of the digits is:", digit_sum)

# Output:
# Enter a number: 12345
# The sum of the digits is: 15


