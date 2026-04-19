# Program to convert Decimal to Binary

# Step 1: Take decimal number input from user
decimal_num = int(input("Enter a decimal number: "))

# Step 2: Initialize an empty string to store binary digits
binary_str = ""

# Step 3: If number is 0, directly return "0"
if decimal_num == 0:
    binary_str = "0"
else:
    # Step 4: Keep dividing the number by 2 until it becomes 0
    while decimal_num > 0:
        # Find remainder (0 or 1)
        remainder = decimal_num % 2
        
        # Add remainder in front of the binary string
        binary_str = str(remainder) + binary_str
        
        # Update decimal number by dividing by 2 (integer division)
        decimal_num = decimal_num // 2

# Step 5: Print the binary result
print("Binary value is:", binary_str)
