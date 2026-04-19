# continue statement orders loop to not to terminate but, skip that iteration and continue the loop from starting statement.

num = 1
while(num <= 10):
    if(num == 6):
        num = num + 1
        continue
    print(num)
    num = num + 1    