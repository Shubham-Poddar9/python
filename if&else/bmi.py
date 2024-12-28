height=float(input("Enter your height in cm"))
weight=float(input("Enter your weight in kg"))
bmi=weight/(height/100)**2
print(bmi)
if bmi<=18.4:
  print("YOU ARE UNDER WEIGHT")
elif bmi<=24.9:
  print("YOU ARE HEALTHY")
elif bmi<=29.9:
  print("YOU ARE OVER WEIGHT")
elif bmi<=34.9:
  print("YOU ARE SEVERELY OVER WEIGHT")
elif bmi<=39.9:
  print("YOU ARE OBESE")
else:
  print("YOU ARE SEVERELY OBESE")