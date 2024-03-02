height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / height ** 2
print("Your BMI is: ", format(bmi, '.2f'))