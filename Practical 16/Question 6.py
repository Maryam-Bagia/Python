# Activity - 6

from collections import Counter

with open("paragraph.txt", "r") as file:
    content = file.read()

content = content.replace(" ", "").lower()

alphabet_count = Counter(content)

for alphabet, count in alphabet_count.items():
    if alphabet.isalpha():
        print(f"{alphabet}:{count}")


        