from tkinter import Tk, HIDDEN,NORMAL,Canvas

def toggle_eyes():
    current_color=c.itemcget(eye_left,'fill')
    new_color= c.body_color if current_color =='white' else 'white'
    current_state=c.itemcget(pupil_left,'state')
    new_state= NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfig(pupil_left,state=new_state)
    c.itemconfig(pupil_right,state=new_state)
    c.itemconfig(eye_left,fill=new_color)
    c.itemconfig(eye_right,fill=new_color)

def blink():
    toggle_eyes()
    win.after(250,toggle_eyes)
    win.after(3000,blink)

def toggle_pupils():
    if not c.crossed_eyes:
        c.move(pupil_left,10,-5)
        c.move(pupil_right,-10,-5)
        c.crossed_eyes = True
    else:
        c.move(pupil_left,-10,5)
        c.move(pupil_right,10,5)
        c.crossed_eyes =False

def toggle_tongue():
    if not c.tongue_out:
        c.itemconfig(tongue_tip,state= NORMAL)
        c.itemconfig(tongue_main,state= NORMAL)
        c.tongue_out = True
    else:
        c.itemconfig(tongue_tip,state= NORMAL)
        c.itemconfig(tongue_main,state= NORMAL)
        c.tongue_out = False

def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    win.after(1000,toggle_tongue)
    win.after(1000,toggle_pupils)
    return

def show_happy(event):
    if (20<= event.x and event.x < 350) and (20 <= event.y and event.y <= 350):
        c.itemconfig(cheek_left,state=NORMAL)
        c.itemconfig(cheek_right,state=NORMAL)
        c.itemconfig(mouth_happy,state=NORMAL)
        c.itemconfig(mouth_normal,state=HIDDEN)
        c.itemconfig(mouth_sad,state=HIDDEN)
        c.happy_level =10
    return

def hide_happy(event):
    c.itemconfig(cheek_left,state=HIDDEN)
    c.itemconfig(cheek_right,state=HIDDEN)
    c.itemconfig(mouth_happy,state=HIDDEN)
    c.itemconfig(mouth_normal,state=NORMAL)
    c.itemconfig(mouth_sad,state=NORMAL)
    c.happy_level =10
    return

def sad():
    if c.happy_level==0:
        c.itemconfig(mouth_happy,state=HIDDEN)
        c.itemconfig(mouth_normal,state=HIDDEN)
        c.itemconfig(mouth_sad,state=NORMAL)
    else:
        c.happy_level -=1
    win.after(500,sad)

        




#create the window
win= Tk()

#create the canvas template for drawing
c= Canvas(win,width=400,height=400)
c.configure(bg='black',highlightthickness=0)


#create the body color
c.body_color = 'Skyblue'
#shape of the cat
body = c.create_oval(35,20,365,350,outline=c.body_color,fill=c.body_color)

#create the leg
foot_left=c.create_oval(65,320,145,360, outline=c.body_color, fill=c.body_color)
foot_left=c.create_oval(250,320,330,360, outline=c.body_color, fill=c.body_color)

#create the ears
ear_left =c.create_polygon(75,80,75,10,165,70, outline=c.body_color, fill=c.body_color)
ear_right =c.create_polygon(225,45,325,10,320,70, outline=c.body_color, fill=c.body_color)

#create the eyes
eye_left= c.create_oval(130,110,160,170,outline='black', fill='white')
pupil_left=c.create_oval(140,145,150,155,outline='black', fill='black')
eye_right= c.create_oval(230,110,260,170,outline='black', fill='white')
pupil_right=c.create_oval(240,145,250,155,outline='black', fill='black')

#create the mouth
mouth_normal= c.create_line(170,250,200,272,230,250,smooth=1,width=2,state=NORMAL)

mouth_happy =c.create_line(170,250,200,282,230,250,smooth=1,width=2,state=HIDDEN)

mouth_sad = c.create_line(170,250,200,232,230,250,smooth=1,width=2,state=HIDDEN)

#create the tongue
tongue_main= c.create_rectangle(170,250,230,290,outline='red', fill='red',state=HIDDEN )
tongue_tip= c.create_oval(170,285,230,300,outline='red', fill='red' ,state=HIDDEN)

#create the cheek
cheek_left= c.create_oval(70,180,120,230,outline='pink', fill='pink',state=HIDDEN)
cheek_right= c.create_oval(280,180,330,230,outline='pink', fill='pink',state=HIDDEN)




c.pack()
c.bind('<Motion>', show_happy)
c.bind('<Leave>',hide_happy)
c.bind('<Double - 1 >',cheeky)

c.crossed_eyes =False
c.tongue_out= False
c.happy_level= 0
win.after(1000,blink)
win.after(5000,sad)
#run the window
win.mainloop()