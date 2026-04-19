# Activity-5:

bill = float(input("Enter the purchase amount: "))

if(bill >= 5000):
    discount = bill * 0.20
elif(bill >= 3000):
    discount = bill * 0.10
else:
    discount = bill * 0.05
    
final_amount = bill - discount

print(f"Discount: {discount}")
print(f"Final amount to be paid: {final_amount}")

# Output:
# Enter the purchase amount: 6000
# Discount: 1200.0
# Final amount to be paid: 4800.0

