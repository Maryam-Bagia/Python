# Program to count digits in a number

# Step 1: Take input from user
num = int(input("Enter a number: "))

# Step 2: If the number is 0, it has only 1 digit
if num == 0:
    count = 1
else:
    count = 0  # Initialize count

    # Step 3: Use a loop to divide the number by 10 until it becomes 0
    while num > 0:
        num = num // 10   # Remove the last digit
        count += 1        # Increase digit count

# Step 4: Print result
print("The number of digits is:", count)

