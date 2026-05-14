
import tkinter as tk
from tkinter import messagebox
import os
import re

# File to store contacts
CONTACT_FILE = "contacts.txt"

# ---------------- LOAD CONTACTS ---------------- #

def load_contacts():

    contacts = {}

    if os.path.exists(CONTACT_FILE):

        with open(CONTACT_FILE, "r") as file:

            for line in file:

                line = line.strip()

                if line and "," in line:

                    name, phone = line.split(",", 1)

                    if name in contacts:
                        contacts[name].append(phone)
                    else:
                        contacts[name] = [phone]

    return contacts


# ---------------- SAVE CONTACTS ---------------- #

def save_contacts(contacts):

    with open(CONTACT_FILE, "w") as file:

        for name, phones in contacts.items():

            for phone in phones:

                file.write(f"{name},{phone}\n")


# ---------------- ADD CONTACT ---------------- #

def add_contact():

    name = entry_name.get().strip()
    phone = entry_phone.get().strip()

    # Remove extra spaces
    name = " ".join(name.split())

  

    name_pattern = r"^[a-zA-Z\s]+$"
    phone_pattern = r"^\d{10}$"

    if re.match(name_pattern, name) and re.match(phone_pattern, phone):

        if name in contacts:

            # Prevent duplicate numbers
            if phone in contacts[name]:

                messagebox.showwarning(
                    "Duplicate",
                    "This number already exists!"
                )
                return

            contacts[name].append(phone)

        else:
            contacts[name] = [phone]

        save_contacts(contacts)

        messagebox.showinfo(
            "Success",
            f"Contact '{name}' added successfully!"
        )

        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)

    else:

        messagebox.showwarning(
            "Input Error",
            "Enter valid name and 10-digit phone number"
        )
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)


# ---------------- SEARCH BY NAME ---------------- #

def search_contact():

    name = entry_name.get().strip()

    # Remove extra spaces
    name = " ".join(name.split())



    if name == "":

        messagebox.showwarning(
            "Input Error",
            "Please enter name"
        )
        return

    if re.match(r"^[a-zA-Z\s]+$", name):

        if name in contacts:

            phones = "\n".join(contacts[name])

            messagebox.showinfo(
                "Contact Found",
                f"Name: {name}\n\nPhone Numbers:\n{phones}"
            )

        else:

            messagebox.showwarning(
                "Not Found",
                f"Contact '{name}' not found."
            )

    else:

        messagebox.showwarning(
            "Search Error",
            "Invalid input"
        )
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)


# ---------------- SEARCH BY PHONE ---------------- #

def search_by_phone():

    phone = entry_phone.get().strip()

    if phone == "":

        messagebox.showwarning(
            "Input Error",
            "Please enter phone number"
        )
        return

    found = False

    for name, phones in contacts.items():

        if phone in phones:

            messagebox.showinfo(
                "Contact Found",
                f"Phone Number: {phone}\nOwner: {name}"
            )

            found = True
            break

    if not found:

        messagebox.showwarning(
            "Not Found",
            "Phone number not found"
        )
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

# ---------------- UPDATE CONTACT ---------------- #

def update_contact():

    name = entry_name.get().strip()
    new_phone = entry_phone.get().strip()

    # Remove extra spaces
    name = " ".join(name.split())

    

    if name in contacts:

        if re.match(r"^\d{10}$", new_phone):

            contacts[name].append(new_phone)

            # Remove duplicates
            contacts[name] = list(set(contacts[name]))

            save_contacts(contacts)

            messagebox.showinfo(
                "Updated",
                f"New number added for {name}"
            )

        else:

            messagebox.showwarning(
                "Input Error",
                "Enter valid 10-digit number"
            )

    else:

        messagebox.showwarning(
            "Not Found",
            "Contact not found"
        )
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)


# ---------------- DELETE CONTACT ---------------- #

def delete_contact():

    name = entry_name.get().strip()
    phone = entry_phone.get().strip()

    # Remove extra spaces
    name = " ".join(name.split())

    

    if name in contacts:

        if phone in contacts[name]:

            contacts[name].remove(phone)

            # Remove contact if no numbers left
            if len(contacts[name]) == 0:
                del contacts[name]

            save_contacts(contacts)

            messagebox.showinfo(
                "Deleted",
                "Contact deleted successfully"
            )

        else:

            messagebox.showwarning(
                "Error",
                "Phone number not found"
            )

    else:

        messagebox.showwarning(
            "Error",
            "Contact not found"
        )
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)


# ---------------- DISPLAY CONTACTS ---------------- #

def display_contacts():

    display_window = tk.Toplevel(root)

    display_window.title("All Contacts")

    display_window.geometry("400x400")

    text_display = tk.Text(display_window)

    text_display.pack(expand=True, fill='both')

    # SORT CONTACTS ALPHABETICALLY
    for name in sorted(contacts):

        text_display.insert(
            tk.END,
            f"\nName: {name}\n"
        )

        for phone in contacts[name]:

            text_display.insert(
                tk.END,
                f"Phone: {phone}\n"
            )
    
# ---------------- MAIN ---------------- #

contacts = load_contacts()

root = tk.Tk()

root.title("Contact Book")

root.geometry("420x320")


# NAME
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root, width=25)
entry_name.grid(row=0, column=1, padx=10, pady=10)


# PHONE
label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=1, column=0, padx=10, pady=10)

entry_phone = tk.Entry(root, width=25)
entry_phone.grid(row=1, column=1, padx=10, pady=10)


# BUTTONS
btn_add = tk.Button(
    root,
    text="Add Contact",
    width=18,
    command=add_contact
)
btn_add.grid(row=2, column=0, padx=10, pady=10)


btn_delete = tk.Button(
    root,
    text="Delete Contact",
    width=18,
    command=delete_contact
)
btn_delete.grid(row=2, column=1, padx=10, pady=10)


btn_search = tk.Button(
    root,
    text="Search By Name",
    width=18,
    command=search_contact
)
btn_search.grid(row=3, column=0, padx=10, pady=10)


btn_phone_search = tk.Button(
    root,
    text="Search By Phone",
    width=18,
    command=search_by_phone
)
btn_phone_search.grid(row=3, column=1, padx=10, pady=10)


btn_update = tk.Button(
    root,
    text="Update Contact",
    width=18,
    command=update_contact
)
btn_update.grid(row=4, column=0, padx=10, pady=10)


btn_display = tk.Button(
    root,
    text="Display Contacts",
    width=18,
    command=display_contacts
)
btn_display.grid(row=4, column=1, padx=10, pady=10)


root.mainloop()