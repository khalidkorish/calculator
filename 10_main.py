from tkinter import *
gui=Tk()

gui.title("calculator")

gui.geometry("320x490")

titleLabel=Label(gui,text="calculator",fg="blue",font=("Arial 20 bold"))

titleLabel.grid(columnspan=4)

equation=StringVar()
experession_Field=  Entry(gui,textvariable=equation)
experession_Field.grid(columnspan=4,padx=20, pady=20,ipadx=80,ipady=20)

user_view=''

def press(user_input) :
    global user_view 
    user_view+=str(user_input)
    equation.set(user_view)

def epual_press():
    global user_view
    if user_view!='' :
        result= str(eval(user_view))
        equation.set(result)
        user_view=""
    else :
        clear()

def clear():
    global user_view
    user_view=''
    equation.set(user_view)

def delete():
    global user_view
    lista=list(user_view)
    if lista !=[]:
        lista.pop()
    else:
        clear()
    result=""
    for i in range(len(lista)):
        result+=lista[i]
    equation.set(result)
    user_view=result
    
def square():
    global user_view
    result=str(eval(user_view)*eval(user_view))
    equation.set(result)
    user_view=""
    
        


btn_devvv=Button(gui,text='%',command=lambda:press("%"),height=4,width=10)
btn_devvv.grid(row=2,column=0)

btn_sqr=Button(gui,text='^2',command=square,height=4,width=10)
btn_sqr.grid(row=2,column=1)

btn_clear=Button(gui,text='AC',command=clear,height=4,width=10)
btn_clear.grid(row=2,column=2)

btn_delete=Button(gui,text='Delete',command=delete,height=4,width=10)
btn_delete.grid(row=2,column=3)

btn1=Button(gui,text='1',command=lambda:press(1),height=4,width=10)
btn1.grid(row=3,column=0)

btn2=Button(gui,text='2',command=lambda:press(2),height=4,width=10)
btn2.grid(row=3,column=1)

btn3=Button(gui,text='3',command=lambda:press(3),height=4,width=10)
btn3.grid(row=3,column=2)

btn_add=Button(gui,text='+',command=lambda:press("+"),height=4,width=10)
btn_add.grid(row=3,column=3)

btn4=Button(gui,text='4',command=lambda:press(4),height=4,width=10)
btn4.grid(row=4,column=0)

btn5=Button(gui,text='5',command=lambda:press(5),height=4,width=10)
btn5.grid(row=4,column=1)

btn6=Button(gui,text='6',command=lambda:press(6),height=4,width=10)
btn6.grid(row=4,column=2)

btn_sub=Button(gui,text='-',command=lambda:press("-"),height=4,width=10)
btn_sub.grid(row=4,column=3)
                 
btn7=Button(gui,text='7',command=lambda:press(7),height=4,width=10)
btn7.grid(row=5,column=0)

btn8=Button(gui,text='8',command=lambda:press(8),height=4,width=10)
btn8.grid(row=5,column=1)

btn9=Button(gui,text='9',command=lambda:press(9),height=4,width=10)
btn9.grid(row=5,column=2)

btn_mul=Button(gui,text='*',command=lambda:press("*"),height=4,width=10)
btn_mul.grid(row=5,column=3)

btn0=Button(gui,text='0',command=lambda:press(0),height=4,width=10)
btn0.grid(row=6,column=0)

btn_comma=Button(gui,text='.',command=lambda:press("."),height=4,width=10)
btn_comma.grid(row=6,column=1)

btn_equal=Button(gui,text='=',command=epual_press,height=4,width=10)
btn_equal.grid(row=6,column=2)

btn_dev=Button(gui,text='/',command=lambda:press("/"),height=4,width=10)
btn_dev.grid(row=6,column=3)


gui.mainloop()