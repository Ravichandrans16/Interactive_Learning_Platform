from tkinter import *
import pymysql as m
from tkinter import messagebox
w = Tk()
w.geometry("679x452")
pic2 = PhotoImage(file="img/img1.png")
x1 = Label(w, image=pic2)
x1.place(x=0, y=0)
def log():

    a3 = Label(w, text="LOGIN", font=("cavolini", 20), bg=None, fg='black')
    a3.place(x=230, y=30)
    a1 = Label(w, text="Email", font=("French Script MT", 20), bg=None, fg="black")
    a1.place(x=100, y=100)
    b1 = Entry(w, width=30)
    b1.place(x=300, y=100)
    a2 = Label(w, text="password", font=("French Script MT", 20), bg=None, fg="black")
    a2.place(x=100, y=150)
    b2 = Entry(w, width=30)
    b2.place(x=300, y=150)

    def login1():
        A = b1.get()
        B = b2.get()
        check = (A, B)
        db = m.connect(host="localhost", user="root", password="Ravisg@2001$", db="db7")
        cur = db.cursor()
        cur.execute("SELECT * FROM tb2")
        found = False
        for i in cur.fetchall():
            if i[0] == A and i[1] == B:
                found = True
                break
        if found:
            def select():
                w.destroy()
                import choice
                
            select()

        else:
            messagebox.showerror("Login unsuccessful", "Invalid credentials")

    btn = Button(w, text="Login", bd=10, command=login1)
    btn.place(x=300, y=350)
    w.mainloop()
    

log()
