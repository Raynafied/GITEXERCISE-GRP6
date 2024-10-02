# import tkinter as tk

# class FitnessApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Fitness App")
#         self.root.geometry("620x420")  # Change size as per RATNA later
#         self.pages = {}  # storre different pages
#         self.user_data = {}  # store user selections
#         self.setup_pages()  # set up pages

#         # Show the initial page
#         self.show_page('plan_choice')  # Show the first page

#     def setup_pages(self):
#         plan_choice_page = PlanChoicePage(self)
#         workout_plan_page = WorkoutPlanPage(self)
#         diet_plan_page = DietPlanPage(self)
        
#         self.pages['plan_choice'] = plan_choice_page
#         self.pages['workout_plan'] = workout_plan_page
#         self.pages['diet_plan'] = diet_plan_page

#     def show_page(self, page_name):
#         # Check if the page exists
#         if page_name not in self.pages:
#             print("Error: Page does not exist!")
#             return

#         # Display the page
#         page = self.pages[page_name]
#         page.pack(fill='both', expand=True)

#         #this will hide other pages
#         for p in self.pages.values():
#             if p != page:
#                 p.pack_forget()

# class PlanChoicePage(tk.Frame):
#     def __init__(self, app):
#         super().__init__(app.root, bg="light blue") 
#         self.app = app

#         # Configure padding
#         self.configure(padx=20, pady=20)

#         # Create and pack the label
#         label = tk.Label(self, text="Choose a Plan", font=("Helvetica", 16, "bold"), bg="light blue")
#         label.pack(pady=20)

#         # Create and pack the buttons
#         self.workoutbutton = tk.Button(self, text="Workout Plan", command=self.select_workout_plan, font=("Helvetica", 12, "bold"), bg="green", fg="white")
#         self.workoutbutton.pack(pady=10, fill='x')

#         self.dietbutton = tk.Button(self, text="Diet Plan", command=self.select_diet_plan, font=("Helvetica", 12, "bold"), bg="green", fg="white")
#         self.dietbutton.pack(pady=10, fill='x')

#         self.bothbutton = tk.Button(self, text="Both Plan", command=self.select_both_plan, font=("Helvetica", 12, "bold"), bg="green", fg="white")
#         self.bothbutton.pack(pady=10, fill='x')

#     def select_workout_plan(self):
#         # this is to navigate to workout plan page
#         self.app.show_page('workout_plan')

#     def select_diet_plan(self):
#         self.app.show_page('diet_plan')

#     def select_both_plan(self): #here you need to work to make sure workout and diet plan shows with
#         self.app.show_page('workout_plan')

# class WorkoutPlanPage(tk.Frame):
#     def __init__(self, app):
#         super().__init__(app.root, bg="grey") 
#         self.app = app

        
#         label = tk.Label(self, text="Workout Plan", font=("Helvetica", 16, "bold"), bg="pink")
#         label.pack(pady=20)

        
#         workout_plans = [
#             "Push-ups: 3 sets of 12 reps",
#             "Squats: 4 sets of 15 reps",
#             "Lunges: 3 sets of 10 reps",
#             "Plank: Hold for 60 seconds",
#             "Jumping Jacks: 3 sets of 30 reps"
#         ]

#         for plan in workout_plans:
#             tk.Label(self, text=plan, font=("Helvetica", 12), bg="pink").pack(pady=5)

# class DietPlanPage(tk.Frame):
#     def __init__(self, app):
#         super().__init__(app.root, bg="grey")
#         self.app = app

#         # Create and pack the label
#         label = tk.Label(self, text="Diet Plan", font=("Helvetica", 16, "bold"), bg="pink")
#         label.pack(pady=20)

#         diet_plans = [
#             "Breakfast: Oatmeal with fruits",
#             "Lunch: Grilled chicken salad",
#             "Snack: Greek yogurt with nuts",
#             "Dinner: Steamed vegetables with tofu",
#             "Hydration: Drink 8 cups of water"
#         ]

#         for plan in diet_plans:
#             tk.Label(self, text=plan, font=("Helvetica", 12), bg="pink").pack(pady=5)

# # main application loop
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FitnessApp(root)
#     root.mainloop()
