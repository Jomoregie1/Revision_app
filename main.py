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

    def display_title(self):
        pass

    def display_question(self):
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
window.mainloop()
