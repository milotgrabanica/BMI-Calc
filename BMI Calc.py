name = input("What is your name? ")
print("Hello " + name + ", welcome to BMI calculator" )

height = float(input("What is your height in metres:"))
weight = int(input("What is your weight in kilograms:"))
bmi = round(weight/ (height * height), 1)

if bmi <= 18.5:
     print('Your BMI is', bmi, 'which means you are underweight.')

elif bmi > 18.5 and bmi < 25:
     print('Your BMI is', bmi, 'which means you are normal.')

elif bmi > 25 and bmi < 30:
     print('Your BMI is', bmi, 'which means you are overweight.')

elif bmi > 30:
     print('Your BMI is', bmi, 'which means you are obese.')

else:
    print('There is an error with your input')

print("Thank you for using BMI calculator")


input("Press return to exit . . .")
