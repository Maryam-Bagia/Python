# Activity - 1

import math

# Square root
num = float(input("Enter a number to find its square root: "))
square_root = math.sqrt(num)
print(f"Square root of {num} is {square_root}")

# Power
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))
power = math.pow(base, exponent)
print(f"{base} raised to the power of {exponent} is {power}")

# Logarithm
log_num = float(input("Enter a number to find its logarithm (base 10): "))
log_value = math.log10(log_num)
print(f"Logarithm (base 10) of {log_num} is {log_value}")

# Output:
# Enter a number to find its square root: 16
# Square root of 16 is 4.0
# Enter the base number: 2
# Enter the exponent: 3
# 2 raised to the power of 3 is 8.0
# Enter a number to find its logarithm (base 10): 100
# Logarithm (base 10) of 100 is 2.0



