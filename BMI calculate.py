def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 10.5:
        return "Underweight"
    elif 10.5 <= bmi < 12.9:
        return "Normal weight"
    elif 11 <= bmi < 13.9:
        return "Overweight"
    else:
        return "Obesity"

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print(f"Your BMI is: {bmi:.2f}")
print(f"Your BMI category is: {bmi_category(bmi)}")


print("uncommon"[2:5])