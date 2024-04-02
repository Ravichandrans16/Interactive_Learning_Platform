from tkinter import *
import pymysql as m
from tkinter import messagebox



# Create the main window


def signup():
    w = Tk()
    w.geometry("679x452")
    pic1 = PhotoImage(file="img/6img.png")
    w.iconphoto(True, pic1)
    pic2 = PhotoImage(file="img/img1.png")
    x1 = Label(w, image=pic2)
    x1.place(x=0, y=0)

    
    a8 = Label(w, text="REGISTER", font=("cavolini", 20), bg=None, fg='black')
    a8.place(x=230, y=50)
    a6 = Label(w, text="name", font=("French Script MT", 20), bg=None, fg="black")
    a6.place(x=50, y=100)
    b6 = Entry(w, width=30)
    b6.place(x=300, y=100)
    a2 = Label(w, text="mob_no", font=("French Script MT", 20), bg=None, fg="black")
    a2.place(x=50, y=150)
    b2 = Entry(w, width=30)
    b2.place(x=300, y=150)
    a3 = Label(w, text="course", font=("French Script MT", 20), bg=None, fg="black")
    a3.place(x=50, y=200)
    b3 = Entry(w, width=30)
    b3.place(x=300, y=200)
    a4 = Label(w, text="email", font=("French Script MT", 20), bg=None, fg="black")
    a4.place(x=50, y=250)
    b4 = Entry(w, width=30)
    b4.place(x=300, y=250)
    a5 = Label(w, text="password", font=("French Script MT", 20), bg=None, fg="black")
    a5.place(x=50, y=300)
    b5 = Entry(w, width=30)
    b5.place(x=300, y=300)


    def submit():
        name = b6.get()
        mob_no = b2.get()
        course = b3.get()
        email = b4.get()
        password = b5.get()
        if name == "" or mob_no == "" or course == "" or email == "" or password == "":
            messagebox.showerror("incomplete", "Please fill in all the required details")
            w.destroy()
        else:
            db = m.connect(host="localhost", user="root", password="Ravisg@2001$", db="db7")
            cur = db.cursor()
            cur.execute("insert into tb1 values ('" + name + "','" + mob_no + "','" + course + "','" + email + "','" + password + "')")
            cur.execute("insert into tb2 values ('" + email + "','" + password + "')")
            db.commit()
            def login():
                w.destroy()
                import login
                login.log()

            login()       

    btn = Button(w, text="REGISTER", bd=10, command=submit)
    btn.place(x=250, y=350)
    w.mainloop()




signup()
