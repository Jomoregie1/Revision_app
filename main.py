import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import json



class Quiz:

    def __init__(self):
        self.question_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opt_selected = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(question)
        self.correct = 0

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f" Wrong: {wrong_count}"

        score = int((self.correct / self.data_size) * 100)
        result = f"Score: {score}%"

        mb.showinfo("Result", f"{result} \n {correct} \n {wrong}")

    def display_title(self):
        title = Label(window, text="Revision Quiz",
                      width=50, bg="blue", fg="white", font=("ariel", 20, "bold"))

        title.place(x=0, y=2)

    def display_question(self):
        pass

    def next_button(self):
        pass

    def previous_button(self):
        pass

    def check_answer(self):
        pass

    def radio_buttons(self):
        pass

    def display_options(self):
        pass

    def buttons(self):
        pass


window = tkinter.Tk()
window.geometry("800x450")
window.title("Revision Quiz")
frm = ttk.Frame(window)
quiz = Quiz()
window.mainloop()
