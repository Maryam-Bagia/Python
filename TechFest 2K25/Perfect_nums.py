perfects = []

for num in range(1,1000,1):
    sum = 0 
    for i in range(1,num,1):
        div = []
        if num % i == 0:
            div.append(i)
            for n in div:
                sum = sum + n
                if sum == num:
                    perfects.append(num)


print(perfects)