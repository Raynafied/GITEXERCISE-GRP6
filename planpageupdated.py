# import tkinter as tk

# class FitnessApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Fitness App")
#         self.root.geometry("620x420")  # Change size as per RATNA later
#         self.pages = {} # storre different pages
#         self.setup_pages()  #set up pages

#         # Show the initial page
#         self.show_page('plan_choice')  #show the first page

#     def setup_pages(self):
#         self.pages['plan_choice'] = PlanChoicePage(self)
#         self.pages['plan'] = PlanPage(self)

#     def show_page(self, page_name):
#         if page_name not in self.pages:
#             print(f"Error: Page '{page_name}' does not exist!")  #this will check if the page exists
#             return
        
#         page = self.pages[page_name]
#         page.pack(fill='both', expand=True) #display the page

#         # Hide other pages
#         for p in self.pages.values():
#             if p != page:
#                 p.pack_forget()

# class PlanChoicePage(tk.Frame):
#     def __init__(self, app):
#         super().__init__(app.root, bg="#e0f7fa")
#         self.app = app

#         # Configure padding
#         self.configure(padx=20, pady=20)

#         # Create a label
#         label = tk.Label(self, text="Choose a Plan", font=("Helvetica", 16, "bold"), bg="#e0f7fa")
#         label.pack(pady=20)

#         # Create buttons
#         self.workoutbutton = tk.Button(self, text="Workout Plan", command=self.select_workout_plan, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
#         self.workoutbutton.pack(pady=10, fill='x')

#         self.dietbutton = tk.Button(self, text="Diet Plan", command=self.select_diet_plan, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
#         self.dietbutton.pack(pady=10, fill='x')

#         self.bothbutton = tk.Button(self, text="Both Plan", command=self.select_both_plan, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
#         self.bothbutton.pack(pady=10, fill='x')

#     def select_workout_plan(self):
#         self.app.user_data['current_plan_type'] = 'workout'
#         print("workout plan selected")
        

#     def select_diet_plan(self):
#         self.app.user_data['current_plan_type'] = 'diet'
#         print("diet plan selected")

#     def select_both_plan(self):
#         # Action for selecting both plans
#         self.app.user_data['current_plan_type'] = 'both'
#         print("both plans selected")

# class PlanPage(tk.Frame):
#     def __init__(self, app):
#         super().__init__(app.root)
#         label = tk.Label(self, text="Plan Page")
#         label.pack()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FitnessApp(root)
#     root.mainloop()



