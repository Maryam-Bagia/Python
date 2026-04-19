# Activity - 5

with open("source.txt", "r") as source_file:
    content = source_file.read()

with open("destination.txt", "w") as destination_file:
    destination_file.write(content)


    