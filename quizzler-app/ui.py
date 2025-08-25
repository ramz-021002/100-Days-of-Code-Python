from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.geometry("400x400")
        self.window.configure(background=THEME_COLOR)

        self.window.mainloop()

