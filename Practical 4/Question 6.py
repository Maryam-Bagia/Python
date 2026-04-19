# Activity-6:

cpf = int(input("Enter your CPF marks : "))
maths = int(input("Enter your Maths marks : "))
cse = int(input("Enter your CSE marks : "))
be = int(input("Enter your BE marks : "))
mp = int(input("Enter your MP marks : "))

sub_total = cpf + maths + cse + be + mp
total = 150
percentage = (sub_total/total)*100

print(f"Your percentage = {percentage:.2f}%")

# Output:
# Enter your CPF marks : 29
# Enter your Maths marks : 28
# Enter your CSE marks : 27
# Enter your BE marks : 29
# Enter your MP marks : 29
# Your percentage = 96.67%



