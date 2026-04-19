num = int(input("Enter a number :"))

a = 0

if(num == 0 or num == 1):
    print(f"{num} is not a Prime number.")
else:
    for i in range(2,num,1):
        if(num % i == 0):
            a=1
            break

if a == 0:
    print(f"{num} is Prime number.")
else:
    print(f"{num} is not a Prime number.")