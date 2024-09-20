import tkinter as tk
from tkinter import messagebox
import json
import os

root = tk.Tk()
root.title("Fitness App")
root.geometry("620x420")

user_data = {
    'name': None,
    'current_plan_type': '',
    'current_plan_step': '',
    'workout_day': 1,
    'diet_day': 1,
    'both_workout_day': 1,
    'both_diet_day': 1
}

# Widgets
label = tk.Label(root, font=("Helvetica", 16, "bold"))
label.pack(pady=20)

button_workout = tk.Button(root, text="Workout Plan", bg="#4CAF50", fg="white")
button_workout.pack(pady=10)

button_diet = tk.Button(root, text="Diet Plan", bg="#4CAF50", fg="white")
button_diet.pack(pady=10)

button_both = tk.Button(root, text="Both Workout and Diet", bg="#4CAF50", fg="white")
button_both.pack(pady=10)

day_label = tk.Label(root)
day_label.pack(pady=10)

checklist_frame = tk.Frame(root)
checklist_frame.pack(pady=10)

complete_button = tk.Button(root, text="Complete", bg="#4CAF50", fg="white")
complete_button.pack(pady=10)

# Plan Selection
def show_plan_choice_page():
    label.config(text="Choose a Plan")
    button_workout.pack(pady=10)
    button_diet.pack(pady=10)
    button_both.pack(pady=10)
    day_label.pack_forget()
    checklist_frame.pack_forget()
    complete_button.pack_forget()

def show_workout_plan():
    global user_data
    user_data['current_plan_type'] = 'workout'
    user_data['current_plan_step'] = 'workout'
    save_data()
    show_plan_page()

def show_diet_plan():
    global user_data
    user_data['current_plan_type'] = 'diet'
    user_data['current_plan_step'] = 'diet'
    save_data()
    show_plan_page()

def show_both_plans():
    global user_data
    user_data['current_plan_type'] = 'both'
    user_data['current_plan_step'] = 'workout'
    save_data()
    show_plan_page()

def show_plan_page():
    global user_data
    label.config(text="Today's Plan")
    button_workout.pack_forget()
    button_diet.pack_forget()
    button_both.pack_forget()
    load_plan()

def load_plan():
    global user_data
    plan_type = user_data['current_plan_type']
    step = user_data['current_plan_step']
    
    plan_items = {
        "workout": ["Push-ups", "Squats", "Plank"],
        "diet": ["Breakfast: Oats", "Lunch: Salad", "Dinner: Grilled Chicken"]
    }
    
    if plan_type == 'workout':
        items = plan_items["workout"]
    elif plan_type == 'diet':
        items = plan_items["diet"]
    else:
        if step == 'workout':
            items = plan_items["workout"]
        elif step == 'diet':
            items = plan_items["diet"]
    
    for widget in checklist_frame.winfo_children():
        widget.destroy()
    
    for item in items:
        tk.Checkbutton(checklist_frame, text=item).pack(anchor='w')
    
    if plan_type == 'both':
        if step == 'workout':
            label.config(text="Today's Plan (Workout):")
            current_day = user_data['both_workout_day']
        elif step == 'diet':
            label.config(text="Today's Plan (Diet):")
            current_day = user_data['both_diet_day']
    else:
        label.config(text=f"{plan_type.capitalize()} Plan for Today:")
        current_day = user_data[f'{plan_type}_day']
    
    day_label.config(text=f"Day {current_day}")
    day_label.pack(pady=10)
    checklist_frame.pack(pady=10)
    complete_button.pack(pady=10)

def complete_plan():
    global user_data
    plan_type = user_data['current_plan_type']
    step = user_data['current_plan_step']

    if plan_type == 'both':
        if step == 'workout':
            user_data['both_workout_day'] += 1
            user_data['current_plan_step'] = 'diet'
        elif step == 'diet':
            user_data['both_diet_day'] += 1
            user_data['current_plan_step'] = 'workout'
    elif plan_type == 'workout':
        user_data['workout_day'] += 1
    elif plan_type == 'diet':
        user_data['diet_day'] += 1

    save_data()
    show_plan_page()

# Save and Load Data
def save_data():
    data_dir = os.path.join(os.path.expanduser("~"), "FitnessAppData")
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    filename = os.path.join(data_dir, "user_data.json")
    with open(filename, 'w') as f:
        json.dump(user_data, f)

def load_data():
    data_dir = os.path.join(os.path.expanduser("~"), "FitnessAppData")
    filename = os.path.join(data_dir, "user_data.json")
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            global user_data
            user_data = json.load(f)

button_workout.config(command=show_workout_plan)
button_diet.config(command=show_diet_plan)
button_both.config(command=show_both_plans)
complete_button.config(command=complete_plan)

show_plan_choice_page()

root.mainloop()
