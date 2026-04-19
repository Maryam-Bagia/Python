# Activity - 1

paragraph = input("Enter a paragraph: ")

with open("paragraph.txt", "w") as file:
    file.write(paragraph)

with open("paragraph.txt", "r") as file:
    content = file.read()

print("Content of the file:")
print(content)


