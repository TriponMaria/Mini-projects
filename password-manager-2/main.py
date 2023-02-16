from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if password == "" or email == "" or website == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as f:
                # Reading the old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            try:
                # Updating old data with new data
                data.update(new_data)
            except KeyError:
                pass
            with open("data.json", "w") as f:
                # Saving updated data
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            website_entry.focus()
            password_entry.delete(0, END)


# ---------------------------- FIND EMAIL AND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            websites = list(data.keys())
            if website in websites:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email:{email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for the website: {website} exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
mypass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1)
email_entry = Entry(width=50)
email_entry.insert(0, "maria@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3)
add = Button(text="Add", width=43, command=save)
add.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()



