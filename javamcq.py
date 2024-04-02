from tkinter import *
import tkinter as tk
import random
def java():
    def check_answer(answer, correct_answer, marks):
        if answer == correct_answer:
            marks += 1
        return marks

    class JAVAMCQ:
        def __init__(self):
            self.marks = 0
            self.current_question = 1
            self.questions = random.sample([
                {
                    "question": " Who invented Java Programming?\nA). Guido van Rossum\nB). James Gosling\nC). Dennis Ritchie\nD). Bjarne Stroustrup ",
                    "correct_answer": "B"
                },
                {
                    "question": " Which statement is true about Java?\nA). Java is a sequence-dependent programming language\nB). Java is a code dependent programming language\nC). Java is a platform-dependent programming language\nD). Java is a platform-independent programming language",
                    "correct_answer": "D"
                },
                {
                    "question": " Which component is used to compile, debug and execute the java programs?\nA). JRE\nB). JIT\nC). JDK\nD). JVM",
                    "correct_answer": "C"
                },
                {
                    "question": "Which one of the following is not a Java feature?\nA). Object-oriented\nB). Use of pointers\nC). Portable\nD). Dynamic and Extensible",
                    "correct_answer": "B"
                },
                {
                    "question": " Which of these cannot be used for a variable name in Java?\nA). identifier & keyword\nB). identifier\nC). keyword\nD). none of the mentioned",
                    "correct_answer": "C"
                },
                {
                    "question": " What will be the output of the following Java code?\nclass increment {\npublic static void main(String args[]) \n{        \nint g = 3;\nSystem.out.print(++g * 8);\n} \n}\nA). 32\nB). 33\nC). 24\nD). 25",
                    "correct_answer": "A"
                },
                {
                    "question": " Which environment variable is used to set the java path?\nA).MAVEN_Path\nB). JavaPATH\nC). JAVA\nD). JAVA_HOME",
                    "correct_answer": "D"
                },
                {
                    "question": " Which of the following is not an OOPS concept in Java?\nA). Polymorphism\nB). Inheritance\nC). Compilation\nD). Encapsulation",
                    "correct_answer": "C"
                },
                {
                    "question": " What is not the use of “this” keyword in Java?\nA). Referring to the instance variable when a local variable has the same name\nB). Passing itself to the method of the same class\nC). Passing itself to another method\nD). Calling another constructor in constructor chaining",
                    "correct_answer": "B"
                },
                {
                    "question": " What will be the error in the following Java code?\nbyte b = 50;\nb = b * 50;\nA). b cannot contain value 50\nB). b cannot contain value 100, limited by its range\nC). No error in this code\nD). * operator has converted b * 50 into int, which can not be converted to byte without casting",
                    "correct_answer": "D"
                },
                {
                    "question": " Who invented Java Programming?\nA). Guido van Rossum\nB). James Gosling\nC). Dennis Ritchie\nD). Bjarne Stroustrup ",
                    "correct_answer": "B"
                },
                {
                    "question": " Which statement is true about Java?\nA). Java is a sequence-dependent programming language\nB). Java is a code dependent programming language\nC). Java is a platform-dependent programming language\nD). Java is a platform-independent programming language",
                    "correct_answer": "D"
                },
                {
                    "question": " Which component is used to compile, debug and execute the java programs?\nA). JRE\nB). JIT\nC). JDK\nD). JVM",
                    "correct_answer": "C"
                },
                {
                    "question": " Which one of the following is not a Java feature?\nA). Object-oriented\nB). Use of pointers\nC). Portable\nD). Dynamic and Extensible",
                    "correct_answer": "B"
                },
                {
                    "question": " Which of these cannot be used for a variable name in Java?\nA). identifier & keyword\nB). identifier\nC). keyword\nD). none of the mentioned",
                    "correct_answer": "C"
                }
            ], 10)
            self.root = tk.Tk()
            self.root.geometry("679x452")
            self.root.title("JAVA MCQ")
            self.background_image = tk.PhotoImage(file="img/img1.png")
            self.background_label = tk.Label(self.root, image=self.background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.question_label = tk.Label(self.root, text=self.questions[self.current_question-1]["question"], font=("Arial", 14), justify="left")
            self.question_label.pack(pady=20)
            self.entry = tk.Entry(self.root, font=("Arial", 14))
            self.entry.bind("<Return>", lambda _: self.next_question())
            self.entry.pack(pady=10)
            self.submit_button = tk.Button(self.root, text="Submit Answer", font=("Arial", 14), command=self.next_question)
            self.submit_button.pack(pady=20)

        def next_question(self):
            answer = self.entry.get().upper()
            self.marks = check_answer(answer, self.questions[self.current_question-1]["correct_answer"], self.marks)
            self.entry.delete(0, tk.END)
            self.current_question += 1
            if self.current_question > len(self.questions):
                self.show_result()
            else:
                self.question_label.config(text=self.questions[self.current_question-1]["question"])

        def show_result(self):
            self.question_label.pack_forget()
            self.entry.pack_forget()
            self.submit_button.pack_forget()
            result_label = tk.Label(self.root, text=f"Your score is {self.marks}/{len(self.questions)}", font=("Arial", 20))
            result_label.pack(pady=100)
            if self.marks < 4:
                result = "YOUR MARK IS " + str(self.marks) + ", TRY TO IMPROVE"
            elif self.marks >= 4 and self.marks <= 7:
                result = "YOUR MARK IS " + str(self.marks) + ", GOOD, TRY TO BE BETTER"
            elif self.marks > 7:
                result = "YOUR MARK IS " + str(self.marks) + ", FANTASTIC"
            else:
                result = "INVALID MARKS"
            result_label2 = tk.Label(self.root, text=result, font=("Arial", 20))
            result_label2.pack(pady=20)

    mcq = JAVAMCQ()
    mcq.root.mainloop()
java()
