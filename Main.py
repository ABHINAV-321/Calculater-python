from tkinter import *

class Calculater:
    def __init__(self):
        window =Tk()

        window.geometry("500x500")
        window.config(width=500,height=500,bg='#BDEDFF')
        window.title('Calculater')
        label =Label(window,text='Answer',justify="right",anchor='e',padx=10,pady=20,width=23,height=0-5,font=('Ariel',15),borderwidth=25,border=3,relief='sunken')
        label.place(x=50,y=5)

        #buttons

       # button= Button(window,text=9,width=8,height=4,foreground='red',font=('italic',15)).grid(row=2,column=0,padx=15)
        button = Button(window, text=8, width=8, height=4, foreground='red', font=('italic', 15)).grid(row=2, column=2,  padx=15)
        button7 = Button(window, text=7, width=8, height=4, foreground='red', font=('italic', 15)).grid(row=2, column=3,padx=15)


        window.mainloop()

calc=Calculater()