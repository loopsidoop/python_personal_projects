import random
from tkinter import *

window = Tk()
window.geometry('400x300')
window.resizable(0,0)
window.title("Krypto Generator")

title = Label(window, text="Krypto Generator", font=("Arial", 14, 'bold')).pack()
target_num = Label(window, text="1", font=("Calibri",25,'bold'),width=20,height=1, bg='ghost white',relief=SOLID).place(x=25,y=30)

num1 = Label(window, text="2", font=("Calibri",25,'bold'),width=3,height=1, bg='ghost white',relief=SOLID).place(x=25,y=80)
num2 = Label(window, text="2", font=("Calibri",25,'bold'),width=3,height=1, bg='ghost white',relief=SOLID).place(x=97,y=80)
num3 = Label(window, text="2", font=("Calibri",25,'bold'),width=3,height=1, bg='ghost white',relief=SOLID).place(x=169,y=80)
num4 = Label(window, text="2", font=("Calibri",25,'bold'),width=3,height=1, bg='ghost white',relief=SOLID).place(x=241,y=80)
num5 = Label(window, text="2", font=("Calibri",25,'bold'),width=3,height=1, bg='ghost white',relief=SOLID).place(x=313,y=80)

window.mainloop()