def calculate_bmi( weight , height):
  bmi= weight/(height*height)
  print(f"Your bmi is {bmi}")


calculate_bmi(float(input("Please input your weight: ")), float(input("Please input your height: ")))