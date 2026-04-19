# Activity-1:

p = float(input("Enter Principal Amount : "))
r = float(input("Enter Rate of interest : "))
t = float(input("Enter Time period : "))

SI = (p*r*t)/100
CI = (p*((1+r/100))**t)-p

print(f"Simple Interest = {SI}")
print(f"Compound Interest = {CI}")

# Output:
# Enter Principal Amount : 1000
# Enter Rate of interest : 5
# Enter Time period : 2
# Simple Interest = 100.0
# Compound Interest = 102.5


