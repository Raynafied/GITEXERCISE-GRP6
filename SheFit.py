#FINAL COMPLETED VERSION 
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import random
import webbrowser 
from PIL import Image, ImageTk
from tkinter import Button
import logging
#import shelve

class FitnessApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.title('Fitness App')
        self.current_bg_key = 'welcome'  # Store the current background key
        
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
        self.create_menu_bar()

        # Base path for images
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.images_path = os.path.join(self.base_path, "images")  
        
        # Load images
        self.bg_images = self.load_images()

        # Canvas for background image
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Set default background
        self.bg_image = None
        self.bg_image_on_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.bg_image)
        self.content_frame = ttk.Frame(self.canvas, style='Transparent.TFrame', width=700, height=500)  # Increase width and height
        self.canvas_window = self.canvas.create_window(450, 300, anchor='center', window=self.content_frame) 

        self.bind("<Configure>", self.resize_bg_image)
    
                # Create a style object
        self.style = ttk.Style(self)
        self.configure_button_style()
        self.configure_label_style()
    
        self.welcome_login_page()

    def configure_label_style(self):
        self.style.configure("Custom.TLabel", 
                             font=("Comic Sans MS", 14), 
                             foreground="#4A0E4E",  # Dark purple for text
                             padding=(10, 5)
                             )

    def configure_button_style(self):
        self.style.configure("Custom.TButton", 
                            font=("Segoe Script", 12, "bold"),
                            foreground="#4A0E4E",  # Dark purple for text
                            background="#F0F0F0",  # Light gray for button background
                            borderwidth=1,
                            relief="solid",
                            padding=(10, 5)
                            )
        self.style.map("Custom.TButton", 
                    background=[('active', "#E0E0E0")],  # Slightly darker when active
                    relief=[('pressed', 'sunken')])

    def load_images(self):
        image_keys = ['welcome', 'LOGINPAGE', 'BMIPAGE', 'PLACSPAGE', 'PLAS3PAGEWORKOUT', 'PLAS3PAGEDIET', 'SUMRPAGE']
        images = {}
        for key in image_keys:
            try:
                image_path = os.path.join(self.images_path, f"{key}.png")
                images[key] = Image.open(image_path)
            except FileNotFoundError:
                logging.warning(f"Image file not found: {image_path}")
                images[key] = None  # Set to None if image is not found
        return images

    def update_background(self, image_key):
        self.current_bg_key = image_key  # Update the current background key
        try:
            if image_key in self.bg_images and self.bg_images[image_key] is not None:
                bg = self.bg_images[image_key].resize((self.winfo_width(), self.winfo_height()), Image.LANCZOS)
                self.bg_image = ImageTk.PhotoImage(bg)
                self.canvas.itemconfig(self.bg_image_on_canvas, image=self.bg_image)
            else:
                logging.warning(f"Image for key '{image_key}' not found or is None.")
                # Set a default background color
                self.canvas.configure(bg='light gray')
        except Exception as e:
            logging.error(f"Error updating background: {e}")
            # Set a default background color
            self.canvas.configure(bg='light gray')

    def resize_bg_image(self, event=None):
        new_width = self.winfo_width()
        new_height = self.winfo_height()
        self.update_background(self.current_bg_key)
        self.canvas.coords(self.canvas_window, new_width/2, new_height/2)


        
    def welcome_login_page(self):
        self.update_background('welcome')
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        welcome_label = ttk.Label(self.content_frame, text="Welcome to the SheFIT!",font=("Courier", 20, "bold"), style="Custom.TLabel") #need to add colour here foreground="#4A0E4E"
        welcome_label.pack(pady=20)

        description_label = ttk.Label(self.content_frame, text="Unlock your fitness journey with SheFIT!\n" \
            "Custom workout and meal plans tailored for women.\n" \
            "Choose from engaging workout video guides \n"
            "Take one step at a time with 7-day challenges and transform your lifestyle today! 💪✨",
            font=("Courier", 12, "italic"),wraplength=400, justify="center", style="Custom.TLabel")
        description_label.pack(pady=10)

        start_button = ttk.Button(self.content_frame, text="Let's Get Started", command=self.show_login_page, style="Custom.TButton")
        start_button.pack(pady=20)

        

    def create_menu_bar(self):
        menubar = tk.Menu(self)
        
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Change User", command=self.change_user)
        settings_menu.add_command(label="Change Plan", command=self.change_plan)
        settings_menu.add_command(label="Edit User Data", command=self.edit_user_data)
        settings_menu.add_command(label="View My Summary Chart", command=self.show_summary_page)
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
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        def save_changes():
            try:
                self.user_data['weight'] = float(weight_entry.get())
                self.user_data['height'] = float(height_entry.get())
                self.user_data['age'] = int(age_entry.get())
                
                # Recalculate BMI and age category
                height_m = self.user_data['height'] / 100  # Convert cm to m
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


        label = ttk.Label(self.content_frame, text="Edit Your Data \n" \
                          " \n" \
                           "Please update your personal information below to ensure we provide you with the \n"
                           "best fitness recommendations tailored to your goals!", justify="center", style="Custom.TLabel")
        label.pack(pady=(40, 10))

        weight_label = ttk.Label(self.content_frame, text="Weight (kg): ", style="Custom.TLabel")
        weight_label.pack(pady=(10, 5))
        weight_entry = ttk.Entry(self.content_frame)
        weight_entry.insert(0, self.user_data['weight'])  # pre-fill with current weight
        weight_entry.pack(pady=(5, 10))

        height_label = ttk.Label(self.content_frame, text="Height (cm): ", style="Custom.TLabel")
        height_label.pack(pady=(10, 5))
        height_entry = ttk.Entry(self.content_frame)
        height_entry.insert(0, self.user_data['height'])  # pre-fill with current height
        height_entry.pack(pady=(5, 10))

        age_label = ttk.Label(self.content_frame, text="Age: ", style="Custom.TLabel")
        age_label.pack(pady=(10, 5))
        age_entry = ttk.Entry(self.content_frame)
        age_entry.insert(0, self.user_data['age'])  # pre-fill with current age
        age_entry.pack(pady=(5, 10))

        bmi_result_label = ttk.Label(self.content_frame, text="", style="Custom.TLabel")
        bmi_result_label.pack(pady=(5, 10))

        save_button = ttk.Button(self.content_frame, text="Save Changes", command=save_changes, style="Custom.TButton")
        save_button.pack(pady=(10, 40))


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
            for widget in self.content_frame.winfo_children():
                widget.destroy()

            label = ttk.Label(self.content_frame, text="Select a New Plan \n"
                              f"Ready to switch things up, {self.user_data['name']}? Choose one of the options below to explore a new path on your fitness journey! \n"
                              "Whether you're looking to focus on workouts, diets, or both, we've got tailored plans just for you!",justify="center", style="Custom.TLabel")
            label.pack(pady=20)

            workout_button = ttk.Button(self.content_frame, text="Workout Plan", command=self.show_workout_plan, style="Custom.TButton")
            diet_button = ttk.Button(self.content_frame, text="Diet Plan", command=self.show_diet_plan, style="Custom.TButton")
            both_button = ttk.Button(self.content_frame, text="Both Workout and Diet", command=self.show_both_plans, style="Custom.TButton")

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
        self.update_background('LOGINPAGE')
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        def check_name(*args):
            if self.name_entry.get().strip() and age_entry.get().strip():
                login_button.config(state=tk.NORMAL)
            else:
                login_button.config(state=tk.DISABLED)

        def handle_login():
            name = self.name_entry.get().strip()
            age_str = age_entry.get().strip()

            if not age_str.isdigit():
                messagebox.showerror("Invalid Input", "Please enter only digits for age.")
                return

            age = int(age_str)
            if age > 75:
                messagebox.showerror("Invalid Age", "Age must be 75 or below.")
                return

            if self.load_data(name):
                messagebox.showinfo("Welcome Back", f"Welcome back, {name}!")
                self.show_plan_choice_page()
            else:
                self.user_data['name'] = name
                self.user_data['age'] = int(age)
                # Set age category based on entered age
                if self.user_data['age'] <= 25:
                    self.user_data['age_category'] = '25 and below'
                elif 26 <= self.user_data['age'] <= 35:
                    self.user_data['age_category'] = '26-35'
                else:
                    self.user_data['age_category'] = '36+'
                self.show_bmi_page()

        login_label = ttk.Label(self.content_frame, text="Welcome Gorgeous!  \n" \
                                 "Please enter your name and age to start your journey toward a healthier you!",justify="center", style="Custom.TLabel")
        name_label = ttk.Label(self.content_frame, text="Enter Your Name: ", style="Custom.TLabel")
        self.name_entry = ttk.Entry(self.content_frame)

        age_label = ttk.Label(self.content_frame, text="Enter Your Age: ", style="Custom.TLabel")
        age_entry = ttk.Entry(self.content_frame)
        
        login_button = ttk.Button(self.content_frame, text="Let's Start", command=handle_login, state=tk.DISABLED, style="Custom.TButton")

        login_label.grid(row=0, column=0, columnspan=2, pady=40, padx=20)
        name_label.grid(row=1, column=0, padx=(0, 10), sticky="e")
        self.name_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        
        age_label.grid(row=2, column=0, padx=(0, 10), sticky="e")
        age_entry.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        login_button.grid(row=3, column=0, columnspan=2, pady=30)

        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)

        self.name_var = tk.StringVar()
        self.name_entry.config(textvariable=self.name_var)
        self.age_var = tk.StringVar()
        age_entry.config(textvariable=self.age_var)

        self.name_var.trace("w", check_name)
        self.age_var.trace("w", check_name)



    def show_age_page(self):
        self.update_background('LOGINPAGE')
        for widget in self.content_frame.winfo_children():
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

        age_label = ttk.Label(self.content_frame, text="Enter Your Age: ", style="Custom.TLabel")
        age_entry = ttk.Entry(self.content_frame)
        age_button = ttk.Button(self.content_frame, text="Next", command=calculate_age_category, style="Custom.TButton")

        age_label.grid(row=0, column=0, padx=(0, 10), sticky="e")
        age_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")
        age_button.grid(row=1, column=0, columnspan=2, pady=30)




    def show_bmi_page(self):
        self.update_background('BMIPAGE')
        for widget in self.content_frame.winfo_children():
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

                bmi_result_label.config(text=f"BMI: {bmi:.2f} ({self.user_data['bmi_category']})")

                next_button = ttk.Button(self.content_frame, text="Continue", command=self.show_plan_choice_page, style="Custom.TButton")
                next_button.grid(row=4, column=0, columnspan=2, pady=10)

            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid height and weight.")

        height_label = ttk.Label(self.content_frame, text="Enter Your Height (cm): ", style="Custom.TLabel")
        height_entry = ttk.Entry(self.content_frame)
        weight_label = ttk.Label(self.content_frame, text="Enter Your Weight (kg): ", style="Custom.TLabel")
        weight_entry = ttk.Entry(self.content_frame)
        bmi_button = ttk.Button(self.content_frame, text="Calculate BMI", command=calculate_bmi, style="Custom.TButton")

        bmi_result_label = ttk.Label(self.content_frame, text="BMI will be displayed here after calculation")

        height_label.grid(row=0, column=0, padx=(30, 10), sticky="e")
        height_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")
        weight_label.grid(row=1, column=0, padx=(0, 10), sticky="e")
        weight_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        bmi_button.grid(row=2, column=0, columnspan=2, pady=30)

        bmi_result_label.grid(row=3, column=0, columnspan=2, pady=10)




    def show_plan_choice_page(self):
        self.update_background('PLACSPAGE')
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Display the welcome message 1
        welcome_label = ttk.Label(self.content_frame, text=f"Hey, {self.user_data['name']}!", style="Custom.TLabel")
        welcome_label.pack(pady=5)

        # Display the welcome message 2
        welcome2_label = ttk.Label(self.content_frame, text=f"Embark on your personalized fitness journey, {self.user_data['name']}! \n" \
                                   " Select one of the tailored options below to begin your transformation!",justify="center", style="Custom.TLabel")
        welcome2_label.pack(pady=10)

        # Option buttons (using ttk.Button)
        workout_button = ttk.Button(self.content_frame, text="Workout Plan", command=self.show_workout_plan, style="Custom.TButton")
        diet_button = ttk.Button(self.content_frame, text="Diet Plan", command=self.show_diet_plan, style="Custom.TButton")
        both_button = ttk.Button(self.content_frame, text="Both Workout and Diet", command=self.show_both_plans, style="Custom.TButton")

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
        for widget in self.content_frame.winfo_children():
            widget.destroy()

            # Update background image based on plan type
        if self.user_data['current_plan_type'] == 'workout':
            self.update_background('PLAS3PAGEWORKOUT')  # Set background for workout
        elif self.user_data['current_plan_type'] == 'diet':
            self.update_background('PLAS3PAGEDIET')  # Set background for diet
        elif self.user_data['current_plan_type'] == 'both':
            if self.user_data['current_plan_step'] == 'workout':
                self.update_background('PLAS3PAGEWORKOUT')  # Set background for workout
            else:
                self.update_background('PLAS3PAGEDIET')  # Set background for diet

        tasks = []
        # font = ("Helvetica", 16, "bold")
        # color = "black"

        if self.user_data['current_plan_type'] == 'workout':
            current_day = self.user_data['workout_day'] % 7  # Cycle through 1 to 7
            if current_day == 0:
                current_day = 7
            plan_label = ttk.Label(self.content_frame, text=f"Workout Plan - Day {current_day} \n "
                                   f"Get ready to crush your goals with your Workout Plan for Day {current_day}! \n"
                                   "Let's keep pushing your limits and make every rep count! \n"
                                   ,justify="center", style="Custom.TLabel")
            plan_details = self.plans['workout'][self.user_data['age_category']][self.user_data['bmi_category']][current_day - 1]
            tasks = plan_details
        elif self.user_data['current_plan_type'] == 'diet':
            current_day = self.user_data['diet_day'] % 7  # Cycle through 1 to 7
            if current_day == 0:
                current_day = 7
            plan_label = ttk.Label(self.content_frame, text=f"Diet Plan - Day {current_day} \n"
                                   f"Nourish your body and fuel your journey with your Diet Plan for Day {current_day}! \n"
                                   "Each meal is designed to support your transformation and keep you energized!"
                                   , style="Custom.TLabel")
            plan_details = self.plans['diet'][self.user_data['age_category']][self.user_data['bmi_category']][current_day - 1]
            tasks = plan_details
        elif self.user_data['current_plan_type'] == 'both':
            if self.user_data['current_plan_step'] == 'workout':
                plan_label = ttk.Label(self.content_frame, text=f"Workout Plan for Day {self.user_data['both_workout_day']}", style="Custom.TLabel")
                plan_details = self.plans['workout'][self.user_data['age_category']][self.user_data['bmi_category']][self.user_data['both_workout_day'] - 1]
                tasks = plan_details
            else:
                plan_label = ttk.Label(self.content_frame, text=f"Diet Plan for Day {self.user_data['both_diet_day']}", style="Custom.TLabel")
                plan_details = self.plans['diet'][self.user_data['age_category']][self.user_data['bmi_category']][self.user_data['both_diet_day'] - 1]
                tasks = plan_details

        plan_label.pack(pady=20)

        self.task_vars = []  # List to hold the IntVar for each task checkbox
        for task in tasks:
            var = tk.IntVar(value=0)  # 0 for unchecked, 1 for checked
            self.task_vars.append(var)

            def on_check(var, task):
                if (self.user_data['current_plan_type'] == 'workout' or 
                    (self.user_data['current_plan_type'] == 'both' and self.user_data['current_plan_step'] == 'workout')):
                    
                    if var.get() == 1:  # Checkbox checked for workout tasks
                        # Check if the task is a rest day
                        if "Rest Day" in task:
                            # Don't show video prompt for rest day
                            return
                        
                        # For non-rest day tasks, show the video prompt
                        response = messagebox.askyesno("Watch YouTube Video", f"Do you want to watch a video for '{task}'?")
                        if response:  # User said yes
                            # Create a button to open the YouTube video
                            self.open_youtube_video(task)

            checkbox = tk.Checkbutton(self.content_frame, text=task, variable=var, command=lambda var=var, task=task: on_check(var, task)) ####varshaa's code only added (command=lambda var=var, task=task: on_check(var, task))####
            checkbox.pack(anchor='w')

        complete_button = ttk.Button(self.content_frame, text="Complete", command=self.complete_plan, style="Custom.TButton")
        complete_button.pack(pady=20)

########varshaa's code  from here########
    def open_youtube_video(self, task):
        # Define a map of tasks to YouTube video URLs
        video_links = {
            "Bodyweight Squats": "https://youtu.be/l83R5PblSMA?si=glaQzD1vzpt3p2YO",
            "Push-ups": "https://youtube.com/shorts/Dq8ErSsp9Xc?si=wst0t_4SkZcUSgEN",
            "Yoga (At Home)": "https://www.youtube.com/watch?v=v7AYKMP6rOE",
            "Jumping Jacks": "https://youtube.com/shorts/7Pxr4xOrhNk?si=_5jGieF8-8Xed42l",
            "Pilates (At Home)": "https://youtu.be/o2C8U1cNPJs?si=e8m29e0wmYHPIYl_",
            "Light Strength Training": "https://youtu.be/66kfC7qEJTQ?si=4mxtDtxQV2wcbL9P",
            "Brisk Walking in Place": "https://youtu.be/tVpUCkMLgms?si=WiavH-2ud8JApna7",
            "Core Exercises": "https://youtu.be/He6e8LqmvhQ?si=KRiM5n4-fdZh_X23",
            "Mountain Climbers": "https://youtu.be/KH2u4F_MWZc?si=E2qK7PXH7j61E-xf",
            "Running in Place": "https://youtu.be/5umbf4ps0GQ?si=Oh1lrupoVijPlmKj",
            "HIIT (At Home)": "https://youtu.be/jeLxN-wt7jY?si=pWiVys0xKM399RLL",
            "Strength Training (Bodyweight)": "https://youtu.be/66kfC7qEJTQ?si=4mxtDtxQV2wcbL9P",
            "Burpees": "https://youtube.com/shorts/bRvW5keP4r8?si=GHJaT9QS9fkci7LZ",
            "Cycling (Stationary)": "https://youtu.be/-juKjold5cc?si=NY-icye8nPAMZcLT",
            "Dance Workout (At Home)": "https://youtu.be/rvu7iNIrNa8?si=HCZpYYhoGkqbT0nl",
            "Swimming Simulation (Arm Exercises)": "https://youtu.be/XmFQE-PsBl0?si=T-rwJ_xj_ptVTbWK",
            "Kickboxing (At Home)": "https://youtu.be/XOSJdJbkYkM?si=0ajRAF68ug9wBXaZ",
            "Bodyweight Exercises": "https://youtu.be/ZnoJ4ZmdPcA?si=Bc61fu_akcrmz-l4",
            "Circuit Training (At Home)": "https://youtube.com/shorts/W80p2SkEJTI?si=2_aXuuVcrZvcJgN6",
            "Jump Rope": "https://youtu.be/qNGJDb3pdc0?si=5OR4J9WRO_XHuJcS",
            "Core Strengthening": "https://youtu.be/He6e8LqmvhQ?si=KRiM5n4-fdZh_X23",
            "Bodyweight Strength Training": "https://youtu.be/0hYDDsRjwks?si=K8ctAaQBco2ZJwRH",
            "High Knees": "https://youtube.com/shorts/x2jTlPupfPs?si=A69jyYn_qGQQ88P2",
            "Bodyweight Lunges": "https://youtube.com/shorts/FdPl7f69_30?si=MFxkXaNTRzm6oIle",
            "Shadow Boxing": "https://youtu.be/XOSJdJbkYkM?si=0ajRAF68ug9wBXaZ",
            "Stretching": "https://youtu.be/MExM0W5kzqo?si=Ls7RBcF6cm1Vb_kb",
            "Light Cardio": "https://youtu.be/tGrVHoo2jHo?si=iSsIoagJmh4BHCsm",
            "Light Aerobics": "https://youtu.be/WTUruNwUMFI?si=M70mapQzNu1lHh69",
            "Low-Impact Cardio": "https://youtu.be/MvgTAzg_UcM?si=a2Y2xiAt89KAqKkU",
            "Chair Exercises": "https://youtu.be/ayA9EyY-wOc?si=fXXkJWPpuWwLZtvT",
            "Resistance Band Workouts": "https://youtu.be/eYV810veFN4?si=U_w4JwBgEXMk75-G",
            "Gentle Stretching": "https://youtu.be/MExM0W5kzqo?si=Ls7RBcF6cm1Vb_kb",
            "Seated Exercises": "https://youtu.be/RduFF1wniHY?si=yQwbcPrtXV5M0eGd",
            "Gentle Yoga (At Home)": "https://youtu.be/FvaE0KofQEA?si=nsa7vHUWffeW5pU-",
            "Walking in Place": "https://youtu.be/tVpUCkMLgms?si=WiavH-2ud8JApna7",
            "Chair Yoga": "https://youtu.be/V_et6TI2zN4?si=RyMGLbUsX8_2qX_m",
            "Light Walking in Place": "https://youtu.be/tVpUCkMLgms?si=WiavH-2ud8JApna7",
            "Gentle Aerobics": "https://youtu.be/WTUruNwUMFI?si=M70mapQzNu1lHh69",
            "Light Weight Training": "https://youtu.be/tj0o8aH9vJw?si=o5d7zazgSgfbp0Lj",
            "Gentle Dance Workout": "https://youtu.be/XnPw82kImXI?si=cauQULkNqjK2LRTa",
            "Dance Workout": "https://youtu.be/bqVBMv_nqJ4?si=-0fED7QLEiXEPoy2",
            "Weight Training (At Home)": "https://youtu.be/OmLx8tmaQ-4?si=YKJThUMmav-OkwlX",
        }

        # Open the corresponding YouTube video
        if self.user_data['current_plan_type'] == 'workout' and task in video_links:
            link = video_links[task]
            webbrowser.open(link)
        elif self.user_data['current_plan_type'] == 'both' and task in video_links:
            link = video_links[task]
            webbrowser.open(link)
     ########varshaa's code until here########

    def complete_plan(self):
        all_completed = all(var.get() == 1 for var in self.task_vars)

        if all_completed:
            if self.user_data['current_plan_type'] == 'workout':
                self.user_data['completed_workout'] = True
                self.user_data['workout_day'] += 1
                self.save_data()      
                self.planner_page()  # Directly go to planner_page after workout plan completion  ########varshaa's code########

            elif self.user_data['current_plan_type'] == 'diet':
                self.user_data['completed_diet'] = True
                self.user_data['diet_day'] += 1
                self.save_data() 
                self.planner_page()  # Directly go to planner_page after diet plan completion  ########varshaa's code########

            elif self.user_data['current_plan_type'] == 'both':
                if self.user_data['current_plan_step'] == 'workout':
                    self.user_data['completed_workout'] = True
                    self.user_data['both_workout_day'] += 1
                    self.user_data['current_plan_step'] = 'diet'  # Switch to diet after completing workout
                    self.save_data()  
                    messagebox.showinfo("Workout Complete", "You have completed your workout. Now proceed to your diet plan.")  ########varshaa's code########
                    self.show_plan_page()  # Reload the page to show diet plan    

                elif self.user_data['current_plan_step'] == 'diet':
                    self.user_data['completed_diet'] = True
                    self.user_data['both_diet_day'] += 1
                    self.user_data['current_plan_step'] = 'workout'  # Reset to workout for next cycle
                    self.save_data() 
                    messagebox.showinfo("Diet Complete", "You have completed your diet plan. Now returning to the planner.")  ########varshaa's code########
                    self.planner_page()  # Proceed to the planner after completing both plans    ########varshaa's code########

        else:
            messagebox.showwarning("Incomplete Tasks", "Please complete all tasks before proceeding.")


    ########varshaa's code########
    
    def create_treeview(self, parent, columns):
        tree = ttk.Treeview(parent, columns=columns, show="headings", height=7)
        
        # Adjust column widths
        tree.heading("Day", text="Day")
        tree.column("Day", width=100, anchor="center")
        
        tree.heading("Workout", text="Workout")
        tree.column("Workout", width=500, anchor="w")  # Significantly increased widt

        return tree

    def show_treeview(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        center_frame = ttk.Frame(self.content_frame)
        center_frame.pack(expand=True, fill="both", padx=20, pady=20)

        columns = ("Day", "Workout", "Meals")
        tree = self.create_treeview(center_frame, columns)

        scrollbar = ttk.Scrollbar(center_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(side="left", expand=True, fill="both")
        scrollbar.pack(side="right", fill="y")

        # Determine what plan to display based on user choice
        plan_type = self.user_data.get('current_plan_type', '')
        age_category = self.user_data.get('age_category', '')
        bmi_category = self.user_data.get('bmi_category', '')

        workout_plan = self.plans.get('workout', {}).get(age_category, {}).get(bmi_category, [])
        diet_plan = self.plans.get('diet', {}).get(age_category, {}).get(bmi_category, [])

        for day in range(1, 8):  # Days 1 to 7
            workout = workout_plan[day - 1] if day <= len(workout_plan) else "Rest Day"
            meal = diet_plan[day - 1] if day <= len(diet_plan) else "No specific meal plan"

            if plan_type == 'workout':
                tree.insert("", "end", values=(f"Day {day}", workout, "Not chosen"))
            elif plan_type == 'diet':
                tree.insert("", "end", values=(f"Day {day}", "Not chosen", meal))
            elif plan_type == 'both':
                tree.insert("", "end", values=(f"Day {day}", workout, meal))
            else:
                # Handle unexpected plan_type
                tree.insert("", "end", values=(f"Day {day}", "Plan not set", "Plan not set"))

        # Add a label to show the current plan type
        plan_label = ttk.Label(self.content_frame, text=f"Current Plan: {plan_type.capitalize()}", style="Custom.TLabel")
        plan_label.pack(pady=5)

        back_button = ttk.Button(self.content_frame, text="Back to Planner", command=self.show_plan_choice_page, style="Custom.TButton")
        back_button.pack(pady=10)

########varshaa's code########
    def planner_page(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        label1 = ttk.Label(self.content_frame, text="Great job! Keep the momentum going and plan your next move!", style="Custom.TLabel")
        label1.pack(pady=5)

        # Motivational Quote
        motivational_quote = ttk.Label(self.content_frame, text="A woman who prioritizes her health radiates confidence and strength and remember \n" \
                                                                "You don't have to be extreme; just be consistent", justify="center", style="Custom.TLabel")
        motivational_quote.pack(pady=10)

        treeview_button = ttk.Button(self.content_frame, text="View Your Full Week Plan", command=self.show_treeview, style="Custom.TButton")
        treeview_button.pack(pady=10)
        backbutton=ttk.Button(self.content_frame, text="Back to Plan Choice", command=self.show_plan_choice_page, style="Custom.TButton")
        backbutton.pack(pady=10)
        summarychart_button = ttk.Button(self.content_frame, text="View Your Summary Chart", command=self.show_summary_page, style="Custom.TButton")
        summarychart_button.pack(pady=20)

        
########varshaa's code########
    def create_widgets(self):
        self.content_frame = ttk.Frame(self.container)
        self.content_frame.pack(fill="both", expand=True)
        
        # Example button to go back to the Planner page
        back_button = ttk.Button(self.content_frame, text="Back to Planner", command=self.planner_page, style="Custom.TButton")
        back_button.pack(pady=20)
    
        
########varshaa's code########
    def create_workout_frame(self):
        workout_plan = self.user_data.get('workout_plan', [])

        if not workout_plan:
            messagebox.showerror("Error", "No workout plan found. Please assign a workout plan.")
            return

    
        workout_day = self.user_data.get('workout_day', 1) - 1  #for 0-based index
        if workout_day < len(workout_plan):
            exercises = workout_plan[workout_day]  # Get exercises for the current day
        else:
            exercises = ["Rest Day"]  # Default message if no exercises are available

        # comma-separated string of exercises
        exercise_string = ", ".join(exercises)


#rk
    def show_summary_page(self):
        self.update_background('SUMRPAGE')
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        main_frame = ttk.Frame(self.content_frame)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)

        title_label = ttk.Label(main_frame, text="Your Fitness Summary \n"
                                "You have made significant strides in your fitness journey, and your dedication is truly inspiring. \n"
                                "Here’s a detailed recap of your progress so far, showcasing the hard work and commitment you've put into achieving your health and wellness goals.", justify="center")
        title_label.pack(pady=(0, 20))

        # Top section: BMI and Goal Summary
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 20))

        # BMI Information
        bmi_frame = ttk.LabelFrame(top_frame, text="BMI Information")
        bmi_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        ttk.Label(bmi_frame, text=f"BMI: {self.user_data['bmi']:.2f}").pack(pady=5)
        ttk.Label(bmi_frame, text=f"Category: {self.user_data['bmi_category']}").pack(pady=5)

        # Goal Summary
        goal_frame = ttk.LabelFrame(top_frame, text="Goal Summary")
        goal_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
        ttk.Label(goal_frame, text=f"Workouts Completed: {self.user_data['workout_day'] - 1}/7").pack(pady=5)
        ttk.Label(goal_frame, text=f"Diet Plan Followed: {self.user_data['diet_day'] - 1}/7").pack(pady=5)

        # Middle section: Weekly Plan
        plan_frame = ttk.LabelFrame(main_frame, text="Weekly Meal and Workout Plan")
        plan_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))

        plan_tree = ttk.Treeview(plan_frame, columns=("Day", "Meal", "Workout"), show="headings", height=7)
        plan_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for col in ("Day", "Meal", "Workout"):
            plan_tree.heading(col, text=col)
            plan_tree.column(col, width=100)

        scrollbar = ttk.Scrollbar(plan_frame, orient="vertical", command=plan_tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        plan_tree.configure(yscrollcommand=scrollbar.set)

        # Populate the treeview with completed workout and diet data
        workout_days = max(self.user_data['workout_day'], self.user_data['both_workout_day'])
        diet_days = max(self.user_data['diet_day'], self.user_data['both_diet_day'])
        max_days = max(workout_days, diet_days)

        for i in range(max_days):
            day = i + 1
            workout = "Completed" if day < workout_days else "Not completed"
            diet = "Followed" if day < diet_days else "Not followed"
            plan_tree.insert("", "end", values=(f"Day {day}", diet, workout))

        # Bottom section: Motivation and Recommendations
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill=tk.X)

        # List of motivational quotes
        quotes = [
            "Stay committed to your decisions, but flexible in your approach.",
            "Success starts with self-discipline.",
            "Believe in yourself and all that you are.",
            "Push harder than yesterday if you want a different tomorrow.",
            "Consistency is key to success.",
            "Your only limit is your mind.",
            "You are stronger than you think.",
            "Small progress is still progress.", "Strong women aren't simply born. They are forged through challenges, perseverance, and a passion for health."
            "Take care of your body. It's the only place you have to live.",
            "Empower yourself by taking charge of your health and fitness every day.",
            "Fitness is not about being better than someone else. It's about being better than you used to be.",
            "A woman who prioritizes her health radiates confidence and strength.,"
            "You don't have to be extreme; just be consistent.",
            "The strongest actions for a woman are to love herself, be herself, and shine amongst those who never believed she could.",
            "Your body can stand almost anything. It’s your mind you have to convince.",
            "The only bad workout is the one that didn’t happen.",
            "Be proud of how far you've come, and never stop pushing to become even better.",
            "The key to a healthy lifestyle is finding balance. Love your body and treat it with kindness.",
            "Women who invest in themselves go further in life.",
            "Exercise is not just about fitness; it's therapy for the mind, body, and soul.",
            "A healthy outside starts from the inside.",
            "Believe in your strength. Believe in your power. Believe in yourself.",
            "The body achieves what the mind believes.",
            "She believed she could, so she did.",
            "Sweat is magic. Cover yourself in it daily to grant your fitness wishes.",
            "Don't wish for a good body. Work for it.",
            "Strong is the new beautiful.",
            "You are capable of amazing things. Believe in your strength.",
            "Fall in love with taking care of yourself: body, mind, and spirit.",
            "Fitness is not about being better than someone else; it’s about being better than you used to be.",
            "A woman who moves forward with her health inspires others to follow.",
            "The best project you'll ever work on is you.",
            "Let exercise be your stress relief, not food.",
            "Be stronger than your excuses.",
            "Your health is an investment, not an expense.",
            "The strongest women are those who build others up while maintaining their own strength.",
            "Consistency is what transforms average into amazing.",
            "A fit woman is unstoppable. She sets goals and doesn’t stop until they are achieved.",
            "Love yourself enough to live a healthy lifestyle.",
            "Taking care of yourself is the most powerful way to begin taking care of others.",
            "Your only limit is your mind. Break those barriers and get stronger every day.",
            "Healthy is an outfit that looks different on every woman, but it always fits perfectly."
        ]

        # Randomly select a quote
        random_quote = random.choice(quotes)

                # Motivational Quote
        quote_frame = ttk.LabelFrame(bottom_frame, text="Your Daily Motivation")
        quote_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        quote_label = ttk.Label(quote_frame, text=random_quote, wraplength=200)
        quote_label.pack(pady=10, padx=10)

        # Back button
        back_button = ttk.Button(main_frame, text="Back to Plan Choice", command=self.show_plan_choice_page, style="Custom.TButton")
        back_button.pack(pady=(20, 0))

if __name__ == "__main__":
    app = FitnessApp()
    app.mainloop()
