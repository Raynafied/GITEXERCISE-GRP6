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