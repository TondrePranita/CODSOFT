import random, string
from tkinter import *
import pyperclip

root =Tk()
root.geometry("340x380")
root.title("Password Generator")
root.iconbitmap("img.ico")
root.configure(bg="#31503e")

output_pass = StringVar()

all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase] 

def randPassGen():
    password = ""
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)   
        password = password + random.choice(char_type)
    
    output_pass.set(password)

def copyPass():
    pyperclip.copy(output_pass.get())

pass_head = Label(root, text = 'Enter Password Length', font = 'arial 12 bold',padx="5",pady="5").pack(pady="30 20") 

pass_len = IntVar() 
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 20, font='arial 16').pack()

Button(root, command = randPassGen, text = "Generate Password", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20, padx=20)

pass_label = Label(root, text = 'Password Generated', font = 'arial 12 bold',padx="5",pady="5").pack(pady="30 20")
Entry(root , textvariable = output_pass, width = 22, font='arial 16').pack()

Button(root, text = 'Copy to Clipboard', command = copyPass, font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

root.mainloop() 

