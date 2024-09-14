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
from tkinter import*
import tkinter

window = Tk()

window.state('zoomed') #window.geometry('500x500')
window.title('Female Fitness App')

frame = tkinter.Frame()

login_label = tkinter.Label(frame, text="Welcome")
name_label = tkinter.Label(frame, text="Enter Your Name Gorgeous! ")
name_entry = tkinter.Entry(frame)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1, pady=20)

frame.pack()
window.mainloop()
# user can type their name here already
