from tkinter import *
gui=Tk()

gui.title("khalid's calculator")

gui.geometry("320x490")
gui.configure(background='black')

titleLabel=Label(gui,text="KHalid's calculator",fg="blue",font=("Arial 20 bold"))

titleLabel.grid(columnspan=4)
experession_Field=  Entry(gui)
experession_Field.grid(columnspan=4,padx=20, pady=20,ipadx=80,ipady=20)

btn_devvv=Button(gui,text='%',height=4,width=10)
btn_devvv.grid(row=2,column=0)

btn_sqr=Button(gui,text='^2',height=4,width=10)
btn_sqr.grid(row=2,column=1)

btn_clear=Button(gui,text='AC',height=4,width=10)
btn_clear.grid(row=2,column=2)

btn_delete=Button(gui,text='Delete',height=4,width=10)
btn_delete.grid(row=2,column=3)

btn1=Button(gui,text='1',height=4,width=10)
btn1.grid(row=3,column=0)

btn2=Button(gui,text='2',height=4,width=10)
btn2.grid(row=3,column=1)

btn3=Button(gui,text='3',height=4,width=10)
btn3.grid(row=3,column=2)

btn_add=Button(gui,text='+',height=4,width=10)
btn_add.grid(row=3,column=3)

btn4=Button(gui,text='4',height=4,width=10)
btn4.grid(row=4,column=0)

btn5=Button(gui,text='5',height=4,width=10)
btn5.grid(row=4,column=1)

btn6=Button(gui,text='6',height=4,width=10)
btn6.grid(row=4,column=2)

btn_sub=Button(gui,text='-',height=4,width=10)
btn_sub.grid(row=4,column=3)
                 
btn7=Button(gui,text='7',height=4,width=10)
btn7.grid(row=5,column=0)

btn8=Button(gui,text='8',height=4,width=10)
btn8.grid(row=5,column=1)

btn9=Button(gui,text='9',height=4,width=10)
btn9.grid(row=5,column=2)

btn_mul=Button(gui,text='*',height=4,width=10)
btn_mul.grid(row=5,column=3)

btn0=Button(gui,text='0',height=4,width=10)
btn0.grid(row=6,column=0)

btn_comma=Button(gui,text='.',height=4,width=10)
btn_comma.grid(row=6,column=1)

btn_equal=Button(gui,text='=',height=4,width=10)
btn_equal.grid(row=6,column=2)

btn_dev=Button(gui,text='/',bg="gold",fg="white",height=4,width=10)
btn_dev.grid(row=6,column=3)

gui.mainloop()