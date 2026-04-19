# Activity - 2
# main.py

import custommodule

string = input("Enter a string: ")

reversed_string = custommodule.reverse_string(string)
capitalized_string = custommodule.capitalize_string(string)
length_of_string = custommodule.string_length(string)

print("Reversed string:", reversed_string)
print("Capitalized string:", capitalized_string)
print("Length of string:", length_of_string)

# Output:
# Enter a string: hello world
# Reversed string: dlrow olleh
# Capitalized string: Hello world
# Length of string: 11


