from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"







# SETTING UP UI


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")

canvas.create_image(400,263,image=front_image)
canvas.grid(row=0,column=0,columnspan=2)



right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1,column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1,column=0)


window.mainloop()