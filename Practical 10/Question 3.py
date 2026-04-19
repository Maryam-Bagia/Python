# Activity - 3

my_tuple = (1, 2, 3, 4, 5)

element = int(input("Enter an element to check: "))

if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

if element not in my_tuple:
    print(f"{element} does not exist in the tuple.")
else:
    print(f"{element} exists in the tuple.")


# Output:
# Enter an element to check: 3
# 3 exists in the tuple.


