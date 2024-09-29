# first part tkinter testing
#from tkinter import*

#window = Tk()
#window.geometry('500x500')
#window.title('Female Fitness App')

#window.mainloop()

#2nd testing for labels
#from tkinter import*

#window = Tk()
#window.geometry('500x500')
#window.title('Female Fitness App')

#label = Label(window,text='Welcome, Please enter your name gorgeous!')
#label.place(x=100,y=200)

#window.mainloop()

# 3rd testing for buttons
# from tkinter import*
# def click():
#     print ('I am fine!')

# window = Tk()
# window.geometry('500x500')
# window.title('Female Fitness App')

# label = Label(window,text='Hi')
# label.place(x=100,y=200)

# button = Button(window,text='Welcome GORGEOUS!',command=click)
# button.place(x=200,y=300)

# window.mainloop()


# 4th testing the entrybox
# from tkinter import*
# def submit():
#     value = entry.get()
#     print(value)

# window = Tk()
# window.geometry('500x500')
# window.title('Female Fitness App')

# entry = Entry(window)
# entry.place(x=100,y=200)

# buttonSubmit = Button(window,text='Lets Start',command=submit)
# buttonSubmit.place(x=200,y=100)

# window.mainloop()



# Start (working)
# from tkinter import*

# window = Tk()

# window.state('zoomed')
# window.title('Female Fitness App')

# label = Label(window,text='Welcome, Please enter your name gorgeous!')
# label.pack()

# window.mainloop()



# 2nd progress - to make user type their name 
# from tkinter import*
# import tkinter

# window = Tk()

# window.state('zoomed') #window.geometry('500x500')
# window.title('Female Fitness App')

# frame = tkinter.Frame()

# login_label = tkinter.Label(frame, text="Welcome")
# name_label = tkinter.Label(frame, text="Enter Your Name Gorgeous! ")
# name_entry = tkinter.Entry(frame)

# login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
# name_label.grid(row=1, column=0)
# name_entry.grid(row=1, column=1, pady=20)

# frame.pack()
# window.mainloop()
# user can type their name here already 


# # 3rd Progress to make user to click something after typing their name
# from tkinter import*
# import tkinter
# window = Tk()

# # window.state('zoomed') or
# window.geometry('500x500')
# window.title('Female Fitness App')
# frame = tkinter.Frame()

# login_label = tkinter.Label(frame, text="Welcome,")
# name_label = tkinter.Label(frame, text="Enter Your Name Gorgeous! ")
# name_entry = tkinter.Entry(frame)
# login_button = tkinter.Button(frame, text="Let's Start")

# login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
# name_label.grid(row=1, column=0)
# name_entry.grid(row=1, column=1, pady=20)
# login_button.grid(row=3, column=0, columnspan=2, pady=30)

# frame.pack()
# window.mainloop()
# # user can click button after typing their name (but does not redirect anywhr)

# SETTLED - FOR USER LOGIN/WELCOME PAGE 



# BMI Page 
# Progress BMI Calculator/Data  1
# from tkinter import*
# import tkinter

# window = Tk()

# # window.state('zoomed')
# window.geometry('500x500')
# window.title('Female Fitness App')
# frame = tkinter.Frame()

# bmi_label = tkinter.Label(frame, text="BMI Calculator")
# height_label = tkinter.Label(frame, text="Enter Your Height: ")
# height_entry = tkinter.Entry(frame)
# weight_label = tkinter.Label(frame, text="Enter Your Weight: ")
# weight_entry = tkinter.Entry(frame)
# bmicalculate_button = tkinter.Button(frame, text="My BMI")

# bmi_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
# height_label.grid(row=1, column=0)
# height_entry.grid(row=2, column=0, pady=10)
# weight_label.grid(row=3, column=0)
# weight_entry.grid(row=4, column=0, pady=10)
# bmicalculate_button.grid(row=5, column=0, columnspan=2, pady=30)

# frame.pack()
# window.mainloop()
# #can insert height & weight but will not show the calculated bmi



# Progress BMI Calculator/Data  2 - to include the function to collect users h&w in order to calculate their BMI

# from tkinter import*
# import tkinter

# window = Tk()

# # window.state('zoomed')
# window.geometry('500x500')
# window.title('Female Fitness App')
# frame = tkinter.Frame()

# def calculate_bmi():
#     try:
#         height = float(height_entry.get()) / 100  # convert cm to m
#         weight = float(weight_entry.get())
#         bmi = weight / (height ** 2)
#         bmi_result.config(text=f"Your BMI is {bmi}")
#     except ValueError:
#         bmi_result.config(text="Please enter valid numbers")

# # welcome_label = tkinter.Label(frame, text="Welcome!")
# bmi_label = tkinter.Label(frame, text="BMI Calculator")
# height_label = tkinter.Label(frame, text="Please enter Your Height (in cm) : ")
# height_entry = tkinter.Entry(frame)
# weight_label = tkinter.Label(frame, text="Please enter Your Weight (in kg) : ")
# weight_entry = tkinter.Entry(frame)
# bmicalculator_button = Button(frame, text="Calculate My BMI", command=calculate_bmi)
# bmi_result = Label(frame, text="")

# # welcome_label.grid(row=0, column=0, sticky="nw", columnspan=2, pady=10)
# bmi_label.grid(column=0, columnspan=2, sticky="news", pady=30)
# height_label.grid(row=2, column=0)
# height_entry.grid(row=3, column=0, pady=10)
# weight_label.grid(row=4, column=0)
# weight_entry.grid(row=5, column=0, pady=10)
# bmicalculator_button.grid(row=6, column=0, columnspan=2, pady=30)
# bmi_result.grid(row=7, column=0, columnspan=2)

# frame.pack()
# window.mainloop()
# # # user can calculate their bmi and user can see their bmi



#Progress BMI Calculator/Data 3 - to show the category of BMI users are in
# - to add "lets continue" button 

# from tkinter import*
# import tkinter

# window = Tk()

# # window.state('zoomed')
# window.geometry('500x500')
# window.title('Female Fitness App')
# frame = tkinter.Frame()

# def bmi_category(bmi):
#     if bmi < 18.5:
#         return "Underweight"
#     elif 18.5 <= bmi < 24.9:
#         return "Normal weight"
#     elif 25 <= bmi < 29.9:
#         return "Overweight"
#     else:
#         return "Obesity"

# def calculate_bmi():
#     try:
#         height = float(height_entry.get()) / 100  # convert cm to m
#         weight = float(weight_entry.get())
#         bmi = weight / (height ** 2)
#         category = bmi_category(bmi)
#         bmi_result.config(text=f"Your BMI is {bmi}")
#         category_result.config(text=f"Category: {category}")
#     except ValueError:
#         bmi_result.config(text="Please enter valid numbers")

# # welcome_label = tkinter.Label(frame, text="Welcome!")
# bmi_label = tkinter.Label(frame, text="BMI Calculator")
# height_label = tkinter.Label(frame, text="Please enter Your Height (in cm) : ")
# height_entry = tkinter.Entry(frame)
# weight_label = tkinter.Label(frame, text="Please enter Your Weight (in kg) : ")
# weight_entry = tkinter.Entry(frame)
# bmicalculator_button = Button(frame, text="Calculate My BMI", command=calculate_bmi)
# bmi_result = Label(frame, text="")
# category_result = Label(frame, text="")
# continue_button = Button(frame, text="Let's Continue")

# # welcome_label.grid(row=0, column=0, sticky="nw", columnspan=2, pady=10)
# bmi_label.grid(column=0, columnspan=2, sticky="news", pady=30)
# height_label.grid(row=2, column=0)
# height_entry.grid(row=3, column=0, pady=10)
# weight_label.grid(row=4, column=0)
# weight_entry.grid(row=5, column=0, pady=10)
# bmicalculator_button.grid(row=6, column=0, columnspan=2, pady=30)
# bmi_result.grid(row=7, column=0, columnspan=2)
# category_result.grid(row=8, column=0, columnspan=2, pady=10)
# continue_button.grid(row=10, column=0, columnspan=2, pady=10)

# frame.pack()
# window.mainloop()
# ##user can get their category displayed & also added a "lets continue button"


# Progress BMI Calculator/Data 4th and final
# to make the lets continue button function
# to makesure user must calculate their bmi first, only then they can click lets continue button
# rounded off the bmi value to 2 decimal places
#
# from tkinter import*
# import tkinter

# window = Tk()

# # window.state('zoomed')
# window.geometry('500x500')
# window.title('Female Fitness App')
# frame = tkinter.Frame()

# def bmi_category(bmi):
#     if bmi < 18.5:
#         return "Underweight"
#     elif 18.5 <= bmi < 24.9:
#         return "Normal weight"
#     elif 25 <= bmi < 29.9:
#         return "Overweight"
#     else:
#         return "Obesity"

# def calculate_bmi():
#     try:
#         height = float(height_entry.get()) / 100  # convert cm to m
#         weight = float(weight_entry.get())
#         bmi = weight / (height ** 2)
#         category = bmi_category(bmi)
#         bmi_result.config(text=f"Your BMI is {bmi:.2f}")
#         category_result.config(text=f"Category: {category}")

#         continue_button.config(state=NORMAL)
#     except ValueError:
#         bmi_result.config(text="Please enter valid numbers")
#         category_result.config(text="")
#         continue_button.config(state=DISABLED)

# # welcome_label = tkinter.Label(frame, text="Welcome!")
# bmi_label = tkinter.Label(frame, text="BMI Calculator")
# height_label = tkinter.Label(frame, text="Please enter Your Height (in cm) : ")
# height_entry = tkinter.Entry(frame)
# weight_label = tkinter.Label(frame, text="Please enter Your Weight (in kg) : ")
# weight_entry = tkinter.Entry(frame)
# bmicalculator_button = Button(frame, text="Calculate My BMI", command=calculate_bmi)
# bmi_result = Label(frame, text="")
# category_result = Label(frame, text="")

# continue_button = Button(frame, text="Let's Continue", state=DISABLED)

# # welcome_label.grid(row=0, column=0, sticky="nw", columnspan=2, pady=10)
# bmi_label.grid(column=0, columnspan=2, sticky="news", pady=30)
# height_label.grid(row=2, column=0)
# height_entry.grid(row=3, column=0, pady=10)
# weight_label.grid(row=4, column=0)
# weight_entry.grid(row=5, column=0, pady=10)
# bmicalculator_button.grid(row=6, column=0, columnspan=2, pady=30)
# bmi_result.grid(row=7, column=0, columnspan=2)
# category_result.grid(row=8, column=0, columnspan=2, pady=10)
# continue_button.grid(row=10, column=0, columnspan=2, pady=10)

# frame.pack()
# window.mainloop()
# #SETTLED FOR 2nd page



#combined user login and bmi data for 2 pages completed

# import tkinter as tk
# from tkinter import ttk

# class FemaleFitnessApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry('500x500')
#         self.title('Female Fitness App')
#         self.frame = ttk.Frame(self)
#         self.frame.pack(fill=tk.BOTH, expand=True)
#         self.show_login_page()

#     def show_login_page(self):
#         for widget in self.frame.winfo_children():
#             widget.destroy()

#         def check_name(*args):
#             if self.name_entry.get().strip():
#                 login_button.config(state=tk.NORMAL)
#             else:
#                 login_button.config(state=tk.DISABLED)

#         login_label = ttk.Label(self.frame, text="Welcome to Female Fitness App!")
#         name_label = ttk.Label(self.frame, text="Enter Your Name Gorgeous: ")
#         self.name_entry = ttk.Entry(self.frame)
#         login_button = ttk.Button(self.frame, text="Let's Start", command=self.show_bmi_page, state=tk.DISABLED)

#         login_label.grid(row=0, column=0, columnspan=2, pady=40, padx=20)
#         name_label.grid(row=1, column=0, padx=(0,10), sticky="e")
#         self.name_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w")
#         login_button.grid(row=2, column=0, columnspan=2, pady=30)

#         self.frame.grid_columnconfigure(0, weight=1)
#         self.frame.grid_columnconfigure(1, weight=1)

#         self.name_var = tk.StringVar()
#         self.name_entry.config(textvariable=self.name_var)
#         self.name_var.trace("w", check_name)

#     def show_bmi_page(self):
#         for widget in self.frame.winfo_children():
#             widget.destroy()

#         def bmi_category(bmi):
#             if bmi < 18.5:
#                 return "Underweight"
#             elif 18.5 <= bmi < 24.9:
#                 return "Normal weight"
#             elif 25 <= bmi < 29.9:
#                 return "Overweight"
#             else:
#                 return "Obesity"

#         def calculate_bmi():
#             try:
#                 height = float(height_entry.get()) / 100  # convert cm to m
#                 weight = float(weight_entry.get())
#                 bmi = weight / (height ** 2)
#                 category = bmi_category(bmi)
#                 bmi_result.config(text=f"Your BMI is {bmi:.2f}")
#                 category_result.config(text=f"Category: {category}")
#                 continue_button.config(state=tk.NORMAL)
#             except ValueError:
#                 bmi_result.config(text="Please enter valid numbers")
#                 category_result.config(text="")
#                 continue_button.config(state=tk.DISABLED)

#         bmi_label = ttk.Label(self.frame, text="Body Mass Index Calculator")
#         height_label = ttk.Label(self.frame, text="Please enter Your Height (in cm) : ")
#         height_entry = ttk.Entry(self.frame)
#         weight_label = ttk.Label(self.frame, text="Please enter Your Weight (in kg) : ")
#         weight_entry = ttk.Entry(self.frame)
#         bmicalculator_button = ttk.Button(self.frame, text="Calculate My BMI", command=calculate_bmi)
#         bmi_result = ttk.Label(self.frame, text="")
#         category_result = ttk.Label(self.frame, text="")
#         continue_button = ttk.Button(self.frame, text="Let's Continue", state=tk.DISABLED)

#         bmi_label.grid(column=0, columnspan=2, pady=30)
#         height_label.grid(row=2, column=0, columnspan=2)
#         height_entry.grid(row=3, column=0, columnspan=2, pady=10)
#         weight_label.grid(row=4, column=0, columnspan=2)
#         weight_entry.grid(row=5, column=0, columnspan=2, pady=10)
#         bmicalculator_button.grid(row=6, column=0, columnspan=2, pady=30)
#         bmi_result.grid(row=7, column=0, columnspan=2)
#         category_result.grid(row=8, column=0, columnspan=2, pady=10)
#         continue_button.grid(row=10, column=0, columnspan=2, sticky="s", pady=10)

#         self.frame.grid_columnconfigure(0, weight=1)
#         self.frame.grid_columnconfigure(1, weight=1)

# if __name__ == "__main__":
#     app = FemaleFitnessApp()
#     app.mainloop()

#updates done 23 Sept 2024 
# added age into the login page, disabled the lets start button as well 

import tkinter as tk
from tkinter import ttk

class FemaleFitnessApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Female Fitness App')
        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.show_login_page()

    def show_login_page(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        def validate_age(P):
            return P.isdigit() or P == ""

        def validate_inputs(*args):
            name = self.name_entry.get().strip()
            age = self.age_entry.get().strip()
            if name and age.isdigit():
                login_button.config(state=tk.NORMAL)
            else:
                login_button.config(state=tk.DISABLED)

        login_label = ttk.Label(self.frame, text="Welcome to Female Fitness App!")
        name_label = ttk.Label(self.frame, text="Enter Your Name Gorgeous: ")
        self.name_entry = ttk.Entry(self.frame)
        age_label = ttk.Label(self.frame, text="Enter Your Age: ")
        self.age_entry = ttk.Entry(self.frame, validate="key", validatecommand=(self.register(validate_age), '%P'))
        login_button = ttk.Button(self.frame, text="Let's Start", command=self.show_bmi_page, state=tk.DISABLED)

        login_label.grid(row=0, column=0, columnspan=2, pady=40, padx=20)
        name_label.grid(row=1, column=0, padx=(0,10), sticky="e")
        self.name_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        age_label.grid(row=2, column=0, padx=(0, 10), sticky="e")
        self.age_entry.grid(row=2, column=1, pady=10, padx=10, sticky="w")
        login_button.grid(row=3, column=0, columnspan=2, pady=30)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        self.name_entry.bind('<KeyRelease>', validate_inputs)
        self.age_entry.bind('<KeyRelease>', validate_inputs)

    def validate_and_proceed(self):
        age = self.age_entry.get()
        if age.isdigit():
            self.show_bmi_page()
        else:
            error_label = ttk.Label(self.frame, text="Please enter a valid age (numbers only)", foreground="red")
            error_label.grid(row=4, column=0, columnspan=2, pady=10)

    def show_bmi_page(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        def bmi_category(bmi):
            if bmi < 18.5:
                return "Underweight"
            elif 18.5 <= bmi < 24.9:
                return "Normal weight"
            elif 25 <= bmi < 29.9:
                return "Overweight"
            else:
                return "Obesity"

        def calculate_bmi():
            try:
                height = float(height_entry.get()) / 100  # convert cm to m
                weight = float(weight_entry.get())
                bmi = weight / (height ** 2)
                category = bmi_category(bmi)
                bmi_result.config(text=f"Your BMI is {bmi:.2f}")
                category_result.config(text=f"Category: {category}")
                continue_button.config(state=tk.NORMAL)
            except ValueError:
                bmi_result.config(text="Please enter valid numbers")
                category_result.config(text="")
                continue_button.config(state=tk.DISABLED)

        bmi_label = ttk.Label(self.frame, text="Body Mass Index Calculator")
        height_label = ttk.Label(self.frame, text="Please enter Your Height (in cm) : ")
        height_entry = ttk.Entry(self.frame)
        weight_label = ttk.Label(self.frame, text="Please enter Your Weight (in kg) : ")
        weight_entry = ttk.Entry(self.frame)
        bmicalculator_button = ttk.Button(self.frame, text="Calculate My BMI", command=calculate_bmi)
        bmi_result = ttk.Label(self.frame, text="")
        category_result = ttk.Label(self.frame, text="")
        continue_button = ttk.Button(self.frame, text="Let's Continue", state=tk.DISABLED)

        summary_page_button = ttk.Button(self.frame, text="My Summary Page", command=self.show_summary_page)

        bmi_label.grid(column=0, columnspan=2, pady=30)
        height_label.grid(row=2, column=0, columnspan=2)
        height_entry.grid(row=3, column=0, columnspan=2, pady=10)
        weight_label.grid(row=4, column=0, columnspan=2)
        weight_entry.grid(row=5, column=0, columnspan=2, pady=10)
        bmicalculator_button.grid(row=6, column=0, columnspan=2, pady=30)
        bmi_result.grid(row=7, column=0, columnspan=2)
        category_result.grid(row=8, column=0, columnspan=2, pady=10)
        continue_button.grid(row=10, column=0, columnspan=2, sticky="s", pady=10)

        summary_page_button.grid(row=12, column=0, columnspan=2, sticky="s", pady=10) 


        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

## FINALIZED SUMMARY CHART AFTER MERGE WITH TEAMMATE CODE
#note: THIS IS THE CODE THAT RUNS
    def show_summary_page(self):
        self.update_background('choipla')
        for widget in self.frame.winfo_children():
            widget.destroy()

        main_frame = ttk.Frame(self.frame)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        title_label = ttk.Label(main_frame, text="Your Fitness Summary")
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

        # Motivational Quote
        quote_frame = ttk.LabelFrame(bottom_frame, text="Your Daily Motivation")
        quote_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        quote_label = ttk.Label(quote_frame, text="Stay committed to your decisions, but flexible in your approach.",
                                wraplength=180)
        quote_label.pack(pady=10, padx=10)

        # Recommendations
        rec_frame = ttk.LabelFrame(bottom_frame, text="Recommendations")
        rec_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
        ttk.Label(rec_frame, text="Daily Calorie Intake: 2000").pack(pady=5)
        ttk.Label(rec_frame, text="Daily Steps: 7K-10K").pack(pady=5)

        # Back button
        back_button = ttk.Button(main_frame, text="Back to Plan Choice", command=self.show_plan_choice_page)
        back_button.pack(pady=(20, 0))


if __name__ == "__main__":
    app = FemaleFitnessApp()
    app.mainloop()