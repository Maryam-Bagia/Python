# Activity - 3

with open("paragraph.txt", "r") as file:
    content = file.read()

word_count = len(content.split())

print("Number of words in the file:",word_count)


