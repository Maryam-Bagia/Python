# Activity - 2

text_to_append = input("Enter text to append to the file: ")

with open("paragraph.txt", "a") as file:
    file.write("\n" + text_to_append)

with open("paragraph.txt", "r") as file:
    content = file.read()

print("Updated content of the file:")
print(content)


