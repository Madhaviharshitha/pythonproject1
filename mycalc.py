import tkinter as tk
window=tk.Tk()
window.geometry('300x400')
window.title('calc')

a=tk.StringVar()
b=tk.StringVar()
c=tk.StringVar()

lblnum1=tk.Label(window,text='num')
lblnum1.place(x=100,y=100)
txtnum1=tk.Entry(window,textvariable=a)
txtnum1.place(x=200,y=100)

lblnum2=tk.Label(window,text='num2')
lblnum2.place(x=100,y=150)
txtnum2=tk.Entry(window,textvariable=b)
txtnum2.place(x=200,y=150)

lblnum3=tk.Label(window,text='result')
lblnum3.place(x=100,y=200)
txtnum3=tk.Entry(window,state=tk.DISABLED,textvariable=c)
txtnum3.place(x=200,y=200)

def add():
    m=int(a.get())+int(b.get())
    c.set(str(m))

def clear():
    a.set('')
    b.set('')
    c.set('')

btnadd=tk.Button(window,text='Add',command=add)
btnadd.place(x=100,y=250)

btncancel=tk.Button(window,text='cancel',command=clear)
btncancel.place(x=200,y=250)

window.mainloop()
