height=float(input("Enter your height in cm"))
weight=float(input("Enter your weight in kg"))
bmi=weight/(height/100)**2
print("You'r BMI is",bmi)
if bmi<=18.4:
    print("you are Under Weight")
elif bmi<=24.9:
    print("you are Healthy")
elif bmi<=29.9:
    print("you are Over Weight")
elif bmi<=34.9:
    print("you are Severely Over Weight")
elif bmi<=39.9:
    print("you are Obese")
else:
    print("you are Severely Obese")