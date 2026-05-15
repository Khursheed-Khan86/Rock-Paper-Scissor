from tkinter import StringVar
from tkinter import Button
from tkinter import Label
from tkinter import * 
import random 

screen = Tk() 

screen.geometry("500x500")
screen.maxsize(500,500)
screen.title("ROCK PAPER SCISSOR GAME")
screen.configure(background="#b39ddb")

user_selected_tk = StringVar()
user_selected_tk.set("PENDING")
user_score_tk=StringVar()
result_tk=StringVar()

computer_selected_tk = StringVar()
computer_selected_tk.set("PENDING")

computer_score_tk=StringVar()
user_count_tk=IntVar()
computer_count_tk=IntVar()
user_count=0
computer_count=0
def game(userChoice):
    global user_selected_tk,computer_selected_tk,user_score_tk,computer_score_tk,result_tk,user_count_tk,computer_count_tk,user_count,computer_count
    #print(userChoice)
    
    user_selected_tk.set(userChoice)
    game_list = ["ROCK","PAPER","SCISSOR"]
    computer_choice = random.choice(game_list)
    #print("--> COMPUTER CHOICE ::: ",computer_choice)
    computer_selected_tk.set(computer_choice)
    if userChoice!=computer_choice:
        if userChoice=="ROCK":
            if computer_choice=="PAPER":
                user_score_tk.set(0)
                computer_score_tk.set(1)
                result_tk.set("COMPUTER GOT ONE POINT")
                computer_count+=1
                computer_count_tk.set(computer_count)
            elif computer_choice=="SCISSOR":
               user_score_tk.set(1)
               computer_score_tk.set(0)
               result_tk.set("  USER GOT ONE POINT")
               user_count+=1
               user_count_tk.set(user_count)
        elif userChoice=="PAPER":
            if computer_choice=="SCISSOR":
                user_score_tk.set(0)
                computer_score_tk.set(1)
                result_tk.set("COMPUTER GOT ONE POINT")
                computer_count+=1
                computer_count_tk.set(computer_count)
            elif computer_choice=="ROCK":
               user_score_tk.set(1)
               computer_score_tk.set(0)
               result_tk.set("  USER GOT ONE POINT")
               user_count+=1
               user_count_tk.set(user_count)
        elif userChoice=="SCISSOR":
            if computer_choice=="ROCK":
                user_score_tk.set(0)
                computer_score_tk.set(1)
                result_tk.set("COMPUTER GOT ONE POINT")
                computer_count+=1
                computer_count_tk.set(computer_count)
            elif computer_choice=="PAPER":
               user_score_tk.set(1)
               computer_score_tk.set(0)
               result_tk.set("   USER GOT ONE POINT")
               user_count+=1
               user_count_tk.set(user_count)
    else:
        user_score_tk.set("TIE")
        computer_score_tk.set("TIE")
        result_tk.set("              TIE")
    
     


label = Label(screen,text="ROCK PAPER SCISSOR GAME",font=('arial',16,'bold'),bg="#b39ddb")
label.pack()

btn1 = Button(screen,text="ROCK",font=('arial',16,'bold'),bg="#3f51b5",fg="white",activebackground="#5e35b1",activeforeground="white",command=lambda :game("ROCK"),height=1,width=9)
btn1.place(x=40,y=60)

btn2 = Button(screen,text="PAPER",font=('arial',16,'bold'),bg="#3f51b5",fg="white",activebackground="#5e35b1",activeforeground="white",command=lambda : game("PAPER"),height=1,width=9)
btn2.place(x=190,y=60)

btn3 = Button(screen,text="SCISSOR",font=('arial',16,'bold'),bg="#3f51b5",fg="white",activebackground="#5e35b1",activeforeground="white",command=lambda : game("SCISSOR"),height=1,width=9)
btn3.place(x=340,y=60)


# -------------begin::: user panel -----------------------

# user panel
user = Button(screen,text="USER",font=('arial',16,'bold'),bg="#ef6c00",fg="white",activebackground="#5e35b1",activeforeground="white",height=1,width=9)
user.place(x=40,y=140)

# user selected choice
user = Button(screen,textvariable=user_selected_tk,font=('arial',16,'bold'),bg="#ef6c00",fg="white",activebackground="#5e35b1",activeforeground="white",height=1,width=9)
user.place(x=190,y=140)

# user score 
user_s = Button(screen,textvariable=user_score_tk,font=('arial',16,'bold'),bg="#ef6c00",fg="white",activebackground="#5e35b1",activeforeground="white",height=1,width=9)
user_s.place(x=340,y=140)


# -------------end :: user panel -----------------------


# -------------begin :: computer panel -----------------------


# computer panel
computer = Button(screen,text="COMPUTER",font=('arial',16,'bold'),bg="#7c4dff",fg="white",activebackground="#5e35b1",activeforeground="white",height=1,width=9)
computer.place(x=40,y=240)

# computer selected choice
computer = Button(screen,textvariable=computer_selected_tk,font=('arial',16,'bold'),bg="#7c4dff",fg="white",activebackground="#5e35b1",activeforeground="white",height=1,width=9)
computer.place(x=190,y=240)

# computer score 
computer_s = Button(screen,textvariable=computer_score_tk,font=('arial',16,'bold'),bg="#7c4dff",fg="white",activebackground="#5e35b1",activeforeground="white",height=1,width=9)
computer_s.place(x=340,y=240)

# -------------end :: computer panel -----------------------

#--------------------result label---------------------
lbl_result=Label(screen,textvariable=result_tk,font=('arial',16,'bold'),bg="#b39ddb")
lbl_result.place(x=110,y=350)

#------------------begin-score panel--------------------------
lbl1=Label(screen,text="USER SCORE: ",font=('arial',16,'bold'),bg="white",width=24)
lbl1.place(x=60,y=400)

lbl2=Label(screen,textvariable=user_count_tk,font=('arial',16,'bold'),bg="white",width=8)
lbl2.place(x=320,y=400)

lbl3=Label(screen,text="COMPUTER SCORE: ",font=('arial',16,'bold'),bg="white",width=24)
lbl3.place(x=60,y=440)

lbl4=Label(screen,textvariable=computer_count_tk,font=('arial',16,'bold'),bg="white",width=8)
lbl4.place(x=320,y=440)
#------------------end- score panel-------------------------------

screen.mainloop()
