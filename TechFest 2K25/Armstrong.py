# Armstrong Number Program in Python

# Step 1: Ask the user to enter a number
num = int(input("Enter a number: "))

# Step 2: Convert number to string to easily count digits
num_str = str(num)

# Step 3: Find the number of digits
n = len(num_str)

# Step 4: Initialize sum to 0
sum_of_powers = 0

# Step 5: Loop through each digit in the number
for digit in num_str:
    # Convert digit back to integer
    d = int(digit)
    
    # Raise the digit to the power of n (number of digits)
    power = d ** n
    
    # Add this power to the sum
    sum_of_powers += power

# Step 6: Compare the sum with the original number
if sum_of_powers == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")
