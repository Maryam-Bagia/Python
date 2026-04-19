# Activity-6:

weight = float(input("Enter your weight in kg. : "))
height = float(input("Ente your height in meters : "))

BMI = weight/(height**2)

print(f"Your Body Mass Index (BMI) is {BMI:.2f} .")

if(BMI < 19):
    print("You are underweight.")
elif(19 < BMI < 25):
    print("You are normal weight.")
elif(BMI > 25):
    print("You are overweight.")

# Output:
# Enter your weight in kg. : 70
# Enter your height in meters : 1.75
# Your Body Mass Index (BMI) is 22.86.
# You are normal weight.

