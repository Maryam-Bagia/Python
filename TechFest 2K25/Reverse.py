num = int(input("Enter a number :"))

sum = 0
while num>0:
    remainder = num % 10
    sum = (sum*10) + remainder
    num = num//10

reversed = sum
print(f"Reversed = {reversed}")