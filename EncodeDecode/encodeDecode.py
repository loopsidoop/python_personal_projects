from tkinter import *
import base64

window = Tk()
window.geometry("840x600")

label = Label(window, text ='ENCODE DECODE', font = ("Arial",12,"bold"))
label.pack()

# Variables to be used
message, private_key, mode, result, = "","","",""

def Encode(key,message):
    enc=[]

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)

window.mainloop()