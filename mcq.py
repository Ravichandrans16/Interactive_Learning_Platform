from tkinter import *

def mcq():
    def py():
        w.destroy()
        import pymcq
        
    def java():
        w.destroy()
        import javamcq
        
    def sql():
        w.destroy()
        import sqlmcq
        

    w = Tk()
    w.geometry("679x452")
    pic1 = PhotoImage(file="img/6img.png")
    w.iconphoto(True, pic1)
    pic2 = PhotoImage(file="img/img1.png")
    x1 = Label(w, image=pic2)
    x1.place(x=0, y=0)



    python_button = Button(w, text="python_mcq", command=py, width=25, height=2)
    python_button.pack(pady=20)
    python_button.place(x=230, y=100)

    java_button = Button(w, text="java_mcq", command=java, width=25, height=2)
    java_button.pack(pady=20)
    java_button.place(x=230, y=200)

    sql_button = Button(w, text="sql_mcq", command=sql, width=25, height=2)
    sql_button.pack(pady=20)
    sql_button.place(x=230, y=300)

    w.mainloop()
mcq()
