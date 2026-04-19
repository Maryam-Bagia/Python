# Activity - 3

import math

def compute_mean(numbers):
    return sum(numbers) / len(numbers)

def compute_standard_deviation(numbers, mean):
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

mean = compute_mean(numbers)
std_dev = compute_standard_deviation(numbers, mean)

print("Mean:", mean)
print("Standard Deviation:",std_dev)

# Output:
# Enter numbers separated by space: 1 2 3 4 5
# Mean: 3.0
# Standard Deviation: 1.4142135623730951


