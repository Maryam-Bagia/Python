# Activity - 2

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(num, "is", check_even_odd(num))

# Output:
# Enter a number: 5
# 5 is Odd


