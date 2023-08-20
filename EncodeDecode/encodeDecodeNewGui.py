from tkinter import *
import base64

window = Tk()
window.title("Encode and Decoder")
window.geometry("400x200")
window.resizable(0,0)

label = Label(window, text ='encrypt / decrypt', font = ("Arial",14,"bold")).pack()

# Variables to be used
message,private_key,result = StringVar(), StringVar(), StringVar()

# Encodes a message using base64 module
def Encode(key,message):
    enc=[]

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Decodes a message using base64 module
def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)

# For the encode and decode buttons to work
def activate_encode():
    result.set(Encode(private_key.get(), message.get()))    
def activate_decode():
    result.set(Decode(private_key.get(), message.get()))
    
# Boring GUI shit
        
message_label = Label(window, text="MESSAGE", font=("Arial",12,'bold')).place(x=60,y=45)
message_entry = Entry(window, font=("Arial", 10), textvariable = message,bg = 'ghost white').place(x=200,y=45)

key_label = Label(window, text="KEY", font=("Arial",12,'bold')).place(x=60, y=75)
key_entry = Entry(window, font=("Arial", 10), textvariable = private_key, bg ='ghost white').place(x=200,y=75)

mode_encode = Button(window, text="Encode", command = activate_encode, font=("Arial",10)).place(x=150,y=105)
mode_decode = Button(window, text="Decode", command = activate_decode, font=("Arial",10)).place(x=220,y=105)

result_label = Label(window, text="RESULT", bg ='ghost white', font=("Arial", 14))
final_result = Entry(window, textvariable=result).place(x=150,y=145)

window.mainloop()