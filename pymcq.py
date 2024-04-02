from tkinter import *
import tkinter as tk
import random

def pymcq():
    def check_answer(answer, correct_answer, marks):
        if answer == correct_answer:
            marks += 1
        return marks

    class MCQ:
        def __init__(self):
            self.marks = 0
            self.current_question = 1
            self.questions = random.sample([
                {
                    "question": " What is the maximum possible length of an identifier?\nA).16\nB).32\nC).64\nD).None of these",
                    "correct_answer": "D"
                },
                {
                    "question": " In which language is Python written?\nA).English\nB).PHP\nC).C\nD).All of the above",
                    "correct_answer": "C"
                },
                {
                    "question": " What do we use to define a block of code in Python language?\nA).Key\nB).Brackets\nC).Indentation\nD).None of these",
                    "correct_answer": "C"
                },
                {
                    "question": " Which one of the following has the same precedence level?\nA).Division, Power, Multiplication, Addition and Subtraction\nB).Division and Multiplication\nC).Subtraction and Division\nD).Power and Division",
                    "correct_answer": "B"
                },
                {
                    "question": " Which of the following commands will create a list?\nA). list1 = list()\nB). list1 = []\nC). list1 = list([1, 2, 3])\nD). all of the mentioned",
                    "correct_answer": "D"
                },
                {
                    "question": " What is the output when we execute list(“hello”)?\nA). [‘h’, ‘e’, ‘l’, ‘l’, ‘o’]\nB). [‘hello’]\nC). [‘llo’]\nD). [‘olleh’]",
                    "correct_answer": "A"
                },
                {
                    "question": "Suppose list1 is [1, 5, 9], what is sum(list1)?\nA). 1\nB). 9\nC). 15\nD). Error",
                    "correct_answer": "C"
                },
                {
                    "question": " Suppose t = (1, 2, 4, 3), which of the following is incorrect?\nA). print(t[3])\nB). t[3] = 45\nC). print(max(t))\nD). print(len(t)",
                    "correct_answer": "B"
                },
                {
                    "question": " What will be the output of the following Python code?\n>>>t=(1,2,4,3)\n>>>t[1:-1]\nA). (1, 2)\nB). (1, 2, 4)\nC). (2, 4)\nD). (2, 4, 3)",
                    "correct_answer": "C"
                },
                {
                    "question": " What will be the output of the following Python code?\n>>>t = (1, 2)\n>>>2 * t\nA). (1, 2, 1, 2)\nB). [1, 2, 1, 2]\nC). (1, 1, 2, 2)\nD). [1, 1, 2, 2]",
                    "correct_answer": "A"
                },
                {
                    "question": " Which one of the following has the same precedence level?\nA).Division, Power, Multiplication, Addition and Subtraction\nB).Division and Multiplication\nC).Subtraction and Division\nD).Power and Division",
                    "correct_answer": "B"
                },
                {
                    "question": " Which of the following commands will create a list?\nA). list1 = list()\nB). list1 = []\nC). list1 = list([1, 2, 3])\nD). all of the mentioned",
                    "correct_answer": "D"
                },
                {
                    "question": " What is the output when we execute list(“hello”)?\nA). [‘h’, ‘e’, ‘l’, ‘l’, ‘o’]\nB). [‘hello’]\nC). [‘llo’]\nD). [‘olleh’]",
                    "correct_answer": "A"
                },
                {
                    "question": " Suppose list1 is [1, 5, 9], what is sum(list1)?\nA). 1\nB). 9\nC). 15\nD). Error",
                    "correct_answer": "C"
                },
                {
                    "question": " Suppose t = (1, 2, 4, 3), which of the following is incorrect?\nA). print(t[3])\nB). t[3] = 45\nC). print(max(t))\nD). print(len(t)",
                    "correct_answer": "B"
                    }
            ], 10)
            self.root = tk.Tk()
            self.root.geometry("679x452")
            self.root.title("Python MCQ")
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

    mcq = MCQ()
    mcq.root.mainloop()
pymcq()
