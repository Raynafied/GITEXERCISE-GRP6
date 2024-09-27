import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import random

class FitnessApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Fitness App')
        self.user_data = {
            'name': None,
            'age': None,
            'age_category': None,
            'height': None,
            'weight': None,
            'bmi': None,
            'bmi_category': None,
            'current_plan_type': '',
            'current_plan_step': '',
            'completed_workout': False,
            'completed_diet': False,
            'workout_day': 1,
            'diet_day': 1,
            'both_workout_day': 1,
            'both_diet_day': 1
        }

        self.plans = self.define_plans()
        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.create_menu_bar()
        self.show_login_page()

    def create_menu_bar(self):
        menubar = tk.Menu(self)
        

        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Change User", command=self.change_user)
        settings_menu.add_command(label="Change Plan", command=self.change_plan)
        settings_menu.add_command(label="Edit User Data", command=self.edit_user_data)
        menubar.add_cascade(label="Settings", menu=settings_menu)

        reset_menu = tk.Menu(menubar, tearoff=0)
        reset_menu.add_command(label="Reset Plan", command=self.reset_plan)
        menubar.add_cascade(label="Reset", menu=reset_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)


        self.config(menu=menubar)


    def reset_plan(self):
        """Reset the current workout and diet days with a confirmation dialog."""
        confirmation = messagebox.askyesno("Reset Plan", "Are you sure you want to reset all your plan data to Day 1? This cannot be undone.")
        if confirmation:
            # Reset all the workout and diet days to 1
            self.user_data['workout_day'] = 1
            self.user_data['diet_day'] = 1
            self.user_data['both_workout_day'] = 1
            self.user_data['both_diet_day'] = 1
            self.user_data['completed_workout'] = False
            self.user_data['completed_diet'] = False

            self.save_data()  # Save the changes
            messagebox.showinfo("Plan Reset", "All plans have been reset to Day 1.")
        else:
            messagebox.showinfo("Plan Not Reset", "Your plans were not reset.")


    def edit_user_data(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        
        def save_changes():
            try:
                self.user_data['weight'] = float(weight_entry.get()) 
                self.user_data['height'] = float(height_entry.get()) 
                self.user_data['age'] = int(age_entry.get())

                
                # Recalculate BMI and age category
                height_m = self.user_data['height'] / 100  #cm to m
                weight = self.user_data['weight']
                bmi = weight / (height_m ** 2)
                self.user_data['bmi'] = bmi

                if bmi < 18.5:
                    self.user_data['bmi_category'] = 'Underweight'
                elif 18.5 <= bmi < 24.9:
                    self.user_data['bmi_category'] = 'Normal weight'
                elif 25 <= bmi < 29.9:
                    self.user_data['bmi_category'] = 'Overweight'
                else:
                    self.user_data['bmi_category'] = 'Obesity'

                if self.user_data['age'] <= 25:
                    self.user_data['age_category'] = '25 and below'
                elif 26 <= self.user_data['age'] <= 35:
                    self.user_data['age_category'] = '26-35'
                else:
                    self.user_data['age_category'] = '36+'

                bmi_result_label.config(text=f"BMI: {bmi:.2f} ({self.user_data['bmi_category']})")
                
                messagebox.showinfo("Success", "User data updated successfully.")
                self.save_data()  # Save changes to file
                self.show_plan_choice_page()  # Return to main menu
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for weight, height, and age.")


        label = ttk.Label(self.frame, text="Edit Your Data")
        label.pack(pady=20)

        weight_label = ttk.Label(self.frame, text="Weight (kg): ")
        weight_label.pack()
        weight_entry = ttk.Entry(self.frame)
        weight_entry.insert(0, self.user_data['weight'])  # pre-fill with current weight
        weight_entry.pack(pady=5)

        height_label = ttk.Label(self.frame, text="Height (cm): ")
        height_label.pack()
        height_entry = ttk.Entry(self.frame)
        height_entry.insert(0, self.user_data['height'])  # pre-fill with current height
        height_entry.pack(pady=5)

        age_label = ttk.Label(self.frame, text="Age: ")
        age_label.pack()
        age_entry = ttk.Entry(self.frame)
        age_entry.insert(0, self.user_data['age'])  # pre-fill with current age
        age_entry.pack(pady=5)

        bmi_result_label = ttk.Label(self.frame, text="")
        bmi_result_label.pack(pady=20)

        save_button = ttk.Button(self.frame, text="Save Changes", command=save_changes)
        save_button.pack(pady=20)


    def define_plans(self):
        return {
            'workout': {
                '25 and below': {
                    'Underweight': [
                        ["Bodyweight Squats", "Push-ups", "Yoga (At Home)"],
                        ["Jumping Jacks", "Pilates (At Home)", "Light Strength Training"],
                        ["Brisk Walking in Place", "Core Exercises", "Mountain Climbers"],
                        ["Rest Day"],
                        ["Running in Place", "HIIT (At Home)", "Strength Training (Bodyweight)"],
                        ["Burpees", "Cycling (Stationary)", "Dance Workout (At Home)"],
                        ["Swimming Simulation (Arm Exercises)", "Kickboxing (At Home)", "Yoga (At Home)"]
                    ],
                    'Normal weight': [
                        ["Bodyweight Exercises", "HIIT (At Home)", "Strength Training (Bodyweight)"],
                        ["Circuit Training (At Home)", "Jump Rope", "Yoga (At Home)"],
                        ["Core Strengthening", "Dance Workout", "Bodyweight Strength Training"],
                        ["Rest Day"],
                        ["Running in Place", "High Knees", "Jumping Jacks"],
                        ["Bodyweight Lunges", "Pilates (At Home)", "Shadow Boxing"],
                        ["Stretching", "Yoga (At Home)", "Light Cardio"]
                    ],
                    'Overweight': [
                        ["Brisk Walking in Place", "Bodyweight Exercises", "Yoga (At Home)"],
                        ["Dance Workout (At Home)", "Strength Training (Bodyweight)", "Light Aerobics"],
                        ["Low-Impact Cardio", "Core Exercises", "Pilates (At Home)"],
                        ["Rest Day"],
                        ["Brisk Walking in Place", "Jumping Jacks", "Bodyweight Strength Training"],
                        ["Resistance Band Workouts", "Shadow Boxing", "Chair Exercises"],
                        ["Stretching", "Yoga (At Home)", "Low-Impact Cardio"]
                    ],
                    'Obesity': [
                        ["Chair Exercises", "Gentle Stretching", "Bodyweight Squats"],
                        ["Bodyweight Strength Training", "Seated Exercises", "Low-Impact Cardio"],
                        ["Gentle Yoga (At Home)", "Core Exercises", "Walking in Place"],
                        ["Rest Day"],
                        ["Chair Yoga", "Bodyweight Strength Training", "Light Walking in Place"],
                        ["Resistance Band Workouts", "Gentle Aerobics", "Brisk Walking in Place"],
                        ["Stretching", "Yoga (At Home)", "Light Cardio"]
                    ]
                },
                '26-35': {
                    'Underweight': [
                        ["Bodyweight Squats", "Push-ups", "Yoga (At Home)"],
                        ["Pilates (At Home)", "Light Weight Training", "Brisk Walking in Place"],
                        ["Core Exercises", "Dance Workout", "Light Cardio"],
                        ["Rest Day"],
                        ["Bodyweight Strength Training", "Jump Rope", "Yoga (At Home)"],
                        ["Shadow Boxing", "High Knees", "Bodyweight Lunges"],
                        ["Stretching", "Low-Impact Cardio", "Gentle Dance Workout"]
                    ],
                    'Normal weight': [
                        ["HIIT (At Home)", "Weight Training (At Home)", "Running in Place"],
                        ["Circuit Training (At Home)", "Bodyweight Exercises", "Yoga (At Home)"],
                        ["Core Strengthening", "Dance Workout (At Home)", "Jumping Jacks"],
                        ["Rest Day"],
                        ["Bodyweight Strength Training", "High Knees", "Burpees"],
                        ["Pilates (At Home)", "Shadow Boxing", "Light Cardio"],
                        ["Stretching", "Yoga (At Home)", "Low-Impact Cardio"]
                    ],
                    'Overweight': [
                        ["Walking in Place", "Bodyweight Exercises", "Gentle Yoga (At Home)"],
                        ["Dance Workout (At Home)", "Strength Training (Bodyweight)", "Light Aerobics"],
                        ["Core Exercises", "Low-Impact Cardio", "Resistance Band Workouts"],
                        ["Rest Day"],
                        ["Brisk Walking in Place", "Jumping Jacks", "Bodyweight Strength Training"],
                        ["Shadow Boxing", "Chair Exercises", "Light Cardio"],
                        ["Stretching", "Yoga (At Home)", "Low-Impact Cardio"]
                    ],
                    'Obesity': [
                        ["Chair Exercises", "Gentle Stretching", "Bodyweight Squats"],
                        ["Bodyweight Strength Training", "Low-Impact Cardio", "Seated Exercises"],
                        ["Gentle Yoga (At Home)", "Core Exercises", "Walking in Place"],
                        ["Rest Day"],
                        ["Chair Yoga", "Bodyweight Strength Training", "Light Walking in Place"],
                        ["Resistance Band Workouts", "Gentle Aerobics", "Brisk Walking in Place"],
                        ["Stretching", "Yoga (At Home)", "Light Cardio"]
                    ]
                },
                '36+': {
                    'Underweight': [
                        ["Light Cardio", "Walking", "Bodyweight Squats"],
                        ["Yoga (At Home)", "Pilates (At Home)", "Bodyweight Exercises"],
                        ["Dance Workout (At Home)", "Gentle Strength Training", "Core Exercises"],
                        ["Rest Day"],
                        ["Low-Intensity Cardio", "Brisk Walking in Place", "Gentle Stretching"],
                        ["Light Strength Training", "Yoga (At Home)", "Walking in Place"],
                        ["Stretching", "Low-Impact Cardio", "Chair Exercises"]
                    ],
                    'Normal weight': [
                        ["Strength Training (Bodyweight)", "Running in Place", "Yoga (At Home)"],
                        ["HIIT (At Home)", "Bodyweight Exercises", "Dance Workout"],
                        ["Core Strengthening", "Shadow Boxing", "Pilates (At Home)"],
                        ["Rest Day"],
                        ["High Knees", "Bodyweight Lunges", "Brisk Walking in Place"],
                        ["Jumping Jacks", "Bodyweight Strength Training", "Yoga (At Home)"],
                        ["Stretching", "Low-Impact Cardio", "Dance Workout"]
                    ],
                    'Overweight': [
                        ["Walking in Place", "Bodyweight Exercises", "Gentle Yoga (At Home)"],
                        ["Dance Workout (At Home)", "Strength Training (Bodyweight)", "Light Aerobics"],
                        ["Core Exercises", "Low-Impact Cardio", "Resistance Band Workouts"],
                        ["Rest Day"],
                        ["Brisk Walking in Place", "Jumping Jacks", "Bodyweight Strength Training"],
                        ["Shadow Boxing", "Chair Exercises", "Light Cardio"],
                        ["Stretching", "Yoga (At Home)", "Low-Impact Cardio"]
                    ],
                    'Obesity': [
                        ["Chair Exercises", "Gentle Stretching", "Bodyweight Squats"],
                        ["Bodyweight Strength Training", "Low-Impact Cardio", "Seated Exercises"],
                        ["Gentle Yoga (At Home)", "Core Exercises", "Walking in Place"],
                        ["Rest Day"],
                        ["Chair Yoga", "Bodyweight Strength Training", "Light Walking in Place"],
                        ["Resistance Band Workouts", "Gentle Aerobics", "Brisk Walking in Place"],
                        ["Stretching", "Yoga (At Home)", "Light Cardio"]
                    ]
                }
            },
        

            'diet': {
                '25 and below': {
                    'Underweight': [
                        ["Oatmeal with Fruits", "Grilled Chicken Salad", "Quinoa Bowl"],
                        ["Smoothie with Spinach and Banana", "Turkey Sandwich on Whole Grain", "Greek Yogurt with Honey"],
                        ["Pasta with Olive Oil and Vegetables", "Beef Tacos with Avocado", "Cottage Cheese with Pineapple"],
                        ["Eggs and Avocado Toast", "Stir-Fried Tofu and Vegetables", "Rice with Black Beans"],
                        ["Chili with Beans", "Peanut Butter and Banana Sandwich", "Baked Salmon with Sweet Potato"],
                        ["Homemade Protein Bars", "Vegetable Omelette", "Chickpea Salad"],
                        ["Cheese and Whole Grain Crackers", "Fruit and Nut Mix", "Brown Rice with Chicken"],
                    ],
                    'Normal weight': [
                        ["Oatmeal with Berries", "Grilled Chicken Breast", "Steamed Broccoli"],
                        ["Whole Wheat Toast with Avocado", "Lentil Soup", "Mixed Green Salad"],
                        ["Quinoa Salad with Feta", "Stir-Fried Vegetables with Tofu", "Fruit Smoothie"],
                        ["Egg and Spinach Breakfast Burrito", "Vegetable Stir Fry with Brown Rice", "Turkey Wrap"],
                        ["Chickpea Curry with Rice", "Stuffed Peppers with Quinoa", "Greek Yogurt with Granola"],
                        ["Baked Sweet Potato with Black Beans", "Fish Tacos with Cabbage Slaw", "Cottage Cheese with Peaches"],
                        ["Grilled Shrimp with Zucchini Noodles", "Pasta Primavera", "Fruit Salad"],
                    ],
                    'Overweight': [
                        ["Overnight Oats with Almonds", "Salad with Grilled Chicken", "Steamed Asparagus"],
                        ["Quinoa Bowl with Black Beans", "Vegetable Soup", "Baked Chicken with Sweet Potato"],
                        ["Grilled Salmon with Broccoli", "Chickpea Salad", "Rice and Lentils"],
                        ["Stir-Fried Tofu with Mixed Vegetables", "Whole Wheat Pasta with Marinara", "Fruit with Nut Butter"],
                        ["Zucchini Noodles with Pesto", "Turkey and Spinach Wrap", "Quinoa and Roasted Vegetables"],
                        ["Cabbage Salad with Chickpeas", "Baked Cod with Green Beans", "Smoothie Bowl with Berries"],
                        ["Vegetable Omelette with Whole Grain Toast", "Greek Salad with Feta", "Stuffed Zucchini"],
                    ],
                    'Obesity': [
                        ["Smoothie with Spinach, Banana, and Protein Powder", "Grilled Chicken Salad", "Quinoa and Black Bean Bowl"],
                        ["Overnight Chia Pudding with Berries", "Turkey and Vegetable Stir-Fry", "Zucchini Noodles with Marinara"],
                        ["Lentil Soup with Whole Wheat Bread", "Stuffed Bell Peppers with Quinoa", "Salad with Chickpeas and Avocado"],
                        ["Baked Salmon with Roasted Brussels Sprouts", "Cauliflower Rice Stir-Fry", "Greek Yogurt with Fresh Fruit"],
                        ["Eggs Scrambled with Spinach and Tomatoes", "Fish Tacos with Cabbage", "Vegetable Curry with Rice"],
                        ["Chickpea and Spinach Stew", "Cabbage and Carrot Slaw", "Baked Chicken Thighs with Sweet Potatoes"],
                        ["Homemade Vegetable Soup", "Quinoa Salad with Roasted Vegetables", "Fruit Salad with Nuts"],
                    ],
                },
                '26-35': {
                    'Underweight': [
                        ["Pancakes with Maple Syrup", "Baked Chicken with Veggies", "Smoothie Bowl"],
                        ["Pasta with Pesto and Chicken", "Egg Salad Sandwich", "Fruit and Nut Bar"],
                        ["Chili with Cornbread", "Stuffed Peppers", "Chicken and Rice"],
                        ["Omelette with Cheese and Spinach", "Fish with Roasted Vegetables", "Greek Yogurt with Honey"],
                        ["Burgers with Sweet Potato Fries", "Quinoa Bowl with Chickpeas", "Peanut Butter Banana Toast"],
                        ["Tacos with Ground Turkey", "Cauliflower Rice Stir-Fry", "Protein Smoothie"],
                        ["Sushi Rolls with Avocado", "Zucchini Noodles with Marinara", "Cottage Cheese with Berries"],
                    ],
                    'Normal weight': [
                        ["Avocado Toast with Poached Egg", "Quinoa Salad with Feta", "Grilled Chicken Breast"],
                        ["Vegetable Stir-Fry with Tofu", "Lentil Soup", "Mixed Green Salad with Nuts"],
                        ["Pasta Primavera with Shrimp", "Stuffed Zucchini with Quinoa", "Fruit Smoothie"],
                        ["Egg and Veggie Breakfast Bowl", "Turkey Wrap with Hummus", "Baked Sweet Potato with Black Beans"],
                        ["Grilled Salmon with Asparagus", "Greek Yogurt with Granola", "Chickpea Salad"],
                        ["Vegetable Omelette with Whole Grain Toast", "Fish Tacos with Cabbage Slaw", "Fruit Salad"],
                        ["Stir-Fried Tofu and Broccoli", "Baked Cod with Quinoa", "Grilled Shrimp Salad"],
                    ],
                    'Overweight': [
                        ["Smoothie with Spinach and Protein Powder", "Quinoa Bowl with Vegetables", "Grilled Chicken Salad"],
                        ["Overnight Oats with Berries", "Lentil Soup", "Chickpea Salad"],
                        ["Stuffed Peppers with Ground Turkey", "Zucchini Noodles with Marinara", "Baked Salmon with Broccoli"],
                        ["Vegetable Stir-Fry with Tofu", "Baked Sweet Potato with Black Beans", "Greek Yogurt with Honey"],
                        ["Quinoa and Vegetable Bowl", "Baked Chicken Thighs with Green Beans", "Fruit with Nut Butter"],
                        ["Homemade Vegetable Soup", "Stuffed Zucchini with Quinoa", "Fish Tacos with Cabbage"],
                        ["Grilled Shrimp with Zucchini Noodles", "Chickpea and Spinach Salad", "Smoothie Bowl with Berries"],
                    ],
                    'Obesity': [
                        ["Smoothie with Spinach, Banana, and Almond Milk", "Grilled Chicken Salad with Avocado", "Quinoa and Black Bean Bowl"],
                        ["Oatmeal with Almonds and Berries", "Baked Salmon with Asparagus", "Lentil Soup"],
                        ["Zucchini Noodles with Pesto", "Stuffed Bell Peppers with Quinoa", "Chickpea Curry"],
                        ["Baked Chicken with Roasted Brussels Sprouts", "Vegetable Stir-Fry with Tofu", "Greek Yogurt with Fresh Fruit"],
                        ["Cabbage Salad with Chickpeas", "Baked Cod with Cauliflower Rice", "Smoothie Bowl with Spinach"],
                        ["Eggs Scrambled with Tomatoes and Spinach", "Fish Tacos with Avocado", "Vegetable Soup"],
                        ["Chickpea Stew with Spinach", "Quinoa Salad with Roasted Vegetables", "Fruit Salad with Nuts"],
                    ],
                },
                '36+': {
                    'Underweight': [
                        ["Smoothie with Spinach and Banana", "Chicken Stir-Fry with Vegetables", "Oatmeal with Nuts"],
                        ["Pasta with Olive Oil and Chicken", "Baked Salmon with Quinoa", "Greek Yogurt with Berries"],
                        ["Egg Salad Sandwich on Whole Grain", "Vegetable Soup", "Chili with Beans"],
                        ["Fruit Salad with Nut Butter", "Rice with Stir-Fried Tofu", "Stuffed Peppers with Ground Turkey"],
                        ["Chickpea Salad with Avocado", "Grilled Cheese with Tomato Soup", "Pancakes with Maple Syrup"],
                        ["Vegetable Omelette with Whole Grain Toast", "Quinoa Bowl with Grilled Chicken", "Cottage Cheese with Peaches"],
                        ["Baked Sweet Potato with Black Beans", "Turkey Sandwich on Whole Grain", "Smoothie Bowl with Fruits"],
                    ],
                    'Normal weight': [
                        ["Oatmeal with Berries", "Quinoa Salad with Chickpeas", "Grilled Chicken Breast"],
                        ["Vegetable Stir-Fry with Tofu", "Lentil Soup", "Mixed Green Salad"],
                        ["Stuffed Zucchini with Quinoa", "Pasta Primavera", "Fruit Smoothie"],
                        ["Egg and Veggie Breakfast Bowl", "Turkey Wrap with Hummus", "Baked Sweet Potato"],
                        ["Grilled Salmon with Asparagus", "Greek Yogurt with Granola", "Chickpea Salad"],
                        ["Vegetable Omelette with Whole Grain Toast", "Fish Tacos with Cabbage Slaw", "Fruit Salad"],
                        ["Stir-Fried Tofu and Broccoli", "Baked Cod with Quinoa", "Grilled Shrimp Salad"],
                    ],
                    'Overweight': [
                        ["Smoothie with Spinach and Protein Powder", "Grilled Chicken Salad with Avocado", "Quinoa Bowl with Vegetables"],
                        ["Oatmeal with Almonds and Berries", "Baked Salmon with Broccoli", "Lentil Soup"],
                        ["Zucchini Noodles with Marinara", "Stuffed Bell Peppers with Quinoa", "Chickpea Curry"],
                        ["Baked Chicken with Roasted Brussels Sprouts", "Vegetable Stir-Fry with Tofu", "Greek Yogurt with Fresh Fruit"],
                        ["Cabbage Salad with Chickpeas", "Baked Cod with Cauliflower Rice", "Smoothie Bowl with Spinach"],
                        ["Eggs Scrambled with Tomatoes and Spinach", "Fish Tacos with Avocado", "Vegetable Soup"],
                        ["Chickpea Stew with Spinach", "Quinoa Salad with Roasted Vegetables", "Fruit Salad with Nuts"],
                    ],
                    'Obesity': [
                        ["Smoothie with Spinach, Banana, and Almond Milk", "Grilled Chicken Salad with Avocado", "Quinoa and Black Bean Bowl"],
                        ["Oatmeal with Almonds and Berries", "Baked Salmon with Asparagus", "Lentil Soup"],
                        ["Zucchini Noodles with Pesto", "Stuffed Bell Peppers with Quinoa", "Chickpea Curry"],
                        ["Baked Chicken with Roasted Brussels Sprouts", "Vegetable Stir-Fry with Tofu", "Greek Yogurt with Fresh Fruit"],
                        ["Cabbage Salad with Chickpeas", "Baked Cod with Cauliflower Rice", "Smoothie Bowl with Spinach"],
                        ["Eggs Scrambled with Tomatoes and Spinach", "Fish Tacos with Avocado", "Vegetable Soup"],
                        ["Chickpea Stew with Spinach", "Quinoa Salad with Roasted Vegetables", "Fruit Salad with Nuts"],
                    ],
                },
            }
        }
    
    def change_plan(self):
            for widget in self.frame.winfo_children():
                widget.destroy()

            label = ttk.Label(self.frame, text="Select a New Plan:")
            label.pack(pady=20)

            workout_button = ttk.Button(self.frame, text="Workout Plan", command=self.show_workout_plan)
            diet_button = ttk.Button(self.frame, text="Diet Plan", command=self.show_diet_plan)
            both_button = ttk.Button(self.frame, text="Both Workout and Diet", command=self.show_both_plans)

            workout_button.pack(pady=10)
            diet_button.pack(pady=10)
            both_button.pack(pady=10)


    def change_user(self):
        self.show_login_page()

    def show_about(self):
        messagebox.showinfo("About Fitness App", "This is a simple fitness app built using Tkinter.")

    def save_data(self):
        if self.user_data['name'] is not None:
            data_dir = os.path.join(os.path.expanduser("~"), "FitnessAppData")
            if not os.path.exists(data_dir):
                os.mkdir(data_dir)
            filename = os.path.join(data_dir, f"{self.user_data['name']}_data.json")
            try:
                with open(filename, 'w') as f:
                    json.dump(self.user_data, f)
            except Exception as e:
                print("Error saving data:", e)


    def load_data(self, name):
        data_dir = os.path.join(os.path.expanduser("~"), "FitnessAppData")
        filename = os.path.join(data_dir, f"{name}_data.json")
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    self.user_data = json.load(f)
                return True
            except Exception as e:
                print("Error loading data:", e)
        return False

    def show_login_page(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        def check_name(*args):
            if self.name_entry.get().strip() and age_entry.get().strip():
                login_button.config(state=tk.NORMAL)
            else:
                login_button.config(state=tk.DISABLED)

        def handle_login():
            name = self.name_entry.get().strip()
            age = age_entry.get().strip()
            if self.load_data(name):
                messagebox.showinfo("Welcome Back", f"Welcome back, {name}!")
                self.show_plan_choice_page()
            else:
                self.user_data['name'] = name
                try:
                    self.user_data['age'] = int(age)  # Store age
                    
                    # Set the age category based on the entered age
                    if self.user_data['age'] <= 25:
                        self.user_data['age_category'] = '25 and below'
                    elif 26 <= self.user_data['age'] <= 35:
                        self.user_data['age_category'] = '26-35'
                    else:
                        self.user_data['age_category'] = '36+'

                    # Proceed to the BMI page
                    self.show_bmi_page()
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter a valid age.")


        login_label = ttk.Label(self.frame, text="Welcome to Fitness App!")
        name_label = ttk.Label(self.frame, text="Enter Your Name: ")
        self.name_entry = ttk.Entry(self.frame)

        age_label = ttk.Label(self.frame, text="Enter Your Age: ")
        age_entry = ttk.Entry(self.frame)
        
        login_button = ttk.Button(self.frame, text="Let's Start", command=handle_login, state=tk.DISABLED)

        login_label.grid(row=0, column=0, columnspan=2, pady=40, padx=20)
        name_label.grid(row=1, column=0, padx=(0, 10), sticky="e")
        self.name_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        
        age_label.grid(row=2, column=0, padx=(0, 10), sticky="e")
        age_entry.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        login_button.grid(row=3, column=0, columnspan=2, pady=30)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        self.name_var = tk.StringVar()
        self.name_entry.config(textvariable=self.name_var)
        self.age_var = tk.StringVar()
        age_entry.config(textvariable=self.age_var)

        self.name_var.trace("w", check_name)
        self.age_var.trace("w", check_name)



    def show_age_page(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        def calculate_age_category():
            try:
                age = int(age_entry.get())
                self.user_data['age'] = age
                if age <= 25:
                    self.user_data['age_category'] = '25 and below'
                elif 26 <= age <= 35:
                    self.user_data['age_category'] = '26-35'
                else:
                    self.user_data['age_category'] = '36+'
                self.show_bmi_page()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid age.")

        age_label = ttk.Label(self.frame, text="Enter Your Age: ")
        age_entry = ttk.Entry(self.frame)
        age_button = ttk.Button(self.frame, text="Next", command=calculate_age_category)

        age_label.grid(row=0, column=0, padx=(0, 10), sticky="e")
        age_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")
        age_button.grid(row=1, column=0, columnspan=2, pady=30)

    def show_bmi_page(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        def calculate_bmi():
            try:
                height = float(height_entry.get()) / 100  # convert cm to m
                weight = float(weight_entry.get())
                bmi = weight / (height ** 2)
                self.user_data['height'] = height * 100  # store height in cm
                self.user_data['weight'] = weight
                self.user_data['bmi'] = bmi

                if bmi < 18.5:
                    self.user_data['bmi_category'] = 'Underweight'
                elif 18.5 <= bmi < 24.9:
                    self.user_data['bmi_category'] = 'Normal weight'
                elif 25 <= bmi < 29.9:
                    self.user_data['bmi_category'] = 'Overweight'
                else:
                    self.user_data['bmi_category'] = 'Obesity'

                # Display the BMI and category directly on the page
                bmi_result_label.config(text=f"BMI: {bmi:.2f} ({self.user_data['bmi_category']})")

                # Add a button to proceed to the next page after displaying the result
                next_button = ttk.Button(self.frame, text="Continue", command=self.show_plan_choice_page)
                next_button.grid(row=4, column=0, columnspan=2, pady=10)

            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid height and weight.")




        height_label = ttk.Label(self.frame, text="Enter Your Height (cm): ")
        height_entry = ttk.Entry(self.frame)
        weight_label = ttk.Label(self.frame, text="Enter Your Weight (kg): ")
        weight_entry = ttk.Entry(self.frame)
        bmi_button = ttk.Button(self.frame, text="Calculate BMI", command=calculate_bmi)

        bmi_result_label = ttk.Label(self.frame, text="BMI will be displayed here after calculation")

        height_label.grid(row=0, column=0, padx=(0, 10), sticky="e")
        height_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")
        weight_label.grid(row=1, column=0, padx=(0, 10), sticky="e")
        weight_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        bmi_button.grid(row=2, column=0, columnspan=2, pady=30)

        bmi_result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def show_plan_choice_page(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Display the user's name
        name_label = ttk.Label(self.frame, text=f"Welcome, {self.user_data['name']}!")
        name_label.pack(pady=10)

        # Display the user's age under the name
        age_label = ttk.Label(self.frame, text=f"Your Age: {self.user_data['age']}")
        age_label.pack(pady=10)

        workout_button = ttk.Button(self.frame, text="Workout Plan", command=self.show_workout_plan)
        diet_button = ttk.Button(self.frame, text="Diet Plan", command=self.show_diet_plan)
        both_button = ttk.Button(self.frame, text="Both Workout and Diet", command=self.show_both_plans)

        workout_button.pack(pady=20)
        diet_button.pack(pady=20)
        both_button.pack(pady=20)




    def show_workout_plan(self):
        self.user_data['current_plan_type'] = 'workout'
        self.user_data['current_plan_step'] = 'workout'
        self.save_data()
        self.show_plan_page()

    def show_diet_plan(self):
        self.user_data['current_plan_type'] = 'diet'
        self.user_data['current_plan_step'] = 'diet'
        self.save_data()
        self.show_plan_page()

    def show_both_plans(self):
        self.user_data['current_plan_type'] = 'both'
        self.user_data['current_plan_step'] = 'workout'  # Start with workout
        self.save_data()
        self.show_plan_page()

    def show_plan_page(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        tasks = []
        if self.user_data['current_plan_type'] == 'workout':
            current_day = self.user_data['workout_day'] % 7  # Cycle through 1 to 7
            if current_day == 0:
                current_day = 7
            plan_label = tk.Label(self.frame, text=f"Workout Plan for Day {current_day}")
            plan_details = self.plans['workout'][self.user_data['age_category']][self.user_data['bmi_category']][current_day - 1]
            tasks = plan_details
        elif self.user_data['current_plan_type'] == 'diet':
            current_day = self.user_data['diet_day'] % 7  # Cycle through 1 to 7
            if current_day == 0:
                current_day = 7
            plan_label = tk.Label(self.frame, text=f"Diet Plan for Day {current_day}")
            plan_details = self.plans['diet'][self.user_data['age_category']][self.user_data['bmi_category']][current_day - 1]
            tasks = plan_details
        elif self.user_data['current_plan_type'] == 'both':
            # Handle both plans similarly with current_day logic
            pass
            if self.user_data['current_plan_step'] == 'workout':
                    plan_label = tk.Label(self.frame, text=f"Workout Plan for Day {self.user_data['both_workout_day']}")
                    plan_details = self.plans['workout'][self.user_data['age_category']][self.user_data['bmi_category']][self.user_data['both_workout_day'] - 1]
                    tasks = plan_details
            else:
                    plan_label = tk.Label(self.frame, text=f"Diet Plan for Day {self.user_data['both_diet_day']}")
                    plan_details = self.plans['diet'][self.user_data['age_category']][self.user_data['bmi_category']][self.user_data['both_diet_day'] - 1]
                    tasks = plan_details

        plan_label.pack(pady=20)

        self.task_vars = []  # List to hold the IntVar for each task checkbox
        for task in tasks:
            var = tk.IntVar(value=0)  # 0 for unchecked, 1 for checked
            self.task_vars.append(var)
            checkbox = tk.Checkbutton(self.frame, text=task, variable=var)
            checkbox.pack(anchor='w')

        complete_button = tk.Button(self.frame, text="Complete", command=self.complete_plan)
        complete_button.pack(pady=20)

    def complete_plan(self):
        all_completed = all(var.get() == 1 for var in self.task_vars)

        if all_completed:
            if self.user_data['current_plan_type'] == 'workout':
                self.user_data['completed_workout'] = True
                self.user_data['workout_day'] += 1
            elif self.user_data['current_plan_type'] == 'diet':
                self.user_data['completed_diet'] = True
                self.user_data['diet_day'] += 1
            elif self.user_data['current_plan_type'] == 'both':
                if self.user_data['current_plan_step'] == 'workout':
                    self.user_data['completed_workout'] = True
                    self.user_data['both_workout_day'] += 1
                    self.user_data['current_plan_step'] = 'diet'  # Switch to diet
                else:
                    self.user_data['completed_diet'] = True
                    self.user_data['both_diet_day'] += 1
                    self.user_data['current_plan_step'] = 'workout'  # Switch back to workout
        else:
            messagebox.showwarning("Incomplete Tasks", "Please complete all tasks before proceeding.")

        self.save_data()
        self.show_plan_page()


if __name__ == "__main__":
    app = FitnessApp()
    app.mainloop()



