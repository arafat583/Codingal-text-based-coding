from tkinter import *
from tkinter import messagebox
#from PIL import Image, ImageTk

root = Tk()
root.title("Denomination counter")
root.configure(bg="Light blue")
root.geometry("650x400")


#upload = Image.open("calculator.png")
#upload = upload.resize((300, 300))
#image = ImageTk.PhotoImage(upload)

#label = Label(root, image=image, bg="light blue")
#label.place(x=180, y=20)

label1 = Label(root, text="Hey user! Welcome to denomination calculator application,", bg="light blue")
label1.place(relx=0.5, y=348, anchor=CENTER)

def msg():
    MsgBox = messagebox.askquestion("Alert", "Do you want to calculate the denomination count?")
    if MsgBox == "yes":
        topwin()

button1 = Button(root, text="Let's get started!", bg="brown", fg="white", command=msg)
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="Light gray")
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg="Light grey")
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg="light grey")

    l1 = Label(top, text="1000", bg="Light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            amount = int(entry.get())
            note1000 = amount // 1000
            amount %= 1000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note1000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    btn = Button(top, text="Calculate", command=calculator, bg="brown", fg="white")

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

root.mainloop()
