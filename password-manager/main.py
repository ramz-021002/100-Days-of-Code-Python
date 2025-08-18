from tkinter import *
from tkinter import messagebox
import generate_password as gen
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    password_generated = gen.generate()
    password_entry.insert(0,password_generated)
    pyperclip.copy(password_generated)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password_text = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password_text) == 0:
        messagebox.showerror(title="Error", message="Please fill all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"Email address: {email}\n Password: {password}\n Is it Ok to save?")
        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)


website_entry = Entry(width=35)
website_entry.grid(column=1, row=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2,columnspan=2)
email_entry.insert(0, "test@test.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
generate_password_button = Button(text="Generate Password",command=password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1, row=4,columnspan=2)
window.mainloop()