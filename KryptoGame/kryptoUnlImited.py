"""
Difference between kryptoUnlimited.py and kryptop52cards.py

1. kryptoUnlimited.py
The deck shuffles back its cards everytime you press generate, ensuring the program randomly picks a card out of 52 cards.

2. kryptop52cards.py
The deck doesnt shuffle back its cards every time your press generate. This makes it so that every number in the deck is used 
before shuffling it back to 52 cards.

"""

import random
from tkinter import *

window = Tk()
window.geometry('400x250')
window.resizable(0,0)
window.title("Krypto Generator")
title = Label(window, text="Krypto Generator", font=("Arial", 14, 'bold')).pack()

target_num,num1,num2,num3,num4,num5 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

def gen_krypto():
    krypto_possibilities = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10,
                            11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    krypto_list = []
    while len(krypto_list) < 6:
        krypto = random.choice(krypto_possibilities) # finds a random number in the list
        krypto_possibilities.remove(krypto) # removes the number from the list
        krypto_list.append(str(krypto))
    target_num.set(krypto_list[5])
    num1.set(krypto_list[0])
    num2.set(krypto_list[1])
    num3.set(krypto_list[2])
    num4.set(krypto_list[3])
    num5.set(krypto_list[4])

target_num_label = Label(window, textvariable=target_num, font=("Calibri",25,'bold'),width=20,height=1, bg='ghost white',relief=SOLID).place(x=25,y=30)
num1_label = Label(window, textvariable=num1, font=("Calibri",25,'bold'),width=3,height=1, bg='ghost white',relief=SOLID).place(x=25,y=80)
num2_label = Label(window, textvariable=num2, font=("Calibri",25,'bold'),width=3,height=1, bg='ghost white',relief=SOLID).place(x=97,y=80)
num3_label = Label(window, textvariable=num3, font=("Calibri",25,'bold'),width=3,height=1, bg='ghost white',relief=SOLID).place(x=169,y=80)
num4_label = Label(window, textvariable=num4, font=("Calibri",25,'bold'),width=3,height=1, bg='ghost white',relief=SOLID).place(x=241,y=80)
num5_label = Label(window, textvariable=num5, font=("Calibri",25,'bold'),width=3,height=1, bg='ghost white',relief=SOLID).place(x=313,y=80)

button = Button(window, text="GENERATE", 
                command = gen_krypto,
                font=("Arial",20,'bold')).place(x=120,y=150)

window.mainloop()