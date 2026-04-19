# Write a program to check if a list contains a palindrome of elements or not.

list = []

list.append(input("Enter first element :"))
list.append(input("Enter second element :"))
list.append(input("Enter third element :"))
list.append(input("Enter fourth element :"))
list.append(input("Enter fifth element :"))

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("This list is palindrome.")
else:
    print("This list is not a palindrome.")    


