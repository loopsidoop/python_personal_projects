from tkinter import *
import random

window = Tk()
window.geometry('500x200')
window.resizable(0,0)

def rand_upper_let():
    return chr(random.randint(65,90))
def rand_lower_let():
    return chr(random.randint(97,122))
def rand_dig():
    return chr(random.randint(48,57))
def rand_punc():
    return chr(random.randint(32,47))

def password_gen(length):
    password = ""
    while len(password) < length:
        options = (rand_upper_let(), rand_lower_let(), rand_dig(), rand_punc())
        password += random.choice(options)
    return password

pass_length = IntVar()
userPassword = StringVar()

def activate_password_gen():
    userPassword.set(password_gen(pass_length.get()))

Label(window, text="Password Generator", font=("Arial", 14, 'bold')).pack()

message_label = Label(window, text="Password Length", font=("Arial",11,'bold')).place(x=60,y=45)
message_entry = Entry(window, font=("Arial", 10), textvariable = pass_length,bg = 'ghost white').place(x=220,y=45)

generate = Button(window, text="GENERATE PASSWORD",font=("Arial",12,'bold'), command = activate_password_gen).place(x=150,y=80)
final_result = Entry(window, textvariable=userPassword, width=30, bg ='ghost white').place(x=158,y=120)

window.mainloop()