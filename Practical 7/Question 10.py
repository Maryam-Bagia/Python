# Activity-10:

#pattern-1                                # Output:
for i in range(1,6):                      # *
    for j in range(1,i+1):                # * *            
        print("*",end=" ")                # * * *
    print()                               # * * * *
                                          # * * * * *


#pattern-2                                # Output:
for i in range(1,6):                      # 1
    for j in range(1,i+1):                # 1 2
        print(j,end=" ")                  # 1 2 3
    print()                               # 1 2 3 4
                                          # 1 2 3 4 5


#pattern-3                                # Output:
for i in range(1,6):                      # A
    j=65                                  # A B
    for j in range(j,j+i):                # A B C
        print(chr(j),end=" ")             # A B C D
    print()                               # A B C D E



#pattern-4                                # Output:
for i in range(5,0,-1):                   # * * * * *
    for j in range(1,i+1):                # * * * *
        print("*",end=" ")                # * * *
    print()                               # * *
                                          # *


#pattern-5                                # Output:
for i in range(5,0,-1):                   # 1 2 3 4 5
    for j in range(1,i+1):                # 1 2 3 4
        print(j,end=" ")                  # 1 2 3 
    print()                               # 1 2
                                          # 1


#pattern-6                                # Output:
for i in range(5,0,-1):                   # A B C D E
    j=65                                  # A B C D
    for j in range(j,j+i):                # A B C
        print(chr(j),end=" ")             # A B
    print()                               # A






    