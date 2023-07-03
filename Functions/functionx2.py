def calculate_months(age):
    months_lived = int(age)*12
    try:
        print(f"You have lived for {months_lived} months")
    except:
        print("There is an error either you have not input your age or the age is not an integer")


calculate_months(3)