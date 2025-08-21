from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"


word = {}
# Reading the CSV file
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    #Converting Data Frame into a dictionary
    data_dict = data.to_dict(orient="records")

def flip():
    canvas.itemconfig(background_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word['English'], fill="white")


def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = choice(data_dict)
    canvas.itemconfig(background_image, image=front_image)
    canvas.itemconfig(card_title,text="French", fill='black')
    canvas.itemconfig(card_word, text=word['French'],fill='black')
    flip_timer = window.after(3000, func=flip)

def is_known():
    global data
    data_dict.remove(word)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# SETTING UP UI
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")

background_image = canvas.create_image(400,263,image=front_image)

card_title = canvas.create_text(400, 150, font=("Ariel",40,"italic"),fill="black")
card_word = canvas.create_text(400, 263, font=("Ariel", 40, "bold"), fill="black")

canvas.grid(row=0,column=0,columnspan=2)


right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1,column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,borderwidth=0, command=next_card)
wrong_button.grid(row=1,column=0)

next_card()

window.mainloop()