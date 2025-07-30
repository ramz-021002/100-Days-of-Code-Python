from tkinter import *

def convert():
    m = miles.get()
    km = round(float(m) * 1.609)
    km_result.config(text=f"{km}")


window = Tk()
window.title("First GUI")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles = Entry(width=10)
miles.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)


is_equal_label = Label(text="Is equal to")
is_equal_label.grid(row=1, column=0)

km_result = Label(text="0")
km_result.grid(row=1, column=1)

km_text = Label(text="Km")
km_text.grid(row=1, column=2)

calculate_button = Button(text="Calculate",command=convert)
calculate_button.grid(row=2, column=1)



window.mainloop()


# my_label = Label(window, text="First GUI", font=("Sego UI", 20, "bold"))
# # my_label.pack()
# # my_label.place(x=100, y=100)
# my_label.grid(column=0, row=0)
#
# my_label["text"] = "This is my label"
# my_label.config(text="New Text")
# my_label.config(padx=50, pady=50)
# new_button = Button(window, text="New Button", command=button_clicked)
# new_button.grid(column=2, row=0)
#
# button = Button(text="Click Me",command=button_clicked)
# # button.place(x=100, y=250)
# # button.pack()
# button.grid(column=1, row=1)
#
# user_input = Entry(width=15)
# # user_input.place(x=100, y=200)
# # user_input.pack()
# user_input.grid(column=3, row=2)