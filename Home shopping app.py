from atexit import register
from re import T
from tabnanny import check
from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Home Shopping App")
root.geometry("600x470")

def register():
    print("Registered")
    fnameValue_text = fnameValue.get()
    lnameValue_text = lnameValue.get()
    emailValue_text = emailValue.get()
    confirmemailValue_text = confirmemailValue.get()
    phoneValue_text = phoneValue.get()
    passwordValue_text = passwordValue.get()
    confirmpasswordValue_text = confirmpasswordValue.get()
    if fnameValue_text == "":
        screen1 = Toplevel(root)
        screen1.geometry("150x90")
        screen1.title("Warning!")
        Label(screen1, text = "First name required").pack()

Label(root,text="Registration form",font="arial 25").pack(pady=50)

Label(root,text="First name",font=25).place(x=100, y=150)
Label(root,text="Last name",font=25).place(x=100, y=200)
Label(root,text="E-mail address",font=25).place(x=100, y=250)
Label(root,text="Confirm e-mail address",font=25).place(x=100, y=300)
Label(root,text="Phone number",font=25).place(x=100, y=350)
Label(root,text="Create password",font=25).place(x=100, y=400)
Label(root,text="Re-type password",font=25).place(x=100, y=450)

#entry
fnameValue = StringVar()
lnameValue=StringVar()
emailValue=StringVar()
confirmemailValue=IntVar()
phoneValue=IntVar()
passwordValue=StringVar()
confirmpasswordValue=StringVar()

fnameEntry=Entry(root,textvariable=fnameValue,width=30,bd=2,font=20)
lnameEntry=Entry(root,textvariable=lnameValue,width=30,bd=2,font=20)
emailEntry=Entry(root,textvariable=emailValue,width=30,bd=2,font=20)
confirmemailEntry=Entry(root,textvariable=confirmemailValue,width=30,bd=2,font=20)
phoneEntry=Entry(root,textvariable=phoneValue,width=30,bd=2,font=20)
passwordEntry=Entry(root,textvariable=passwordValue,width=30,bd=2,font=20)
confirmpasswordEntry=Entry(root,textvariable=confirmpasswordValue,width=30,bd=2,font=20)

fnameEntry.place(x=200,y=150)
lnameEntry.place(x=200,y=200)
emailEntry.place(x=240,y=250)
confirmemailEntry.place(x=310,y=300)
phoneEntry.place(x=240,y=350)
passwordEntry.place(x=270,y=400)
confirmpasswordEntry.place(x=270,y=450)

#check button
checkValue=IntVar
checkbtn=Checkbutton(text="Remember Me?",variable=checkValue)
checkbtn.place(x=250,y=500)

Button(text="Register",font=20,width=11,height=2,command=register).place(x=250,y=550)


root.mainloop()