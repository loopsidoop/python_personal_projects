import random
from tkinter import *

window = Tk()
window.geometry('400x200')
window.resizable(0,0)
window.title("Krypto Generator")

def krypto_generate():
    krypto_possibilities = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10,
                            11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    krypto_list = []
    while len(krypto_list) < 6:
        krypto = random.choice(krypto_possibilities) # finds a random number in the list
        krypto_possibilities.remove(krypto) # removes the number from the list
        krypto_list.append(str(krypto))
    return krypto_list

title = Label(window, text="Krypto Generator", font=("Arial", 14, 'bold')).pack()

window.mainloop()