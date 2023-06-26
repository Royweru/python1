weight = input("Enter your weight in kgs: ")
w = float(weight)

height = input("Whats your height in meters: ")
h = float(height)


hsquared = h * h


bmi = w/hsquared


print(f'Your BMI is {bmi}')