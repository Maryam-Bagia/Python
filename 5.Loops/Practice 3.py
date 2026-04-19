# Print the multiplication table of number n.

n = int(input("Enter a number to print it's table : "))
i = 1

while(i<=10):
    print(n,"*",i,"=",n*i)
    i = i + 1