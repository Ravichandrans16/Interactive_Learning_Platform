from tkinter import *
from tkinter import *
import tkinter as tk
import random
def sql():
    def check_answer(answer, correct_answer, marks):
        if answer == correct_answer:
            marks += 1
        return marks

    class SQL_MCQ:
        def __init__(self):
            self.marks = 0
            self.current_question = 1
            self.questions = random.sample([
                {
                    "question": " Which SQL function is used to count the number of rows in a SQL query?\nA). COUNT()\nB). NUMBER()\nC). SUM()\nD). COUNT(*)",
                    "correct_answer": "D"
                },
                {
                    "question": " Which SQL keyword is used to retrieve a maximum value?\nA). MOST\nB). TOP\nC). MAX\nD). UPPER",
                    "correct_answer": "C"
                },
                {
                    "question": " Which of the following SQL clauses is used to DELETE tuples from a database table?\nA). DELETE\nB). REMOVE\nC). DROP\nD). CLEAR",
                    "correct_answer": "A"
                },
                {
                    "question": " ___________removes all rows from a table without logging the individual row deletions.\nA). DELETE\nB). REMOVE\nC). DROP\nD). TRUNCATE",
                    "correct_answer": "D"
                },
                {
                    "question": " Which of the following is not a DDL command?\nA). UPDATE\nB). TRUNCATE\nC). ALTER\nD). None of the Mentioned",
                    "correct_answer": "A"
                },
                {
                    "question": " Which of the following are TCL commands?\nA). UPDATE and TRUNCATE\nB). SELECT and INSERT\nC). GRANT and REVOKE\nD). ROLLBACK and SAVEPOINT",
                    "correct_answer": "D"
                },
                {
                    "question": " ________________ is not a category of SQL command.\nA). TCL\nB). SCL\nC). DCL\nD). DDL",
                    "correct_answer": "B"
                },
                {
                    "question": " If you don’t specify ASC or DESC after a SQL ORDER BY clause, the following is used by default ______________\nA). ASC\nB). DESC\nC). There is no default value\nD). None of the mentioned",
                    "correct_answer": "A"
                },
                {
                    "question": " Which of the following is not a DDL command?\nA). UPDATE\nB). TRUNCATE\nC). ALTER\nD). None of the Mentioned",
                    "correct_answer": "A"
                    
                },
                {
                    "question": " What is the purpose of the SQL AS clause?\nA). The AS SQL clause is used to change the name of a column in the result set or to assign a name to a derived column\nB). The AS clause is used with the JOIN clause only\nC).The AS clause defines a search condition\nD). All of the mentioned",
                    "correct_answer": "D"
                },
                {
                    "question": " Which of the following is not a DDL command?\nA). UPDATE\nB). TRUNCATE\nC). ALTER\nD). None of the Mentioned",
                    "correct_answer": "A"
                },
                {
                    "question": " Which of the following are TCL commands?\nA). UPDATE and TRUNCATE\nB). SELECT and INSERT\nC). GRANT and REVOKE\nD). ROLLBACK and SAVEPOINT",
                    "correct_answer": "D"
                },
                {
                    "question": " ________________ is not a category of SQL command.\nA). TCL\nB). SCL\nC). DCL\nD). DDL",
                    "correct_answer": "B"
                },
                {
                    "question": " If you don’t specify ASC or DESC after a SQL ORDER BY clause, the following is used by default ______________\nA). ASC\nB). DESC\nC). There is no default value\nD). None of the mentioned",
                    "correct_answer": "A"
                },
                {
                    "question": " Which of the following statement is true?\nA). DELETE does not free the space containing the table and TRUNCATE /nfree the space containing the table\nB). Both DELETE and TRUNCATE free the space containing the table\nC). Both DELETE and TRUNCATE does not free the space containing the table\nD). DELETE free the space containing the table and TRUNCATE does not free the space containing the table",
                    "correct_answer": "A"
                }
            ], 10)
            self.root = tk.Tk()
            self.root.geometry("900x452")
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

    mcq = SQL_MCQ()
    mcq.root.mainloop()
sql()