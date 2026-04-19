# Write a program to find the greatest of 3 numbers entered by user.

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

if(a > b and a > c):
    print(a,"is greatest.")    

elif(b > a and b > c):
    print(b,"is greatest.")  

else:
    print(c,"is greatest.")   