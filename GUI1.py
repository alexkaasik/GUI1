from tkinter import*
from math import*

def anwser(event):
    global a
    global b
    global c
    a=ent1.get()
    b=ent2.get()
    c=ent3.get()
    #print(f"{a}\n{b}\n{c}")
    if bool(a)==False:
        ent1.configure(bg="red")
    else:
        ent1.configure(bg="light blue")
    if bool(b)==False:
        ent2.configure(bg="red")
    else:
        ent2.configure(bg="light blue")
    if bool(c)==False:
        ent3.configure(bg="red")
    else:
        ent3.configure(bg="light blue")
    square(event)

def square(event):
    import math

    global a
    global b
    global c
    if bool(a) and bool(b) and bool(c) == True:
        a1=int(a)
        b1=int(b)
        c1=int(c)
        d=int(b1**2-4*a1*c1)
        print(d)
        if d>0.0:
            x1=((-b1+(sqrt(d)))/(2*a1))
            x2=((-b1-(sqrt(d)))/(2*a1))
            N=(f"D={d}\nX1={x1}\nX2={x2}")
        elif d==0.0:
            x=(-b1/2*a1)
            x1=x
            x2=x
            N=(f"D={d}\nX1={x1}\nX2={x2}")
        else:
            N="false"
        l2.configure(text=N)
    else:
        l2.configure(text="false")

sup=Tk()
sup.title("Решение квадратного уравнения")
sup.geometry('600x200')
sup.iconbitmap('0001.ico')

btn1=Button(sup,text="Решить",bg="green",fg="black",font="Bold 23") #.pack(side=TOP) command=vajutamine()
btn1.place(x = 361,y = 54)
btn1.place(height=74, width=137,)

l1=Label(sup,text="Решение квадратного уравнения",height=4,width=13,bg="light blue",fg="black",font="Arial 25")
l1.place(x = 50,y = 0)
l1.place(height=48, width=500,)

l2=Label(sup,text="Решение",height=4,width=13,bg="YELLOW",fg="black",font="Arial 10")
l2.place(x = 87,y = 133)
l2.place(height=69, width=426,)

ent1=Entry(sup,bg="light blue",font="Arial 24")
ent1.place(x = 0,y = 69)
ent1.place(height=46, width=58)

l3=Label(sup,text="x**2+",height=4,width=13,fg="dark green",font="Arial 24")
l3.place(x = 69,y = 69)
l3.place(height=48, width=80,)

ent2=Entry(sup,bg="light blue",font="Arial 24")
ent2.place(x = 166,y = 69)
ent2.place(height=46, width=58)

l4=Label(sup,text="x+",height=4,width=13,fg="dark green",font="Arial 24")
l4.place(x = 224,y = 69)
l4.place(height=48, width=40,)

ent3=Entry(sup,bg="light blue",font="Arial 24")
ent3.place(x = 262,y = 69)
ent3.place(height=46, width=58)

l5=Label(sup,text="=0",height=4,width=13,fg="dark green",font="Arial 24")
l5.place(x = 318,y = 69)
l5.place(height=48, width=40,)

btn1.bind('<Button-1>',anwser)

sup.mainloop()