# Program to convert Binary to Decimal

# Step 1: Take binary number input from user
binary_str = input("Enter a binary number: ")

# Step 2: Initialize decimal value to 0
decimal_value = 0

# Step 3: Find length of binary number
length = len(binary_str)

# Step 4: Loop through each digit in the binary string
for i in range(length):
    # Get each digit (0 or 1)
    digit = int(binary_str[i])
    
    # Find the position power (from right to left)
    power = length - i - 1
    
    # Convert to decimal contribution (digit * 2^power)
    decimal_value += digit * (2 ** power)

# Step 5: Print the result
print("The decimal value of", binary_str, "is:", decimal_value)

