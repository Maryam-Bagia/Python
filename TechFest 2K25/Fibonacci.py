n = int(input("Enter number of terms :"))

t1 = 0
t2 = 1
count = 0

print("Fibonacci series :")
while(count < n):
    print(t1,end=" ")

    nextTerm = t1 + t2
    t1 = t2
    t2 = nextTerm

    count += 1



