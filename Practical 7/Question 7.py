# Activity-7:

fact=0
n=int(input("enter a number:"))

for i in range(1,n+1):
    if n%i==0:
        fact+=1

if fact==2:
    print("%d is prime number"%(n))
else:
    print("%d is not prime number"%(n))

# Output:
# enter a number:47
# 47 is prime number


