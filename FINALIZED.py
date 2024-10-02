# import tkinter as tk
# from tkinter import ttk, messagebox
# import json
# import os
# import random
# import webbrowser 
# from PIL import Image, ImageTk
# from tkinter import Button
# #import shelve

# class FitnessApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry('500x500')
#         self.title('Fitness App')
#         self.current_bg_key = 'welcome'  # Store the current background key
        
#         self.user_data = {
#             'name': None,
#             'age': None,
#             'age_category': None,
#             'height': None,
#             'weight': None,
#             'bmi': None,
#             'bmi_category': None,
#             'current_plan_type': '',
#             'current_plan_step': '',
#             'completed_workout': False,
#             'completed_diet': False,
#             'workout_day': 1,
#             'diet_day': 1,
#             'both_workout_day': 1,
#             'both_diet_day': 1
#         }

#         self.plans = self.define_plans()
#         self.create_menu_bar()

#         # Load background images into a dictionary
#         self.bg_images = {
#             'welcome': Image.open(r"C:\Users\MY-PC\Documents\rk personal\images\welcome.png"),
#             'LOGINPAGE': Image.open(r"C:\Users\MY-PC\Documents\rk personal\images\bg (1).png"),
#             'BMIPAGE': Image.open(r"C:\Users\MY-PC\Documents\rk personal\images\bg (2).png"),
#             'PLACSPAGE': Image.open(r"c:\Users\MY-PC\Documents\rk personal\images\bg (3).png"),
#             'PLAS3PAGEWORKOUT': Image.open(r"c:\Users\MY-PC\Documents\rk personal\images\bg (4).png"),
#             'PLAS3PAGEDIET': Image.open(r"c:\Users\MY-PC\Documents\rk personal\images\bg (5).png"),
#             'SUMRPAGE': Image.open(r"c:\Users\MY-PC\Documents\rk personal\images\bg (6).png"),
#         }

#         self.canvas = tk.Canvas(self)
#         self.canvas.pack(fill=tk.BOTH, expand=True)

#         self.bg_image = ImageTk.PhotoImage(self.bg_images['welcome'].resize((500, 500)))
#         self.bg_image_on_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.bg_image)

#         self.content_frame = ttk.Frame(self.canvas, style='Transparent.TFrame')
#         self.canvas_window = self.canvas.create_window(250, 250, anchor='center', window=self.content_frame)

#         self.bind("<Configure>", self.resize_bg_image)

#         self.welcome_login_page()

#     def resize_bg_image(self, event=None):
#         new_width = self.winfo_width()
#         new_height = self.winfo_height()
#         resized_image = self.bg_images[self.current_bg_key].resize((new_width, new_height), Image.LANCZOS)
#         self.bg_image = ImageTk.PhotoImage(resized_image)
#         self.canvas.itemconfig(self.bg_image_on_canvas, image=self.bg_image)
#         self.canvas.coords(self.canvas_window, new_width/2, new_height/2)

#     def update_background(self, image_key):
#         self.current_bg_key = image_key  # Update the current background key
#         bg = self.bg_images[image_key].resize((self.winfo_width(), self.winfo_height()), Image.LANCZOS)
#         self.bg_image = ImageTk.PhotoImage(bg)
#         self.canvas.itemconfig(self.bg_image_on_canvas, image=self.bg_image)
        
#     def welcome_login_page(self):
#         self.update_background('welcome')
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#         welcome_label = ttk.Label(self.content_frame, text="Welcome to the SheFIT!", font=("Segoe Script", 16, "bold"))
#         welcome_label.pack(pady=20)

#         description_label = ttk.Label(
#             self.content_frame, 
#             text = "Unlock your fitness journey with SheFIT!\n" \
#             "Custom workout and meal plans tailored for women.\n" \
#             "Choose from engaging workout video guides \n"
#             "Take one step at a time with 7-day challenges and transform your lifestyle today! 💪✨",
#             font=("Display", 12,'italic'),
#             wraplength=400,  # Set a max width for the text
#             justify="center"
#         )
#         description_label.pack(pady=10)

#         # start_button = ttk.Button(self.content_frame, text="Get Started", command=self.show_login_page)
#         start_button = tk.Button(self.content_frame, text="Get Started", command=self.show_login_page, font=("Segoe Script", 9, "bold"), bg="#C8A0D4", fg="black")
#         # workout_button = tk.Button(self.content_frame, text="Workout Plan", command=self.show_workout_plan, font=("Segoe Script", 12, "bold"), bg="#DDA0DD", fg="black")
#         start_button.pack(pady=20)

#         # Optional: Add a stylish border or background
#         self.content_frame.config(relief="sunken", borderwidth=5)
#         self.content_frame.pack(pady=20)

#     def create_menu_bar(self):
#         menubar = tk.Menu(self)
        
#         settings_menu = tk.Menu(menubar, tearoff=0)
#         settings_menu.add_command(label="Change User", command=self.change_user)
#         settings_menu.add_command(label="Change Plan", command=self.change_plan)
#         settings_menu.add_command(label="Edit User Data", command=self.edit_user_data)
#         settings_menu.add_command(label="View My Summary Chart", command=self.show_summary_page)
#         menubar.add_cascade(label="Settings", menu=settings_menu)

#         reset_menu = tk.Menu(menubar, tearoff=0)
#         reset_menu.add_command(label="Reset Plan", command=self.reset_plan)
#         menubar.add_cascade(label="Reset", menu=reset_menu)

#         help_menu = tk.Menu(menubar, tearoff=0)
#         help_menu.add_command(label="About", command=self.show_about)
#         menubar.add_cascade(label="Help", menu=help_menu)

#         self.config(menu=menubar)

#     def reset_plan(self):
#         """Reset the current workout and diet days with a confirmation dialog."""
#         confirmation = messagebox.askyesno("Reset Plan", "Are you sure you want to reset all your plan data to Day 1? This cannot be undone.")
#         if confirmation:
#             # Reset all the workout and diet days to 1
#             self.user_data['workout_day'] = 1
#             self.user_data['diet_day'] = 1
#             self.user_data['both_workout_day'] = 1
#             self.user_data['both_diet_day'] = 1
#             self.user_data['completed_workout'] = False
#             self.user_data['completed_diet'] = False

#             self.save_data()  # Save the changes
#             messagebox.showinfo("Plan Reset", "All plans have been reset to Day 1.")
#         else:
#             messagebox.showinfo("Plan Not Reset", "Your plans were not reset.")


#     def edit_user_data(self):
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#         def save_changes():
#             try:
#                 weight = float(weight_entry.get())
#                 height = float(height_entry.get())
#                 age_str = age_entry.get()

#                 # Age validation
#                 if not age_str.isdigit():
#                     messagebox.showerror("Invalid Input", "Please enter only digits for age.")
#                     return

#                 age = int(age_str)
#                 if age > 75:
#                     messagebox.showerror("Invalid Age", "Age must be 75 or below.")
#                     return
#                 self.user_data['weight'] = float(weight_entry.get())
#                 self.user_data['height'] = float(height_entry.get())
#                 self.user_data['age'] = int(age_entry.get())
                
#                 # Recalculate BMI and age category
#                 height_m = self.user_data['height'] / 100  # Convert cm to m
#                 weight = self.user_data['weight']
#                 bmi = weight / (height_m ** 2)
#                 self.user_data['bmi'] = bmi

#                 if bmi < 18.5:
#                     self.user_data['bmi_category'] = 'Underweight'
#                 elif 18.5 <= bmi < 24.9:
#                     self.user_data['bmi_category'] = 'Normal weight'
#                 elif 25 <= bmi < 29.9:
#                     self.user_data['bmi_category'] = 'Overweight'
#                 else:
#                     self.user_data['bmi_category'] = 'Obesity'

#                 if self.user_data['age'] <= 25:
#                     self.user_data['age_category'] = '25 and below'
#                 elif 26 <= self.user_data['age'] <= 35:
#                     self.user_data['age_category'] = '26-35'
#                 else:
#                     self.user_data['age_category'] = '36+'

#                 bmi_result_label.config(text=f"BMI: {bmi:.2f} ({self.user_data['bmi_category']})")
                
#                 messagebox.showinfo("Success", "User data updated successfully.")
#                 self.save_data()  # Save changes to file
#                 self.show_plan_choice_page()  # Return to main menu
#             except ValueError:
#                 messagebox.showerror("Invalid Input", "Please enter valid numbers for weight, height, and age.")


#         label = ttk.Label(self.content_frame, text="Edit Your Data")
#         label.pack(pady=20)

#         weight_label = ttk.Label(self.content_frame, text="Weight (kg): ")
#         weight_label.pack()
#         weight_entry = ttk.Entry(self.content_frame)
#         weight_entry.insert(0, self.user_data['weight'])  # pre-fill with current weight
#         weight_entry.pack(pady=5)

#         height_label = ttk.Label(self.content_frame, text="Height (cm): ")
#         height_label.pack()
#         height_entry = ttk.Entry(self.content_frame)
#         height_entry.insert(0, self.user_data['height'])  # pre-fill with current height
#         height_entry.pack(pady=5)

#         age_label = ttk.Label(self.content_frame, text="Age: ")
#         age_label.pack()
#         age_entry = ttk.Entry(self.content_frame)
#         age_entry.insert(0, self.user_data['age'])  # pre-fill with current age
#         age_entry.pack(pady=5)

#         bmi_result_label = ttk.Label(self.content_frame, text="")
#         bmi_result_label.pack(pady=20)

#         save_button = ttk.Button(self.content_frame, text="Save Changes", command=save_changes)
#         save_button.pack(pady=20)

#     def define_plans(self):
#         return {
#             'workout': {
#                 '25 and below': {
#                     'Underweight': [
#                         ["Bodyweight Squats", "Push-ups", "Yoga (At Home)"],
#                         ["Jumping Jacks", "Pilates (At Home)", "Light Strength Training"],
#                         ["Brisk Walking in Place", "Core Exercises", "Mountain Climbers"],
#                         ["Rest Day"],
#                         ["Running in Place", "HIIT (At Home)", "Strength Training (Bodyweight)"],
#                         ["Burpees", "Cycling (Stationary)", "Dance Workout (At Home)"],
#                         ["Swimming Simulation (Arm Exercises)", "Kickboxing (At Home)", "Yoga (At Home)"]
#                     ],
#                     'Normal weight': [
#                         ["Bodyweight Exercises", "HIIT (At Home)", "Strength Training (Bodyweight)"],
#                         ["Circuit Training (At Home)", "Jump Rope", "Yoga (At Home)"],
#                         ["Core Strengthening", "Dance Workout", "Bodyweight Strength Training"],
#                         ["Rest Day"],
#                         ["Running in Place", "High Knees", "Jumping Jacks"],
#                         ["Bodyweight Lunges", "Pilates (At Home)", "Shadow Boxing"],
#                         ["Stretching", "Yoga (At Home)", "Light Cardio"]
#                     ],
#                     'Overweight': [
#                         ["Brisk Walking in Place", "Bodyweight Exercises", "Yoga (At Home)"],
#                         ["Dance Workout (At Home)", "Strength Training (Bodyweight)", "Light Aerobics"],
#                         ["Low-Impact Cardio", "Core Exercises", "Pilates (At Home)"],
#                         ["Rest Day"],
#                         ["Brisk Walking in Place", "Jumping Jacks", "Bodyweight Strength Training"],
#                         ["Resistance Band Workouts", "Shadow Boxing", "Chair Exercises"],
#                         ["Stretching", "Yoga (At Home)", "Low-Impact Cardio"]
#                     ],
#                     'Obesity': [
#                         ["Chair Exercises", "Gentle Stretching", "Bodyweight Squats"],
#                         ["Bodyweight Strength Training", "Seated Exercises", "Low-Impact Cardio"],
#                         ["Gentle Yoga (At Home)", "Core Exercises", "Walking in Place"],
#                         ["Rest Day"],
#                         ["Chair Yoga", "Bodyweight Strength Training", "Light Walking in Place"],
#                         ["Resistance Band Workouts", "Gentle Aerobics", "Brisk Walking in Place"],
#                         ["Stretching", "Yoga (At Home)", "Light Cardio"]
#                     ]
#                 },
#                 '26-35': {
#                     'Underweight': [
#                         ["Bodyweight Squats", "Push-ups", "Yoga (At Home)"],
#                         ["Pilates (At Home)", "Light Weight Training", "Brisk Walking in Place"],
#                         ["Core Exercises", "Dance Workout", "Light Cardio"],
#                         ["Rest Day"],
#                         ["Bodyweight Strength Training", "Jump Rope", "Yoga (At Home)"],
#                         ["Shadow Boxing", "High Knees", "Bodyweight Lunges"],
#                         ["Stretching", "Low-Impact Cardio", "Gentle Dance Workout"]
#                     ],
#                     'Normal weight': [
#                         ["HIIT (At Home)", "Weight Training (At Home)", "Running in Place"],
#                         ["Circuit Training (At Home)", "Bodyweight Exercises", "Yoga (At Home)"],
#                         ["Core Strengthening", "Dance Workout (At Home)", "Jumping Jacks"],
#                         ["Rest Day"],
#                         ["Bodyweight Strength Training", "High Knees", "Burpees"],
#                         ["Pilates (At Home)", "Shadow Boxing", "Light Cardio"],
#                         ["Stretching", "Yoga (At Home)", "Low-Impact Cardio"]
#                     ],
#                     'Overweight': [
#                         ["Walking in Place", "Bodyweight Exercises", "Gentle Yoga (At Home)"],
#                         ["Dance Workout (At Home)", "Strength Training (Bodyweight)", "Light Aerobics"],
#                         ["Core Exercises", "Low-Impact Cardio", "Resistance Band Workouts"],
#                         ["Rest Day"],
#                         ["Brisk Walking in Place", "Jumping Jacks", "Bodyweight Strength Training"],
#                         ["Shadow Boxing", "Chair Exercises", "Light Cardio"],
#                         ["Stretching", "Yoga (At Home)", "Low-Impact Cardio"]
#                     ],
#                     'Obesity': [
#                         ["Chair Exercises", "Gentle Stretching", "Bodyweight Squats"],
#                         ["Bodyweight Strength Training", "Low-Impact Cardio", "Seated Exercises"],
#                         ["Gentle Yoga (At Home)", "Core Exercises", "Walking in Place"],
#                         ["Rest Day"],
#                         ["Chair Yoga", "Bodyweight Strength Training", "Light Walking in Place"],
#                         ["Resistance Band Workouts", "Gentle Aerobics", "Brisk Walking in Place"],
#                         ["Stretching", "Yoga (At Home)", "Light Cardio"]
#                     ]
#                 },
#                 '36+': {
#                     'Underweight': [
#                         ["Light Cardio", "Walking", "Bodyweight Squats"],
#                         ["Yoga (At Home)", "Pilates (At Home)", "Bodyweight Exercises"],
#                         ["Dance Workout (At Home)", "Gentle Strength Training", "Core Exercises"],
#                         ["Rest Day"],
#                         ["Low-Intensity Cardio", "Brisk Walking in Place", "Gentle Stretching"],
#                         ["Light Strength Training", "Yoga (At Home)", "Walking in Place"],
#                         ["Stretching", "Low-Impact Cardio", "Chair Exercises"]
#                     ],
#                     'Normal weight': [
#                         ["Strength Training (Bodyweight)", "Running in Place", "Yoga (At Home)"],
#                         ["HIIT (At Home)", "Bodyweight Exercises", "Dance Workout"],
#                         ["Core Strengthening", "Shadow Boxing", "Pilates (At Home)"],
#                         ["Rest Day"],
#                         ["High Knees", "Bodyweight Lunges", "Brisk Walking in Place"],
#                         ["Jumping Jacks", "Bodyweight Strength Training", "Yoga (At Home)"],
#                         ["Stretching", "Low-Impact Cardio", "Dance Workout"]
#                     ],
#                     'Overweight': [
#                         ["Walking in Place", "Bodyweight Exercises", "Gentle Yoga (At Home)"],
#                         ["Dance Workout (At Home)", "Strength Training (Bodyweight)", "Light Aerobics"],
#                         ["Core Exercises", "Low-Impact Cardio", "Resistance Band Workouts"],
#                         ["Rest Day"],
#                         ["Brisk Walking in Place", "Jumping Jacks", "Bodyweight Strength Training"],
#                         ["Shadow Boxing", "Chair Exercises", "Light Cardio"],
#                         ["Stretching", "Yoga (At Home)", "Low-Impact Cardio"]
#                     ],
#                     'Obesity': [
#                         ["Chair Exercises", "Gentle Stretching", "Bodyweight Squats"],
#                         ["Bodyweight Strength Training", "Low-Impact Cardio", "Seated Exercises"],
#                         ["Gentle Yoga (At Home)", "Core Exercises", "Walking in Place"],
#                         ["Rest Day"],
#                         ["Chair Yoga", "Bodyweight Strength Training", "Light Walking in Place"],
#                         ["Resistance Band Workouts", "Gentle Aerobics", "Brisk Walking in Place"],
#                         ["Stretching", "Yoga (At Home)", "Light Cardio"]
#                     ]
#                 }
#             },
        

#             'diet': {
#                 '25 and below': {
#                     'Underweight': [
#                         ["Oatmeal with Fruits", "Grilled Chicken Salad", "Quinoa Bowl"],
#                         ["Smoothie with Spinach and Banana", "Turkey Sandwich on Whole Grain", "Greek Yogurt with Honey"],
#                         ["Pasta with Olive Oil and Vegetables", "Beef Tacos with Avocado", "Cottage Cheese with Pineapple"],
#                         ["Eggs and Avocado Toast", "Stir-Fried Tofu and Vegetables", "Rice with Black Beans"],
#                         ["Chili with Beans", "Peanut Butter and Banana Sandwich", "Baked Salmon with Sweet Potato"],
#                         ["Homemade Protein Bars", "Vegetable Omelette", "Chickpea Salad"],
#                         ["Cheese and Whole Grain Crackers", "Fruit and Nut Mix", "Brown Rice with Chicken"],
#                     ],
#                     'Normal weight': [
#                         ["Oatmeal with Berries", "Grilled Chicken Breast", "Steamed Broccoli"],
#                         ["Whole Wheat Toast with Avocado", "Lentil Soup", "Mixed Green Salad"],
#                         ["Quinoa Salad with Feta", "Stir-Fried Vegetables with Tofu", "Fruit Smoothie"],
#                         ["Egg and Spinach Breakfast Burrito", "Vegetable Stir Fry with Brown Rice", "Turkey Wrap"],
#                         ["Chickpea Curry with Rice", "Stuffed Peppers with Quinoa", "Greek Yogurt with Granola"],
#                         ["Baked Sweet Potato with Black Beans", "Fish Tacos with Cabbage Slaw", "Cottage Cheese with Peaches"],
#                         ["Grilled Shrimp with Zucchini Noodles", "Pasta Primavera", "Fruit Salad"],
#                     ],
#                     'Overweight': [
#                         ["Overnight Oats with Almonds", "Salad with Grilled Chicken", "Steamed Asparagus"],
#                         ["Quinoa Bowl with Black Beans", "Vegetable Soup", "Baked Chicken with Sweet Potato"],
#                         ["Grilled Salmon with Broccoli", "Chickpea Salad", "Rice and Lentils"],
#                         ["Stir-Fried Tofu with Mixed Vegetables", "Whole Wheat Pasta with Marinara", "Fruit with Nut Butter"],
#                         ["Zucchini Noodles with Pesto", "Turkey and Spinach Wrap", "Quinoa and Roasted Vegetables"],
#                         ["Cabbage Salad with Chickpeas", "Baked Cod with Green Beans", "Smoothie Bowl with Berries"],
#                         ["Vegetable Omelette with Whole Grain Toast", "Greek Salad with Feta", "Stuffed Zucchini"],
#                     ],
#                     'Obesity': [
#                         ["Smoothie with Spinach, Banana, and Protein Powder", "Grilled Chicken Salad", "Quinoa and Black Bean Bowl"],
#                         ["Overnight Chia Pudding with Berries", "Turkey and Vegetable Stir-Fry", "Zucchini Noodles with Marinara"],
#                         ["Lentil Soup with Whole Wheat Bread", "Stuffed Bell Peppers with Quinoa", "Salad with Chickpeas and Avocado"],
#                         ["Baked Salmon with Roasted Brussels Sprouts", "Cauliflower Rice Stir-Fry", "Greek Yogurt with Fresh Fruit"],
#                         ["Eggs Scrambled with Spinach and Tomatoes", "Fish Tacos with Cabbage", "Vegetable Curry with Rice"],
#                         ["Chickpea and Spinach Stew", "Cabbage and Carrot Slaw", "Baked Chicken Thighs with Sweet Potatoes"],
#                         ["Homemade Vegetable Soup", "Quinoa Salad with Roasted Vegetables", "Fruit Salad with Nuts"],
#                     ],
#                 },
#                 '26-35': {
#                     'Underweight': [
#                         ["Pancakes with Maple Syrup", "Baked Chicken with Veggies", "Smoothie Bowl"],
#                         ["Pasta with Pesto and Chicken", "Egg Salad Sandwich", "Fruit and Nut Bar"],
#                         ["Chili with Cornbread", "Stuffed Peppers", "Chicken and Rice"],
#                         ["Omelette with Cheese and Spinach", "Fish with Roasted Vegetables", "Greek Yogurt with Honey"],
#                         ["Burgers with Sweet Potato Fries", "Quinoa Bowl with Chickpeas", "Peanut Butter Banana Toast"],
#                         ["Tacos with Ground Turkey", "Cauliflower Rice Stir-Fry", "Protein Smoothie"],
#                         ["Sushi Rolls with Avocado", "Zucchini Noodles with Marinara", "Cottage Cheese with Berries"],
#                     ],
#                     'Normal weight': [
#                         ["Avocado Toast with Poached Egg", "Quinoa Salad with Feta", "Grilled Chicken Breast"],
#                         ["Vegetable Stir-Fry with Tofu", "Lentil Soup", "Mixed Green Salad with Nuts"],
#                         ["Pasta Primavera with Shrimp", "Stuffed Zucchini with Quinoa", "Fruit Smoothie"],
#                         ["Egg and Veggie Breakfast Bowl", "Turkey Wrap with Hummus", "Baked Sweet Potato with Black Beans"],
#                         ["Grilled Salmon with Asparagus", "Greek Yogurt with Granola", "Chickpea Salad"],
#                         ["Vegetable Omelette with Whole Grain Toast", "Fish Tacos with Cabbage Slaw", "Fruit Salad"],
#                         ["Stir-Fried Tofu and Broccoli", "Baked Cod with Quinoa", "Grilled Shrimp Salad"],
#                     ],
#                     'Overweight': [
#                         ["Smoothie with Spinach and Protein Powder", "Quinoa Bowl with Vegetables", "Grilled Chicken Salad"],
#                         ["Overnight Oats with Berries", "Lentil Soup", "Chickpea Salad"],
#                         ["Stuffed Peppers with Ground Turkey", "Zucchini Noodles with Marinara", "Baked Salmon with Broccoli"],
#                         ["Vegetable Stir-Fry with Tofu", "Baked Sweet Potato with Black Beans", "Greek Yogurt with Honey"],
#                         ["Quinoa and Vegetable Bowl", "Baked Chicken Thighs with Green Beans", "Fruit with Nut Butter"],
#                         ["Homemade Vegetable Soup", "Stuffed Zucchini with Quinoa", "Fish Tacos with Cabbage"],
#                         ["Grilled Shrimp with Zucchini Noodles", "Chickpea and Spinach Salad", "Smoothie Bowl with Berries"],
#                     ],
#                     'Obesity': [
#                         ["Smoothie with Spinach, Banana, and Almond Milk", "Grilled Chicken Salad with Avocado", "Quinoa and Black Bean Bowl"],
#                         ["Oatmeal with Almonds and Berries", "Baked Salmon with Asparagus", "Lentil Soup"],
#                         ["Zucchini Noodles with Pesto", "Stuffed Bell Peppers with Quinoa", "Chickpea Curry"],
#                         ["Baked Chicken with Roasted Brussels Sprouts", "Vegetable Stir-Fry with Tofu", "Greek Yogurt with Fresh Fruit"],
#                         ["Cabbage Salad with Chickpeas", "Baked Cod with Cauliflower Rice", "Smoothie Bowl with Spinach"],
#                         ["Eggs Scrambled with Tomatoes and Spinach", "Fish Tacos with Avocado", "Vegetable Soup"],
#                         ["Chickpea Stew with Spinach", "Quinoa Salad with Roasted Vegetables", "Fruit Salad with Nuts"],
#                     ],
#                 },
#                 '36+': {
#                     'Underweight': [
#                         ["Smoothie with Spinach and Banana", "Chicken Stir-Fry with Vegetables", "Oatmeal with Nuts"],
#                         ["Pasta with Olive Oil and Chicken", "Baked Salmon with Quinoa", "Greek Yogurt with Berries"],
#                         ["Egg Salad Sandwich on Whole Grain", "Vegetable Soup", "Chili with Beans"],
#                         ["Fruit Salad with Nut Butter", "Rice with Stir-Fried Tofu", "Stuffed Peppers with Ground Turkey"],
#                         ["Chickpea Salad with Avocado", "Grilled Cheese with Tomato Soup", "Pancakes with Maple Syrup"],
#                         ["Vegetable Omelette with Whole Grain Toast", "Quinoa Bowl with Grilled Chicken", "Cottage Cheese with Peaches"],
#                         ["Baked Sweet Potato with Black Beans", "Turkey Sandwich on Whole Grain", "Smoothie Bowl with Fruits"],
#                     ],
#                     'Normal weight': [
#                         ["Oatmeal with Berries", "Quinoa Salad with Chickpeas", "Grilled Chicken Breast"],
#                         ["Vegetable Stir-Fry with Tofu", "Lentil Soup", "Mixed Green Salad"],
#                         ["Stuffed Zucchini with Quinoa", "Pasta Primavera", "Fruit Smoothie"],
#                         ["Egg and Veggie Breakfast Bowl", "Turkey Wrap with Hummus", "Baked Sweet Potato"],
#                         ["Grilled Salmon with Asparagus", "Greek Yogurt with Granola", "Chickpea Salad"],
#                         ["Vegetable Omelette with Whole Grain Toast", "Fish Tacos with Cabbage Slaw", "Fruit Salad"],
#                         ["Stir-Fried Tofu and Broccoli", "Baked Cod with Quinoa", "Grilled Shrimp Salad"],
#                     ],
#                     'Overweight': [
#                         ["Smoothie with Spinach and Protein Powder", "Grilled Chicken Salad with Avocado", "Quinoa Bowl with Vegetables"],
#                         ["Oatmeal with Almonds and Berries", "Baked Salmon with Broccoli", "Lentil Soup"],
#                         ["Zucchini Noodles with Marinara", "Stuffed Bell Peppers with Quinoa", "Chickpea Curry"],
#                         ["Baked Chicken with Roasted Brussels Sprouts", "Vegetable Stir-Fry with Tofu", "Greek Yogurt with Fresh Fruit"],
#                         ["Cabbage Salad with Chickpeas", "Baked Cod with Cauliflower Rice", "Smoothie Bowl with Spinach"],
#                         ["Eggs Scrambled with Tomatoes and Spinach", "Fish Tacos with Avocado", "Vegetable Soup"],
#                         ["Chickpea Stew with Spinach", "Quinoa Salad with Roasted Vegetables", "Fruit Salad with Nuts"],
#                     ],
#                     'Obesity': [
#                         ["Smoothie with Spinach, Banana, and Almond Milk", "Grilled Chicken Salad with Avocado", "Quinoa and Black Bean Bowl"],
#                         ["Oatmeal with Almonds and Berries", "Baked Salmon with Asparagus", "Lentil Soup"],
#                         ["Zucchini Noodles with Pesto", "Stuffed Bell Peppers with Quinoa", "Chickpea Curry"],
#                         ["Baked Chicken with Roasted Brussels Sprouts", "Vegetable Stir-Fry with Tofu", "Greek Yogurt with Fresh Fruit"],
#                         ["Cabbage Salad with Chickpeas", "Baked Cod with Cauliflower Rice", "Smoothie Bowl with Spinach"],
#                         ["Eggs Scrambled with Tomatoes and Spinach", "Fish Tacos with Avocado", "Vegetable Soup"],
#                         ["Chickpea Stew with Spinach", "Quinoa Salad with Roasted Vegetables", "Fruit Salad with Nuts"],
#                     ],
#                 },
#             }
#         }
    
#     def change_plan(self):
#             for widget in self.content_frame.winfo_children():
#                 widget.destroy()

#             label = ttk.Label(self.content_frame, text="Select a New Plan:")
#             label.pack(pady=20)

#             workout_button = tk.Button(self.content_frame, text="Workout Plan", command=self.show_workout_plan, font=("Segoe Script", 12, "bold"), bg="#DDA0DD", fg="black")
#             diet_button = tk.Button(self.content_frame, text="Diet Plan", command=self.show_diet_plan, font=("Segoe Script", 12, "bold"), bg="#DDA0DD", fg="black")
#             both_button = tk.Button(self.content_frame, text="Both Workout and Diet", command=self.show_both_plans, font=("Segoe Script", 12, "bold"), bg="#DDA0DD", fg="black")

#             workout_button.pack(pady=20)
#             diet_button.pack(pady=20)
#             both_button.pack(pady=20)


#     def change_user(self):
#         self.show_login_page()

#     def show_about(self):
#         messagebox.showinfo("SheFit is a revolutionary fitness app designed exclusively for women, offering personalized home workout plans and nutritious meal guidance. Our mission is to empower women on their health journeys, making fitness accessible and enjoyable, and celebrating every step towards a healthier, stronger you.")

#     def save_data(self):
#         if self.user_data['name'] is not None:
#             data_dir = os.path.join(os.path.expanduser("~"), "FitnessAppData")
#             if not os.path.exists(data_dir):
#                 os.mkdir(data_dir)
#             filename = os.path.join(data_dir, f"{self.user_data['name']}_data.json")
#             try:
#                 with open(filename, 'w') as f:
#                     json.dump(self.user_data, f)
#             except Exception as e:
#                 print("Error saving data:", e)


#     def load_data(self, name):
#         data_dir = os.path.join(os.path.expanduser("~"), "FitnessAppData")
#         filename = os.path.join(data_dir, f"{name}_data.json")
#         if os.path.exists(filename):
#             try:
#                 with open(filename, 'r') as f:
#                     self.user_data = json.load(f)
#                 return True
#             except Exception as e:
#                 print("Error loading data:", e)
#         return False
    

#     def show_login_page(self):
#         self.update_background('LOGINPAGE')
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#         style = ttk.Style()
#         style.theme_use('clam')
        
#         # Configure colors
#             # Configure styles for frame, labels, buttons, and checkbuttons
#         # Configure styles for frame, labels, buttons, and checkbuttons
#         style.configure('TFrame', background='white')  # Keep frame color for content
#         style.configure('TLabel', background='white', foreground='navy', font=('Arial', 12, 'italic'))  # Update label font
#         style.configure('TButton', background='#C8A0D4', foreground='white', font=('Segoe Script', 12, 'bold'))  # Update button font
#         style.map('TButton', background=[('active', 'dodgerblue')])
#         style.configure('TCheckbutton', background='white', foreground='navy')

#         def check_name(*args):
#             if self.name_entry.get().strip() and age_entry.get().strip():
#                 login_button.config(state=tk.NORMAL)
#             else:
#                 login_button.config(state=tk.DISABLED)

#         def handle_login():
#             name = self.name_entry.get().strip()
#             age_str = age_entry.get().strip()

#             if not age_str.isdigit():
#                 messagebox.showerror("Invalid Input", "Please enter only digits for age.")
#                 return

#             age = int(age_str)
#             if age > 75:
#                 messagebox.showerror("Invalid Age", "Age must be 75 or below.")
#                 return

#             if self.load_data(name):
#                 messagebox.showinfo("Welcome Back", f"Welcome back, {name}!")
#                 self.show_plan_choice_page()
#             else:
#                 self.user_data['name'] = name
#                 self.user_data['age'] = int(age)
#                 # Set age category based on entered age
#                 if self.user_data['age'] <= 25:
#                     self.user_data['age_category'] = '25 and below'
#                 elif 26 <= self.user_data['age'] <= 35:
#                     self.user_data['age_category'] = '26-35'
#                 else:
#                     self.user_data['age_category'] = '36+'
#                 self.show_bmi_page()


#         # Create UI elements
#         login_label = ttk.Label(self.content_frame, text="Welcome to SheFIT!", font=("Georgia", 16, "bold"))
#         name_label = ttk.Label(self.content_frame, text="Enter Your Name: ")
#         self.name_entry = ttk.Entry(self.content_frame)
        

#         age_label = ttk.Label(self.content_frame, text="Enter Your Age: ")
#         age_entry = ttk.Entry(self.content_frame)

#         login_button = ttk.Button(self.content_frame, text="Let's Start", command=handle_login, state=tk.DISABLED)

#         # Layout the widgets
#         login_label.grid(row=0, column=0, columnspan=2, pady=40, padx=20)
#         name_label.grid(row=1, column=0, padx=(0, 10), sticky="e")
#         self.name_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        
#         age_label.grid(row=2, column=0, padx=(0, 10), sticky="e")
#         age_entry.grid(row=2, column=1, pady=10, padx=10, sticky="w")

#         login_button.grid(row=3, column=0, columnspan=2, pady=30)

#         self.content_frame.grid_columnconfigure(0, weight=1)
#         self.content_frame.grid_columnconfigure(1, weight=1)

#         self.name_var = tk.StringVar()
#         self.name_entry.config(textvariable=self.name_var)
#         self.age_var = tk.StringVar()
#         age_entry.config(textvariable=self.age_var)

#         self.name_var.trace("w", check_name)
#         self.age_var.trace("w", check_name)



#     def show_age_page(self):
#         self.update_background('LOGINPAGE')
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#         def calculate_age_category():
#             try:
#                 age = int(age_entry.get())
#                 self.user_data['age'] = age
#                 if age <= 25:
#                     self.user_data['age_category'] = '25 and below'
#                 elif 26 <= age <= 35:
#                     self.user_data['age_category'] = '26-35'
#                 else:
#                     self.user_data['age_category'] = '36+'
#                 self.show_bmi_page()
#             except ValueError:
#                 messagebox.showerror("Invalid Input", "Please enter a valid age.")

#         age_label = ttk.Label(self.content_frame, text="Enter Your Age: ")
#         age_entry = ttk.Entry(self.content_frame)
#         age_button = ttk.Button(self.content_frame, text="Next", command=calculate_age_category)

#         age_label.grid(row=0, column=0, padx=(0, 10), sticky="e")
#         age_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")
#         age_button.grid(row=1, column=0, columnspan=2, pady=30)


#     def show_bmi_page(self):
#         self.update_background('BMIPAGE')
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#         # Configure style
#         style = ttk.Style()
#         style.theme_use('clam')
#         style.configure("Custom.TButton", font=("Serif", 9, "bold"), background="#800080", foreground="black")

#         # Create input fields
#         height_label = ttk.Label(self.content_frame, text="Enter Your Height (cm): ", font=("Serif", 10, "bold"))
#         height_entry = ttk.Entry(self.content_frame)
#         weight_label = ttk.Label(self.content_frame, text="Enter Your Weight (kg): ", font=("Serif", 10, "bold"))
#         weight_entry = ttk.Entry(self.content_frame)
        
#         # Function to calculate BMI
#         def calculate_bmi():
#             try:
#                 height = float(height_entry.get()) / 100  # convert cm to m
#                 weight = float(weight_entry.get())
#                 bmi = weight / (height ** 2)
#                 self.user_data['height'] = height * 100  # store height in cm
#                 self.user_data['weight'] = weight
#                 self.user_data['bmi'] = bmi

#                 # Determine BMI category
#                 if bmi < 18.5:
#                     self.user_data['bmi_category'] = 'Underweight'
#                 elif 18.5 <= bmi < 24.9:
#                     self.user_data['bmi_category'] = 'Normal weight'
#                 elif 25 <= bmi < 29.9:
#                     self.user_data['bmi_category'] = 'Overweight'
#                 else:
#                     self.user_data['bmi_category'] = 'Obesity'

#                 bmi_result_label.config(text=f"BMI: {bmi:.2f} ({self.user_data['bmi_category']})")

#                 next_button = Button(self.content_frame, text="Continue", command=self.show_plan_choice_page, bg="#C8A0D4", fg="black", font=("Serif", 9, "bold"))
#                 # bmi_button = Button(self.content_frame, text="Calculate BMI", command=calculate_bmi, bg="#C8A0D4", fg="black", font=("Serif", 9, "bold"))
#                 next_button.grid(row=4, column=0, columnspan=2, pady=10)

#             except ValueError:
#                 messagebox.showerror("Invalid Input", "Please enter valid height and weight.")

#         bmi_button = Button(self.content_frame, text="Calculate BMI", command=calculate_bmi, bg="#C8A0D4", fg="black", font=("Serif", 9, "bold"))

#         bmi_result_label = ttk.Label(self.content_frame, text="BMI will be displayed here after calculation")

#         height_label.grid(row=0, column=0, padx=(0, 10), sticky="e")
#         height_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")
#         weight_label.grid(row=1, column=0, padx=(0, 10), sticky="e")
#         weight_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w")
#         bmi_button.grid(row=2, column=0, columnspan=2, pady=30)
#         bmi_result_label.grid(row=3, column=0, columnspan=2, pady=10)

#         self.content_frame.place(fill="both", expand=True)  


#     def show_plan_choice_page(self):
#         self.update_background('PLACSPAGE')
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#         style = ttk.Style()
#         style.theme_use('clam')
        
#         # Configure colors
#         style.configure('TFrame', background='white')
#         style.configure('TLabel', background='white', foreground='navy', font=('Arial', 12, 'italic'))
#         style.configure('TButton', background='#C8A0D4', foreground='white', font=('Segoe Script', 12, 'bold'))
#         style.map('TButton', background=[('active', 'dodgerblue')])
#         style.configure('TCheckbutton', background='white', foreground='navy', font=('Helvetica', 10))

#         # Display the welcome message 1
#         welcome_label = ttk.Label(self.content_frame, text=f"Welcome, {self.user_data['name']}!")
#         welcome_label.pack(pady=5)

#         # Display the welcome message 2
#         welcome2_label = ttk.Label(self.content_frame, text="Choose from our tailored options")
#         welcome2_label.pack(pady=10)

#         # Option buttons (using ttk.Button)
#         workout_button = ttk.Button(self.content_frame, text="Workout Plan", command=self.show_workout_plan)
#         diet_button = ttk.Button(self.content_frame, text="Diet Plan", command=self.show_diet_plan)
#         both_button = ttk.Button(self.content_frame, text="Both Workout and Diet", command=self.show_both_plans)

#         workout_button.pack(pady=20)
#         diet_button.pack(pady=20)
#         both_button.pack(pady=20)

#     def show_workout_plan(self):
#         self.user_data['current_plan_type'] = 'workout'
#         self.user_data['current_plan_step'] = 'workout'
#         self.save_data()
#         self.show_plan_page()

#     def show_diet_plan(self):
#         self.user_data['current_plan_type'] = 'diet'
#         self.user_data['current_plan_step'] = 'diet'
#         self.save_data()
#         self.show_plan_page()

#     def show_both_plans(self):
#         self.user_data['current_plan_type'] = 'both'
#         self.user_data['current_plan_step'] = 'workout'  # Start with workout
#         self.save_data()
#         self.show_plan_page()

#     def show_plan_page(self):
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#             # Update background image based on plan type
#         if self.user_data['current_plan_type'] == 'workout':
#             self.update_background('PLAS3PAGEWORKOUT')  # Set background for workout
#         elif self.user_data['current_plan_type'] == 'diet':
#             self.update_background('PLAS3PAGEDIET')  # Set background for diet
#         elif self.user_data['current_plan_type'] == 'both':
#             if self.user_data['current_plan_step'] == 'workout':
#                 self.update_background('PLAS3PAGEWORKOUT')  # Set background for workout
#             else:
#                 self.update_background('PLAS3PAGEDIET')  # Set background for diet

#         tasks = []
#         font = ("Helvetica", 16, "bold")
#         color = "black"

#         if self.user_data['current_plan_type'] == 'workout':
#             current_day = self.user_data['workout_day'] % 7  # Cycle through 1 to 7
#             if current_day == 0:
#                 current_day = 7
#             plan_label = tk.Label(self.content_frame, text=f"Workout Plan for Day {current_day}", font=font, fg=color)
#             plan_details = self.plans['workout'][self.user_data['age_category']][self.user_data['bmi_category']][current_day - 1]
#             tasks = plan_details
#         elif self.user_data['current_plan_type'] == 'diet':
#             current_day = self.user_data['diet_day'] % 7  # Cycle through 1 to 7
#             if current_day == 0:
#                 current_day = 7
#             plan_label = tk.Label(self.content_frame, text=f"Diet Plan for Day {current_day}", font=font, fg=color)
#             plan_details = self.plans['diet'][self.user_data['age_category']][self.user_data['bmi_category']][current_day - 1]
#             tasks = plan_details
#         elif self.user_data['current_plan_type'] == 'both':
#             if self.user_data['current_plan_step'] == 'workout':
#                 plan_label = tk.Label(self.content_frame, text=f"Workout Plan for Day {self.user_data['both_workout_day']}", font=font, fg=color)
#                 plan_details = self.plans['workout'][self.user_data['age_category']][self.user_data['bmi_category']][self.user_data['both_workout_day'] - 1]
#                 tasks = plan_details
#             else:
#                 plan_label = tk.Label(self.content_frame, text=f"Diet Plan for Day {self.user_data['both_diet_day']}", font=font, fg=color)
#                 plan_details = self.plans['diet'][self.user_data['age_category']][self.user_data['bmi_category']][self.user_data['both_diet_day'] - 1]
#                 tasks = plan_details

#         plan_label.pack(pady=20)

#         self.task_vars = []  # List to hold the IntVar for each task checkbox
#         for task in tasks:
#             var = tk.IntVar(value=0)  # 0 for unchecked, 1 for checked
#             self.task_vars.append(var)

#             def on_check(var, task):
#                 if (self.user_data['current_plan_type'] == 'workout' or 
#                     (self.user_data['current_plan_type'] == 'both' and self.user_data['current_plan_step'] == 'workout')):
                    
#                     if var.get() == 1:  # Checkbox checked for workout tasks
#                         # Check if the task is a rest day
#                         if "Rest Day" in task:
#                             # Don't show video prompt for rest day
#                             return
                        
#                         # For non-rest day tasks, show the video prompt
#                         response = messagebox.askyesno("Watch YouTube Video", f"Do you want to watch a video for '{task}'?")
#                         if response:  # User said yes
#                             # Create a button to open the YouTube video
#                             self.open_youtube_video(task)

#             checkbox = tk.Checkbutton(self.content_frame, text=task, variable=var, command=lambda var=var, task=task: on_check(var, task)) ####varshaa's code only added (command=lambda var=var, task=task: on_check(var, task))####
#             checkbox.pack(anchor='w')

#         complete_button = tk.Button(self.content_frame, text="Complete", command=self.complete_plan, bg="#C8A0D4", fg="black", font=("Serif", 9, "bold"))
#         # bmi_button = Button(self.content_frame, text="Calculate BMI", command=calculate_bmi, bg="#C8A0D4", fg="black", font=("Serif", 9, "bold"))
#         complete_button.pack(pady=20)

# ########varshaa's code  from here########
#     def open_youtube_video(self, task):
#         # Define a map of tasks to YouTube video URLs
#         video_links = {
#             "Bodyweight Squats": "https://youtu.be/l83R5PblSMA?si=glaQzD1vzpt3p2YO",
#             "Push-ups": "https://youtube.com/shorts/Dq8ErSsp9Xc?si=wst0t_4SkZcUSgEN",
#             "Yoga (At Home)": "https://www.youtube.com/watch?v=v7AYKMP6rOE",
#             "Jumping Jacks": "https://youtube.com/shorts/7Pxr4xOrhNk?si=_5jGieF8-8Xed42l",
#             "Pilates (At Home)": "https://youtu.be/o2C8U1cNPJs?si=e8m29e0wmYHPIYl_",
#             "Light Strength Training": "https://youtu.be/66kfC7qEJTQ?si=4mxtDtxQV2wcbL9P",
#             "Brisk Walking in Place": "https://youtu.be/tVpUCkMLgms?si=WiavH-2ud8JApna7",
#             "Core Exercises": "https://youtu.be/He6e8LqmvhQ?si=KRiM5n4-fdZh_X23",
#             "Mountain Climbers": "https://youtu.be/KH2u4F_MWZc?si=E2qK7PXH7j61E-xf",
#             "Running in Place": "https://youtu.be/5umbf4ps0GQ?si=Oh1lrupoVijPlmKj",
#             "HIIT (At Home)": "https://youtu.be/jeLxN-wt7jY?si=pWiVys0xKM399RLL",
#             "Strength Training (Bodyweight)": "https://youtu.be/66kfC7qEJTQ?si=4mxtDtxQV2wcbL9P",
#             "Burpees": "https://youtube.com/shorts/bRvW5keP4r8?si=GHJaT9QS9fkci7LZ",
#             "Cycling (Stationary)": "https://youtu.be/-juKjold5cc?si=NY-icye8nPAMZcLT",
#             "Dance Workout (At Home)": "https://youtu.be/rvu7iNIrNa8?si=HCZpYYhoGkqbT0nl",
#             "Swimming Simulation (Arm Exercises)": "https://youtu.be/XmFQE-PsBl0?si=T-rwJ_xj_ptVTbWK",
#             "Kickboxing (At Home)": "https://youtu.be/XOSJdJbkYkM?si=0ajRAF68ug9wBXaZ",
#             "Bodyweight Exercises": "https://youtu.be/ZnoJ4ZmdPcA?si=Bc61fu_akcrmz-l4",
#             "Circuit Training (At Home)": "https://youtube.com/shorts/W80p2SkEJTI?si=2_aXuuVcrZvcJgN6",
#             "Jump Rope": "https://youtu.be/qNGJDb3pdc0?si=5OR4J9WRO_XHuJcS",
#             "Core Strengthening": "https://youtu.be/He6e8LqmvhQ?si=KRiM5n4-fdZh_X23",
#             "Bodyweight Strength Training": "https://youtu.be/0hYDDsRjwks?si=K8ctAaQBco2ZJwRH",
#             "High Knees": "https://youtube.com/shorts/x2jTlPupfPs?si=A69jyYn_qGQQ88P2",
#             "Bodyweight Lunges": "https://youtube.com/shorts/FdPl7f69_30?si=MFxkXaNTRzm6oIle",
#             "Shadow Boxing": "https://youtu.be/XOSJdJbkYkM?si=0ajRAF68ug9wBXaZ",
#             "Stretching": "https://youtu.be/MExM0W5kzqo?si=Ls7RBcF6cm1Vb_kb",
#             "Light Cardio": "https://youtu.be/tGrVHoo2jHo?si=iSsIoagJmh4BHCsm",
#             "Light Aerobics": "https://youtu.be/WTUruNwUMFI?si=M70mapQzNu1lHh69",
#             "Low-Impact Cardio": "https://youtu.be/MvgTAzg_UcM?si=a2Y2xiAt89KAqKkU",
#             "Chair Exercises": "https://youtu.be/ayA9EyY-wOc?si=fXXkJWPpuWwLZtvT",
#             "Resistance Band Workouts": "https://youtu.be/eYV810veFN4?si=U_w4JwBgEXMk75-G",
#             "Gentle Stretching": "https://youtu.be/MExM0W5kzqo?si=Ls7RBcF6cm1Vb_kb",
#             "Seated Exercises": "https://youtu.be/RduFF1wniHY?si=yQwbcPrtXV5M0eGd",
#             "Gentle Yoga (At Home)": "https://youtu.be/FvaE0KofQEA?si=nsa7vHUWffeW5pU-",
#             "Walking in Place": "https://youtu.be/tVpUCkMLgms?si=WiavH-2ud8JApna7",
#             "Chair Yoga": "https://youtu.be/V_et6TI2zN4?si=RyMGLbUsX8_2qX_m",
#             "Light Walking in Place": "https://youtu.be/tVpUCkMLgms?si=WiavH-2ud8JApna7",
#             "Gentle Aerobics": "https://youtu.be/WTUruNwUMFI?si=M70mapQzNu1lHh69",
#             "Light Weight Training": "https://youtu.be/tj0o8aH9vJw?si=o5d7zazgSgfbp0Lj",
#             "Gentle Dance Workout": "https://youtu.be/XnPw82kImXI?si=cauQULkNqjK2LRTa",
#             "Dance Workout": "https://youtu.be/bqVBMv_nqJ4?si=-0fED7QLEiXEPoy2",
#             "Weight Training (At Home)": "https://youtu.be/OmLx8tmaQ-4?si=YKJThUMmav-OkwlX",
#         }

#         # Open the corresponding YouTube video
#         if self.user_data['current_plan_type'] == 'workout' and task in video_links:
#             link = video_links[task]
#             webbrowser.open(link)
#         elif self.user_data['current_plan_type'] == 'both' and task in video_links:
#             link = video_links[task]
#             webbrowser.open(link)
#      ########varshaa's code until here########

#     def complete_plan(self):
#         all_completed = all(var.get() == 1 for var in self.task_vars)

#         if all_completed:
#             if self.user_data['current_plan_type'] == 'workout':
#                 self.user_data['completed_workout'] = True
#                 self.user_data['workout_day'] += 1
#                 self.save_data()      
#                 self.planner_page()  # Directly go to planner_page after workout plan completion  ########varshaa's code########

#             elif self.user_data['current_plan_type'] == 'diet':
#                 self.user_data['completed_diet'] = True
#                 self.user_data['diet_day'] += 1
#                 self.save_data() 
#                 self.planner_page()  # Directly go to planner_page after diet plan completion  ########varshaa's code########

#             elif self.user_data['current_plan_type'] == 'both':
#                 if self.user_data['current_plan_step'] == 'workout':
#                     self.user_data['completed_workout'] = True
#                     self.user_data['both_workout_day'] += 1
#                     self.user_data['current_plan_step'] = 'diet'  # Switch to diet after completing workout
#                     self.save_data()  
#                     messagebox.showinfo("Workout Complete", "You have completed your workout. Now proceed to your diet plan.")  ########varshaa's code########
#                     self.show_plan_page()  # Reload the page to show diet plan    

#                 elif self.user_data['current_plan_step'] == 'diet':
#                     self.user_data['completed_diet'] = True
#                     self.user_data['both_diet_day'] += 1
#                     self.user_data['current_plan_step'] = 'workout'  # Reset to workout for next cycle
#                     self.save_data() 
#                     messagebox.showinfo("Diet Complete", "You have completed your diet plan. Now returning to the planner.")  ########varshaa's code########
#                     self.planner_page()  # Proceed to the planner after completing both plans    ########varshaa's code########

#         else:
#             messagebox.showwarning("Incomplete Tasks", "Please complete all tasks before proceeding.")


#     ########varshaa's code########
#     def create_treeview(self, parent, columns):
#         style = ttk.Style()
#         style.theme_use("clam")
        
#         style.configure("Treeview",background="#f0f0f0",foreground="black",rowheight=60, fieldbackground="#f0f0f0")
#         style.configure("Treeview.Heading",background="#4a7a8c",foreground="white",relief="flat")
#         style.map("Treeview.Heading",relief=[('active', 'groove'), ('pressed', 'sunken')])

#         tree = ttk.Treeview(parent, columns=columns, show="headings", height=7)
        
#         # Adjust column widths
#         tree.heading("Day", text="Day")
#         tree.column("Day", width=100, anchor="center")
        
#         tree.heading("Workout", text="Workout")
#         tree.column("Workout", width=500, anchor="w")  # Significantly increased width

#         return tree

#     def show_treeview(self):
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#         center_frame = ttk.Frame(self.content_frame)
#         center_frame.pack(expand=True, fill="both", padx=20, pady=20)

#         columns = ("Day", "Workout")
#         tree = self.create_treeview(center_frame, columns)

#         style = ttk.Style()
#         style.configure("Vertical.TScrollbar", gripcount=0, 
#                         background="#4a7a8c", darkcolor="#4a7a8c", lightcolor="#4a7a8c",
#                         troughcolor="#f0f0f0", bordercolor="#4a7a8c", arrowcolor="white")

#         scrollbar = ttk.Scrollbar(center_frame, orient="vertical", command=tree.yview, style="Vertical.TScrollbar")
#         tree.configure(yscrollcommand=scrollbar.set)

#         tree.pack(side="left", expand=True, fill="both")
#         scrollbar.pack(side="right", fill="y")

#         workout_plan = self.plans['workout'][self.user_data['age_category']][self.user_data['bmi_category']]
#         for day in range(7):
#             workout = workout_plan[day] if day < len(workout_plan) else "Rest Day"
#             tree.insert("", "end", values=(f"Day {day + 1}", workout), tags=('oddrow' if day % 2 else 'evenrow',))

#         tree.tag_configure('oddrow', background='#e6e6e6')
#         tree.tag_configure('evenrow', background='#ffffff')

#         style.configure("TButton", padding=6, relief="flat", background="#4a7a8c", foreground="white")
#         style.map("TButton", background=[('active', '#5c8d9e')])
        
#         back_button = ttk.Button(self.content_frame, text="Back to Planner", command=self.show_plan_choice_page, style="TButton")
#         back_button.pack(pady=10)

#     def planner_page(self):
#         label1 = ttk.Label(self.content_frame, text="Keep yourself updated")
#         label1.pack(pady=5)
#         treeview_button = ttk.Button(self.content_frame, text="View Workout Plan", command=self.show_treeview)
#         treeview_button.pack(pady=10)
#         backbutton=ttk.Button(self.content_frame, text="Back to Plan", command=self.show_plan_choice_page)
#         backbutton.pack()
        
# ########varshaa's code########
#     def create_widgets(self):
#         self.content_frame = ttk.Frame(self.container)
#         self.content_frame.pack(fill="both", expand=True)
        
#         # Example button to go back to the Planner page
#         back_button = ttk.Button(self.content_frame, text="Back to Planner", command=self.planner_page)
#         back_button.pack(pady=20)
    
        
# ########varshaa's code########
#     def create_workout_frame(self):
#         workout_plan = self.user_data.get('workout_plan', [])

#         if not workout_plan:
#             messagebox.showerror("Error", "No workout plan found. Please assign a workout plan.")
#             return

    
#         workout_day = self.user_data.get('workout_day', 1) - 1  #for 0-based index
#         if workout_day < len(workout_plan):
#             exercises = workout_plan[workout_day]  # Get exercises for the current day
#         else:
#             exercises = ["Rest Day"]  # Default message if no exercises are available

#         # comma-separated string of exercises
#         exercise_string = ", ".join(exercises)

#     def show_summary_page(self):
#         self.update_background('SUMRPAGE')
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#         style = ttk.Style()
#         style.theme_use('clam')
        
#         # Configure colors
#         style.configure('TFrame', background='white')
#         style.configure('TLabelframe', background='white', bordercolor='#C8A0D4')
#         style.configure('TLabelframe.Label', background='white', foreground='#C8A0D4', font=('Helvetica', 10, 'bold'))
#         style.configure('TLabel', background='white', foreground='navy')
#         style.configure('TButton', background='#C8A0D4', foreground='white', font=('Helvetica', 10, 'bold'))
#         style.map('TButton', background=[('active', 'dodgerblue')])
        
#         # Configure Treeview colors
#         style.configure('Treeview', background='white', fieldbackground='white', foreground='navy')
#         style.configure('Treeview.Heading', background='#C8A0D4', foreground='white', font=('Helvetica', 9, 'bold'))
#         style.map('Treeview', background=[('selected', 'lightblue')], foreground=[('selected', 'navy')])


#         main_frame = ttk.Frame(self.content_frame)
#         main_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)

#         title_label = ttk.Label(main_frame, text="Your Fitness Summary")
#         title_label.pack(pady=(0, 20))

#         # Top section: BMI and Goal Summary
#         top_frame = ttk.Frame(main_frame)
#         top_frame.pack(fill=tk.X, pady=(0, 20))

#         # BMI Information
#         bmi_frame = ttk.LabelFrame(top_frame, text="BMI Information")
#         bmi_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
#         ttk.Label(bmi_frame, text=f"BMI: {self.user_data['bmi']:.2f}").pack(pady=5)
#         ttk.Label(bmi_frame, text=f"Category: {self.user_data['bmi_category']}").pack(pady=5)

#         # Goal Summary
#         goal_frame = ttk.LabelFrame(top_frame, text="Goal Summary")
#         goal_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
#         ttk.Label(goal_frame, text=f"Workouts Completed: {self.user_data['workout_day'] - 1}/7").pack(pady=5)
#         ttk.Label(goal_frame, text=f"Diet Plan Followed: {self.user_data['diet_day'] - 1}/7").pack(pady=5)

#         # Middle section: Weekly Plan
#         plan_frame = ttk.LabelFrame(main_frame, text="Weekly Meal and Workout Plan")
#         plan_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))

#         plan_tree = ttk.Treeview(plan_frame, columns=("Day", "Meal", "Workout"), show="headings", height=7)
#         plan_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         for col in ("Day", "Meal", "Workout"):
#             plan_tree.heading(col, text=col)
#             plan_tree.column(col, width=100)

#         scrollbar = ttk.Scrollbar(plan_frame, orient="vertical", command=plan_tree.yview)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#         plan_tree.configure(yscrollcommand=scrollbar.set)

#         # Populate the treeview with completed workout and diet data
#         workout_days = max(self.user_data['workout_day'], self.user_data['both_workout_day'])
#         diet_days = max(self.user_data['diet_day'], self.user_data['both_diet_day'])
#         max_days = max(workout_days, diet_days)

#         for i in range(max_days):
#             day = i + 1
#             workout = "Completed" if day < workout_days else "Not completed"
#             diet = "Followed" if day < diet_days else "Not followed"
#             plan_tree.insert("", "end", values=(f"Day {day}", diet, workout))

#         # Bottom section: Motivation and Recommendations
#         bottom_frame = ttk.Frame(main_frame)
#         bottom_frame.pack(fill=tk.X)

#         # Motivational Quote
#         quote_frame = ttk.LabelFrame(bottom_frame, text="Your Daily Motivation")
#         quote_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
#         quote_label = ttk.Label(quote_frame, text="Stay committed to your decisions, but flexible in your approach.", wraplength=180)
#         quote_label.pack(pady=10, padx=10)

#         # Recommendations
#         rec_frame = ttk.LabelFrame(bottom_frame, text="Recommendations")
#         rec_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
#         ttk.Label(rec_frame, text="Daily Calorie Intake: 2000").pack(pady=5)
#         ttk.Label(rec_frame, text="Daily Steps: 7K-10K").pack(pady=5)

#         # Back button
#         back_button = ttk.Button(main_frame, text="Back to Plan Choice", command=self.show_plan_choice_page)
#         back_button.pack(pady=(20, 0))

# if __name__ == "__main__":
#     app = FitnessApp()
#     app.mainloop()