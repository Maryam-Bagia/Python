n = 6

for i in range(1,n):
    if i%2 == 0:
        val = 0
    else: 
        val = 1

    for j in range(1,i+1):
        print(val,end=" ")
        val = 1-val
    print()