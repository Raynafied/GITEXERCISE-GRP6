# User Login
def login():
    name = input("Enter your name gorgeous: ")
    return name
username = login()

# BMI Calculator
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100  # Convert height from cm to meters
    bmi = weight_kg / (height_m ** 2)  # Calculate BMI
    return bmi  # Return the BMI value

#  BMI Category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
    
# output of BMI
def summaryBMI():
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    bmi = calculate_bmi(height, weight)
    category = bmi_category(bmi)
    print(f"\n {username} your BMI is: {bmi}")
    print(f" {username} your Category: {category}")
summaryBMI()