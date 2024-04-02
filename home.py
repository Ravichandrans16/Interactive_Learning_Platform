from tkinter import *
import webbrowser

def video():
    def open_python():
        w.destroy()
        webbrowser.open_new("https://www.youtube.com/watch?v=mhdExzt7AnU")

    def open_java():
        w.destroy()
        webbrowser.open_new("https://www.youtube.com/watch?v=XLnimroGCIg")

    def open_sql():
        w.destroy()
        webbrowser.open_new("https://www.youtube.com/watch?v=HXV3zeQKqGY")

    w = Tk()
    w.geometry("679x452")
    pic2 = PhotoImage(file="img/img1.png")
    x1 = Label(w, image=pic2)
    x1.place(x=0, y=0)
    text_label = Label(w, text="Expert Session", font=("Arial", 25))
    text_label.place(x=50, y=200)


    python_image = PhotoImage(file="D:\\tutorial1\\python.png")
    python_button = Button(w, command=open_python, compound="c", image=python_image)
    python_button.place(x=300, y=20)
    python_label = Label(w, text="Python", font=("Arial", 25))
    python_label.place(x=450, y=60)

    java_image = PhotoImage(file="D:\\tutorial1\\java.png")
    java_button = Button(w, command=open_java, compound="c", image=java_image)
    java_button.place(x=300, y=160)
    java_label = Label(w, text="java", font=("Arial", 25))
    java_label.place(x=450, y=200)


    sql_image = PhotoImage(file="D:\\tutorial1\\mysql.png")
    sql_button = Button(w,command=open_sql, compound="c", image=sql_image)
    sql_button.place(x=300, y=300)
    sql_label = Label(w, text="mysql", font=("Arial", 25))
    sql_label.place(x=450, y=340)


    w.mainloop()
video()

