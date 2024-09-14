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
from tkinter import*
def submit():
    value = entry.get()
    print(value)

window = Tk()
window.geometry('500x500')
window.title('Female Fitness App')

entry = Entry(window)
entry.place(x=100,y=200)

buttonSubmit = Button(window,text='Lets Start',command=submit)
buttonSubmit.place(x=200,y=100)

window.mainloop()