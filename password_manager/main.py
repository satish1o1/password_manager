from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    if len(password_entiry.get()) == 0:
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "m", "n", "o", "p", "q", "r", "s",
                   "t", "u", "v", "w", "x", "y", "z", ]
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        characters = ["!", "@", "#", "$", "%", "^", "&", "*", "-"]

        password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
        password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
        password_character = [random.choice(characters) for _ in range(random.randint(2, 4))]
        password_list = password_letters + password_numbers + password_character
        random.shuffle(password_list)
        password_e = "".join(password_list)
        password_entiry.insert(0, password_e)
    else:
        print("password is already there")


# --------------Search Website -------------- #

def search_key():
    website = web_entiry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Website",message="Website field shouldn't be empty")
    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
        except:
            print("file not found")

        else:
            if website in data:
                user_name = data[website]['name']
                password = data[website]["password"]
                messagebox.showinfo(title='data', message=f"User-Name :{user_name}\n"
                                                          f"Password :{password}")
            else:
                messagebox.showinfo(title="DETAILS", message=f"sorry {website} not exits")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entiry.get()
    user_name = user_entiry.get()
    password = password_entiry.get()
    new_data = {website: {
        "name": user_name,
        "password": password
    }
    }
    if website == "" or user_name == "" or password == "":
        messagebox.showerror(title="oh no ", message="Please make sure you haven't left any field empty")
    else:
        confirmation = messagebox.askyesno("conform  data", message=f"Website :{website} \n"
                 f"Username :{user_name} \n  Password :{password} \n are you sure you want save the data")
    if confirmation:
        try:
            with open('data.json', "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        except:
            with open('data.json', "w") as file:
                json.dump(new_data, file, indent=4)

        finally:
            web_entiry.delete(0, END)
            user_entiry.delete(0, END)
            password_entiry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=30, pady=30)
window.title("Password Manager")
canvas = Canvas(width=200, height=220)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# label sections
label_website = Label(text='Website')
label_website.grid(column=0, row=1)
label_username = Label(text='Username')
label_username.grid(column=0, row=2)
label_password = Label(text="Password")
label_password.grid(column=0, row=3)

# entiry_sectons
web_entiry = Entry(width=23)
web_entiry.grid(column=1, row=1, columnspan=1)
user_entiry = Entry(width=45)
user_entiry.grid(column=1, row=2, columnspan=2)
password_entiry = Entry(width=23)
password_entiry.grid(column=1, row=3)

# Button sections
search_button = Button(text='Search', width=17, command=search_key)
search_button.grid(row=1, column=2)
generator_butthon = Button(text="Generate password", command=generate_password)
generator_butthon.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", command=save_password, width=36)
add_button.grid(column=1, row=4, columnspan=3)

window.mainloop()
