from tkinter import *

def choice():
    def home():
        w.destroy()
        import home

    def mcq():
        w.destroy()
        import mcq
        
    
    w = Tk()
    w.geometry("679x452")
    pic1 = PhotoImage(file="img/6img.png")
    w.iconphoto(True, pic1)
    pic2 = PhotoImage(file="img/img1.png")
    x1 = Label(w, image=pic2)
    x1.place(x=0, y=0)


    video_button = Button(w, text="Expert Session", command=home, width=25, height=2)
    video_button.pack(pady=20)
    video_button.place(x=230, y=100)

    mcq_button = Button(w, text="mcq", command=mcq, width=25, height=2)
    mcq_button.pack(pady=20)
    mcq_button.place(x=230, y=200)


    w.mainloop()
choice()