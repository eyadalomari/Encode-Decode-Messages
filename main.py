import tkinter as tk
import base64
from tkinter import ttk
from tkinter import scrolledtext
  
root = tk.Tk()
background_color = 'LightBlue3'
root.geometry('1024x768')
root.resizable(0,0)
root.title("DataFlair - Message Encode and Decode")
root.configure(background=background_color)

tk.Label(root, text = "Encode Decode Messages", bg=background_color, font = "arial 20 bold").pack()

Text = tk.Text(root,  bg = 'ghost white', height=10, width=80)
private_key = tk.StringVar()
mode = tk.StringVar()
Result = tk.Text(root,  bg = 'ghost white', height=10, width=80)

def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

def Mode():
    Result.configure(state='normal')
    
    Result.delete('1.0', tk.END)
    if v.get() == 'encryption':
        Result.insert(tk.INSERT, Encode(private_key.get(), retrieve_message()))

    elif v.get() == 'decryption':
        Result.insert(tk.INSERT, Decode(private_key.get(), retrieve_message()))
    Result.configure(state='disabled')

def Exit():
    root.destroy()

def Reset():
    Text.delete('1.0', tk.END)
    private_key.set("")

    Result.configure(state='normal')
    Result.delete('1.0', tk.END)
    Result.configure(state='disabled')

def retrieve_message():
    inputValue=Text.get("1.0","end-1c")
    return inputValue

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)





tk.Label(root, bg=background_color, font= 'arial 12 bold', text='MESSAGE').place(x= 30,y=130)

Text.place(x=220, y = 60)
scroll = tk.Scrollbar(root, command=Text.yview)
Text.configure(yscrollcommand=scroll.set)

tk.Label(root, bg=background_color, font = 'arial 12 bold', text ='KEY').place(x=30, y = 250)
tk.Entry(root,bg = 'ghost white', font = 'arial 10', textvariable = private_key, width=91).place(x=220, y = 250)

tk.Label(root, bg=background_color, font = 'arial 12 bold', text ='MODE').place(x=30, y = 300)


v = tk.StringVar()
v.set("encryption")

values = {
    "ENCODE" : "encryption",
    "DECODE" : "decryption",
}
index = 10
for (text, value) in values.items():
    radio = tk.Radiobutton(root,bg=background_color, text = text, variable = v, value = value).place(x=210 + index,y=300)
    index = index + 100





tk.Button(root, font = 'arial 10 bold', text = 'RESULT',width =15  ,padx =2,bg ='LimeGreen' ,command = Mode).place(x=30, y = 430)
Result.place(x=220, y = 370)
scroll = tk.Scrollbar(root, command=Result.yview)
Result.configure(yscrollcommand=scroll.set, state=tk.DISABLED)


tk.Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =20, command = Reset,bg = 'SkyBlue1', padx=2).place(x=130, y = 650)
tk.Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 20, command = Exit,bg = 'red4', padx=2, pady=2).place(x=680, y = 650)

root.mainloop()
