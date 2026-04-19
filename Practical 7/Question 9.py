# Activity-9:

reverse=0
n=int(input("enter a number:"))

while n>0:
    digit=n%10
    reverse= reverse*10+digit
    n//=10

print("reversed number:",reverse)

# Output:
# enter a number:12345
# reversed number: 54321



