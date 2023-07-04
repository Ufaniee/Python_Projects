from tkinter import *
import math

#define the mathematical operations
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def lcm(a,b):
    l=a if a>b else b
    while l<=a*b and l%b ==0:
        return l
    l+=1
def hcf(a,b):
    h= a if a<b else b
    while h>=1:
        if a%h ==0 and b%h==0:
            return h
        h-=1
def sqrt(a):
    return math.sqrt(a)
    


# define operations that'll be substituted for each words
operations={"ADD": add, "ADDITTION":add, "SUM":add, "PLUS":add,
            "SUB":sub,"DIFFERENCE":sub,"MINUS":sub,"SUBTRACT":sub,
            "LCM":lcm,"HCF":hcf, "SQRT":sqrt,
            "PRODUCT":mul,"MULTIPLICATION":mul,"MULTIPLY":mul,
            "DIVISION":div,"DIVIDE":div,"DIV":div,"DIVIDE":div,
            "MOD":mod,"REMAINDER":mod,"MODULUS":mod}

#def a func that'll extract a particular word from a sentence
def extract_from_text(text):
    l=[]
    for t in text.split(" "):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l 

def calculate():
     text=textin.get()
     for word in text.split(" "):
        if word.upper() in operations.keys():
            try:
                l=extract_from_text(text)
                r = operations[word.upper()](l[0],l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,"something went wrong,Please enter again")
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,"something went wrong,Please enter again")


#create the window
win = Tk()

#create the geometry
win.geometry("500x400")

#window title
win.title('smart Calculator')
#background color
win.configure(bg="lightskyblue")

#create the labels
l1=Label(win,text="I am a Smart Calculator", width=20,padx=3)
l1.place(x=150,y=10)
l2=Label(win,text="My Name is Anie", width=20)
l2.place(x=150,y=40)
l3=Label(win,text="What can i do for you?", width=20,padx=3)
l3.place(x=150,y=130)

#create a variabale for entries
textin=StringVar()
e1=Entry(win,width=30,textvariable=textin)
e1.place(x=133,y=160)

#create a button
b1=Button(win,text="Just this?", command=calculate)
b1.place(x=210,y=200)

#create the box for display
list=Listbox(win,width=30,height=3)
list.place(x=150,y=230)


#create the end button
c1=Button(win,text="Close",bg="crimson",width=12,command=win.destroy)
c1.place(x=190,y=300)


#open window
win.mainloop()