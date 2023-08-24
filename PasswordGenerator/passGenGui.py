"""
A simple password generator program
"""

from tkinter import *
import random

window = Tk()
window.geometry('500x200')
window.resizable(0,0)
window.title("Password Generator")

# Setting the variables
upperlet, lowerlet, digits, punc, pass_length = IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
userPassword = StringVar()

# The random letters, digits, and punctuations
def rand_upper_let():
    return chr(random.randint(65,90))
def rand_lower_let():
    return chr(random.randint(97,122))
def rand_dig():
    return chr(random.randint(48,57))
def rand_punc():
    return chr(random.randint(32,47))

# Generates the password with the indicated length
def password_gen(length):
    password = ""
    while len(password) < length:
        options = make_option_list() # Makes the list of possible choices based from the checkbox
        if len(options) == 0:
            return "Check at least 1 box"
        password += random.choice(options)
    return password

# To activate the password_gen func
def activate_password_gen():
    userPassword.set(password_gen(pass_length.get()))
   
# List of possible choices based from the checkbox 
def make_option_list():
    options = []
    if upperlet.get() == 1:
        options.append(rand_upper_let())
    if lowerlet.get() == 1:
        options.append(rand_lower_let())
    if digits.get() == 1:
        options.append(rand_dig())
    if punc.get() == 1:
        options.append(rand_punc())
    return options

# The GUI shit

Label(window, text="Password Generator", font=("Arial", 14, 'bold')).pack()

plength_label = Label(window, text="Password Length", font=("Arial",11,'bold')).place(x=60,y=45)
plength_entry = Entry(window, font=("Arial", 10), textvariable = pass_length,bg = 'ghost white').place(x=220,y=45)

check_upperlet = Checkbutton(window, text="Uppercase", variable=upperlet, onvalue=1, offvalue=0).place(x=60,y=70)
check_lowerlet = Checkbutton(window, text="Lowercase", variable=lowerlet, onvalue=1, offvalue=0).place(x=140,y=70)
check_digits = Checkbutton(window, text="Digits", variable=digits, onvalue=1, offvalue=0).place(x=220,y=70)
check_punc = Checkbutton(window, text="Punctuation", variable=punc, onvalue=1, offvalue=0).place(x=280,y=70)

generate = Button(window, text="GENERATE PASSWORD",font=("Arial",12,'bold'), command = activate_password_gen).place(x=150,y=100)
result = Entry(window, textvariable=userPassword, width=30, bg ='ghost white').place(x=158,y=140)

window.mainloop()