weight = input("Enter your weight in kgs: ")
w = float(weight)

height = input("Whats your height in meters: ")
h = float(height)


hsquared = h * h


bmi = w/hsquared

print(f'Your BMI is {bmi}')

if bmi <= 18:
    print("you are under weight")


elif bmi <= 29:
    print("You have normal weight")

elif bmi <= 34:
    print("You are overweight!")

else:
    print('You are just obese work on your health!!')


