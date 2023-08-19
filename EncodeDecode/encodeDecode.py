from tkinter import *
import base64

window = Tk()

label = Label(window, text ='ENCODE DECODE', font = ("Arial",12,"bold"))
label.grid(row=0, column=0,columnspan=2)

# Variables to be used
message = StringVar()
private_key = StringVar()
result = StringVar()

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

def activate_encode():
    result.set(Encode(private_key.get(), message.get()))
def activate_decode():
    result.set(Decode(private_key.get(), message.get()))
        
message_label = Label(window, text="Message", font=("Arial",14)).grid(row=1,column=0)  
message_entry = Entry(window, font=("Arial", 10), textvariable = message).grid(row=1,column=1)

key_label = Label(window, text="Private Key", font=("Arial",14))
key_label.grid(row=2,column=0)   

key_entry = Entry(window, font=("Arial", 10), textvariable = private_key)
key_entry.grid(row=2,column=1)

mode_encode = Button(window, text="Encode", command = activate_encode, font=("Arial",10)).grid(row=2,column=2)
mode_decode = Button(window, text="Decode", command = activate_decode, font=("Arial",10)).grid(row=2,column=3)

result_label = Label(window, text="Result", font=("Arial", 14)).grid(row=3,column=0)
final_result = Entry(window, textvariable=result).grid(row=3,column=1)

window.mainloop()