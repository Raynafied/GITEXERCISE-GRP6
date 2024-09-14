# first part tkinter testing
#from tkinter import*

#window = Tk()
#window.geometry('500x500')
#window.title('Female Fitness App')

#window.mainloop()

#2nd testing for labels
from tkinter import*

window = Tk()
window.geometry('500x500')
window.title('Female Fitness App')

label = Label(window,text='Welcome, Please enter your name gorgeous!')
label.place(x=100,y=200)

window.mainloop()