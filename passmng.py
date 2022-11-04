from tkinter import PhotoImage, Radiobutton, Tk, CENTER, Button, Label, Frame, LabelFrame, Entry, IntVar
import pymysql
import random

fonts=['Segoe UI Bold','Verdana']
bgcol = "#282c34"
#fgcol = "#979fad"
fgcol = "#f5fffa"
btncol = "#59626f"

window = Tk()
window.title("Password Manager")
icon = PhotoImage(file="lock.png")
window.iconphoto(False, icon)

# ALL FUNCTIONS
def urpass():
   print (entry1.get())

def randompass():
    passw=""
    for i in range(int(entry.get())):
        passw+=chr(random.randint(33,126))
    print (passw)

def genpass_radio():
    if var.get()==1:
        print ("Random Pass")
        for widget in window.winfo_children():
            widget.destroy()
        labelframe = LabelFrame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            fg = fgcol
            )
        labelframe.pack()
        label = Label(
            labelframe,
            text = "Enter the length of password",
            font = ("Verdana",17),
            bg = bgcol,
            fg = fgcol
            )
        label.pack(padx=10,pady=10)
        global entry
        entry = Entry(
            labelframe,
            font = ("Verdana",12),
            bg = bgcol,
            fg = fgcol
            )
        submitBtnRand = Button(
                labelframe,
                text="Submit",
                font= ("Verdana",12),
                bg = btncol,
                activebackground = btncol,
                command = randompass
                )
        entry.pack(padx=10,pady=10)
        submitBtnRand.pack(padx=10,pady=10)

    elif var.get()==2:
        for widget in window.winfo_children():
            widget.destroy()
        labelframe = LabelFrame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            fg = fgcol
            )
        labelframe.pack()
        label = Label(
            labelframe,
            text = "Enter your password",
            font = ("Verdana",17),
            bg = bgcol,
            fg = fgcol
            )
        label.pack(padx=10,pady=10)
        global entry1
        entry1 = Entry(
                labelframe,
                font = ("Verdana",12),
                bg = bgcol,
                fg = fgcol
                )
        entry1.pack(padx=10,pady=10)
        submitBtnUr = Button(
                labelframe,
                font = ("Verdana",10),
                text = "Submit",
                bg = btncol,
                activebackground= btncol,
                command = "urpass"
                )
        submitBtnUr.pack(padx=10,pady=10)

def create_submitBtn():   # this function takes software name as input and asks user if they want to generate a random pass
    softname = entry.get()
    print (softname)
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = LabelFrame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            fg = fgcol
            )

    labelframe.pack()
    label = Label(
            labelframe,
            text = "Do you want to generate a random password? ",
            font = ("Verdana",17),
            bg = bgcol,
            fg = fgcol
            )
    label.pack(padx=10,pady=10)
    label = Label(
        labelframe,
        text="",
        bg = bgcol
        )
    label.pack(padx=5,pady=5)
    global var
    var = IntVar()
    r1 = Radiobutton(
            labelframe,
            text = "Yes ",
            font = ("Verdana",10),
            variable = var,
            value = 1,
            relief="groove",
            command = genpass_radio,
            bg = btncol,
            activebackground=btncol,
            )
    r2 = Radiobutton(
            labelframe,
            text = "No ",
            font = ("Verdana",10),
            variable = var,
            relief="groove",
            value = 2,
            command = genpass_radio,
            bg = btncol,
            activebackground= btncol
            )
    r1.pack(padx=10,pady=10)
    r2.pack(padx=10,pady=10)

    label = Label(
        labelframe,
        text="",
        bg = bgcol
        )
    label.pack(padx=5,pady=5)

def createbtn():
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = LabelFrame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            fg = fgcol
            )
    labelframe.pack()
    label = Label(
            labelframe,
            text = "Enter the name of the software",
            font = ("Verdana",17),
            bg = bgcol,
            fg = fgcol
            )
    label.pack(padx=10,pady=10)
    global entry
    entry = Entry(
            labelframe,
            font = ("Verdana",12),
            bg = bgcol,
            fg = fgcol
            )
    entry.pack(padx=10,pady=10)
    submitBtn = Button(
            labelframe,
            text = "Submit",
            font = ("Verdana",10),
            relief="ridge",
            bg = btncol,
            activebackground=btncol,
            command = create_submitBtn
            )
    submitBtn.pack(padx=10,pady=10)

def exitfunc():
    window.destroy()

# FIRST PAGE (MAIN PAGE)
labelframe = LabelFrame(
        window,
        relief="raised",
        height=400,
        width=400,
        borderwidth=18,
        bg = bgcol,
        fg = fgcol,
        )
labelframe.pack()

label = Label (
        labelframe,
        text = "PASSWORD MANAGER",
        font = ("Rockwell",20),
        bg = bgcol,
        fg = fgcol
        )
label.pack(padx=15,pady=15)

createBtn = Button(
        labelframe,
        text = "Create",
        font = ("Britannic",10),
        relief="raised",
        command = createbtn,
        bg = btncol,
        activebackground=btncol
        )
updateBtn = Button(
        labelframe,
        text = "Update",
        font = ("Britannic",10),
        relief="raised",
        bg = btncol,
        activebackground=btncol
        )
deleteBtn = Button(
        labelframe,
        text = "Delete",
        font = ("Britannic",10),
        relief="raised",
        bg = btncol,
        activebackground=btncol
        )
displayBtn = Button(
        labelframe,
        text = "Display",
        font = ("Britannic",10),
        relief="raised",
        bg = btncol,
        activebackground=btncol
        )
exitBtn = Button(
        labelframe,
        text = "  Exit  ",
        font = ("Britannic",10),
        relief="raised",
        bg = bgcol,
        activebackground=bgcol,
        fg = fgcol,
        activeforeground= fgcol,
        command = exitfunc

        )
createBtn.pack(padx=10,pady=10)
updateBtn.pack(padx=10,pady=10)
deleteBtn.pack(padx=10,pady=10)
displayBtn.pack(padx=10,pady=10)
exitBtn.pack(padx=10,pady=10)

label = Label(
        labelframe,
        text="",
        bg = bgcol
        )
label.pack(padx=5,pady=5)


#CREATE PAGE






window.mainloop()

