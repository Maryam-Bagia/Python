# WAP to print only all odd numbers from 1 to 100 using loop and continue statement.

num = 1

while(num <= 100):
    if(num % 2 == 0):
        num = num + 1
        continue
    print(num)
    num = num + 1