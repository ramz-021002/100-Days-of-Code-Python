# from re import search
from tkinter import *
from tkinter import messagebox
import generate_password as gen
import pyperclip
import json
# ---------------------------- SEARCH USERNAME AND PASSWORD ------------------------------- #
def search_details():
    try:
        website = website_entry.get()
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data found")
    else:
        if website in data:
            messagebox.showinfo(title=website,
                                message=f"Email:{data[website]['email']}\n Password:{data[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    password_generated = gen.generate()
    password_entry.insert(0,password_generated)
    pyperclip.copy(password_generated)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def dump_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
def save():
    website = website_entry.get()
    email = email_entry.get()
    password_text = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password_text,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password_text) == 0:
        messagebox.showerror(title="Error", message="Please fill all the fields")
    else:
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)

        except FileNotFoundError:
            dump_data(new_data)

        else:
            data.update(new_data)
            dump_data(new_data)
        # json.load to read the contents, json.update to append the data(not overwrite), json.dump to flush the data into the file
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


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


website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search",width=13, command=search_details)
search_button.grid(column=2, row=1)


email_entry = Entry(width=39)
email_entry.grid(column=1, row=2,columnspan=2)
email_entry.insert(0, "test@test.com")


password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
generate_password_button = Button(text="Generate Password",width=13,command=password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1, row=4,columnspan=2)
window.mainloop()