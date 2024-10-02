# import tkinter as tk

# class FitnessApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Fitness App")
#         self.root.geometry("620x420")  # Change size as per RATNA later

#         self.pages = {}  # storre different pages
#         self.setup_pages()  # set up pages
#         self.show_page('plan_choice')  #show the first page

#     def setup_pages(self):
#         self.pages['plan_choice'] = PlanChoicePage(self)
#         self.pages['plan'] = PlanPage(self)

#     def show_page(self, page_name):
#         if page_name not in self.pages:
#             print(f"Error: Page '{page_name}' does not exist!")
#             return
#         page = self.pages[page_name]
#         page.pack(fill='both', expand=True)
#         for p in self.pages.values():
#             if p != page:
#                 p.pack_forget()

# class PlanChoicePage(tk.Frame):
#     def __init__(self, app):
#         super().__init__(app.root)
        
#         tk.Label(self, text="Plan Choice Page").pack() #this will create label to the page
        
#         self.button = tk.Button(self, text="Click", command=self.on_button_click) 
#         self.button.pack() #add a fake button but need self.button.pack() to make it visible
    
#     def on_button_click(self):
#         print("Button was clicked!")

# class PlanPage(tk.Frame):
#     def __init__(self, app):
#         super().__init__(app.root)
#         tk.Label(self, text="Plan Page").pack()

# # Example usage
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FitnessApp(root)
#     root.mainloop()

