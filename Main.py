from tkinter import *
value2 =''
op_clicked = None
value1 = ""

def add_value( value):
    print('checking')
    global value1
    if op_clicked==None:
        value1+=value
        label.config(text=value1)
        print("value 1 " + value1)
    else:
        global value2
        value2 = value
        text=label.cget(key="text")
        label.config(text=text+value)
        print("value 2 " + value2)
def operater_clicked(value):
    global op_clicked
    op_clicked=value
    label.config(text=value1+value)

def find_answer ():
    if op_clicked == ' / ':
        ans = int(value1)+int(value2)
        print (ans)
        label.config(text=ans)


def start():

    window =Tk()
    window.geometry("500x500")
    window.config(width=500,height=500,bg='#BDEDFF')
    window.title('Calculater')
    global label
    label =Label(window,text='Answer',justify="right",anchor='e',padx=10,pady=20,width=35,height=0-5,font=('Ariel',15),borderwidth=25,border=3,relief='sunken')
    label.grid(row=00,columnspan=20,padx=10,pady=10)


    #setting buttons in frame

    button9= Button(window,text=9,width=4, height=2,font=('italic', 25),foreground='red',command=lambda :add_value("9")).grid(row=1,column=0,padx=7)
    button8 = Button(window, text=8, width=4, height=2,font=('italic', 25), foreground='red', command=lambda :add_value("8")).grid(row=1, column=2,  padx=7)
    button7 = Button(window, text=7, width=4, height=2,font=('italic', 25),  foreground='red', command=lambda :add_value("7")).grid(row=1, column=3,padx=7)
    button8 = Button(window, text='/', width=4, height=2, font=('italic', 25), foreground='red',command=lambda: operater_clicked(" / ")).grid(row=1, column=4, padx=7)
    button6= Button(window, text=6, width=4, height=2,font=('italic', 25), foreground='red',command=lambda :add_value("6")).grid(row=2, column=0,padx=7)
    button5 = Button(window, text=5,width=4, height=2,font=('italic', 25), foreground='red',command=lambda :add_value("5")).grid(row=2, column=2,padx=7)
    button4 = Button(window, text=4, width=4, height=2,font=('italic', 25),  foreground='red',command=lambda :add_value("4")).grid(row=2, column=3,padx=7)
    button8 = Button(window, text='*', width=4, height=2, font=('italic', 25), foreground='red',command=lambda: operater_clicked(" * ")).grid(row=2, column=4, padx=7)
    button3 = Button(window, text=3, width=4, height=2,font=('italic', 25),  foreground='red',command=lambda :add_value("3")).grid(row=3, column=0,padx=7)
    button2 = Button(window, text=2, width=4, height=2,font=('italic', 25), foreground='red',command=lambda :add_value("2")).grid(row=3, column=2,padx=7)
    button1 = Button(window, text=1, width=4, height=2,font=('italic', 25),  foreground='red',command=lambda :add_value("1")).grid(row=3, column=3,padx=7)
    button8 = Button(window, text='+', width=4, height=2, font=('italic', 25), foreground='red',command=lambda: operater_clicked(" + ")).grid(row=3, column=4, padx=7)

    Button(window, text='', width=4, height=2, font=('italic', 25), foreground='red',
           command=lambda: add_value("")).grid(row=4, column=0, padx=7)
    Button(window, text=0, width=4, height=2, font=('italic', 25), foreground='red',
           command=lambda: add_value("0")).grid(row=4, column=2, padx=7)
    Button(window, text='=', width=4, height=2,background='green', font=('italic', 25), foreground='red',
                     command=lambda: find_answer()).grid(row=4, column=3, padx=7)
    Button(window, text='-', width=4, height=2, font=('italic', 25), foreground='red',
           command=lambda: operater_clicked(" - ")).grid(row=4, column=4, padx=7)

    window.mainloop()
start()
