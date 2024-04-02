from tkinter import *
def initial():
    def signup():
        w.destroy()
        import signup1
        
        
    def login1():
        w.destroy()
        import login
    

    w = Tk()
    w.geometry("679x452")raA
    pic1 = PhotoImage(file="img/6img.png")
    w.iconphoto(True, pic1)
    pic2 = PhotoImage(file="img/img1.png")
    x1 = Label(w, image=pic2)
    x1.place(x=0, y=0)
    text_label = Label(w, text="WELCOME TO CAREER DEVELOPMENT", font=("Arial", 25))
    text_label.place(x=25, y=100)

    signup_button = Button(w, text="Signup", command=signup, width=25, height=2)
    signup_button.pack(pady=20)
    signup_button.place(x=230, y=200)

    login_button = Button(w, text="Login", command=login1, width=25, height=2)
    login_button.pack(pady=20)
    login_button.place(x=230, y=300)

    w.mainloop()
initial()