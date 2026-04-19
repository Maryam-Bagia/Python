Marks = int(input("Enter your marks(out of 100) :"))

if(Marks >= 90):
    print("A grade")
elif(Marks >= 80):
    print("B grade")   
elif(Marks >= 70):
    print("C grade")
elif(Marks < 70):
    print("D grade")
else:
    print("You are fail.Better luck next time.")