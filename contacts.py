import tkinter as tk
from tkinter import messagebox
import json
import os 

# File to store contacts
CONTACTS_FILE= "contacts.json" 

# Function to load contacts from JSON file
def load_contacts():
    if os.path.exists("contacts.json"):
     with open("contacts.json","r")as f:
        return json.load(f)
    return[]
    
# Function to save contacts
def save_contacts(contacts):
    with open("contacts.json","w")as f:
        json.dump(contacts,f ,indent=4)
        
contacts= load_contacts()        
root= tk.Tk()
root.title("Simple Contact Book")
root.state("zoomed")
root.config(bg="#d1c4e9") 
BG_COLOR = "#d1c4e9"   
BTN_COLOR = "#8e24aa"  
ENTRY_COLOR = "#ede7f6"  
TEXT_COLOR = "#4a148c" 
frame = tk.Frame(root,  bg="#f0f1ff",width=900,height=700)
frame.place(relx=0.5, rely=0.5, anchor="center") 

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=2)

tk.Label(frame, text=" My Contact Book", font=("Arial", 24, "bold"),
         bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, columnspan=2, pady=20)

# Labels & Entry fields
tk.Label(frame, text="Name:", font=("Arial", 14, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(frame, font=("Arial", 14), bg=ENTRY_COLOR, fg="black", insertbackground="black", width=40)
name_entry.grid(row=1, column=1, padx=20, pady=20)

tk.Label(frame, text="Phone:", font=("Arial", 14, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, padx=15, pady=(0,10), sticky="e")
phone_entry = tk.Entry(frame, font=("Arial", 14), bg=ENTRY_COLOR, fg="black", insertbackground="black", width=40)
phone_entry.grid(row=2, column=1, padx=15, pady=(0,10))
    
# Function to add contacts
def add_contacts():
    global contacts
    name=name_entry.get().strip()
    phone=phone_entry.get().strip()
    if not name or not phone:
        messagebox.showwarning("Input error","Both fields are required!")
        return 
    contacts.append({"name": name , "phone": phone})
    save_contacts(contacts)
    messagebox.showinfo("Success",f"Contact {name} added!")
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    
# Function to view all contacts
def view_contacts():
    global contacts
    if not contacts:
        messagebox.showinfo("Contacts","No contacts available.")
        return
    all_contacts="\n".join([f"{c['name']} - {c['phone']}" for c in contacts])
    messagebox.showinfo("Contacts", all_contacts)
button_frame = tk.Frame(frame, bg="#f0f1ff")
button_frame.grid(row=3, column=0, columnspan=2, pady=20)

# Function to delete contacts
def delete_contact():
    global contacts
    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning("Input Error", "Enter the name of the contact to delete.")
        return

    # Find contact by name
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            messagebox.showinfo("Success", f"Contact {name} deleted!")
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            return

    messagebox.showwarning("Not Found", f"No contact found with name: {name}")

tk.Button(button_frame, text="Add Contact", font=("Arial", 12),
          command=add_contacts, width=15, bg="#934CAF", fg="white", activebackground="#a04568").pack(side="left", padx=10)
tk.Button(button_frame, text="View Contacts", font=("Arial", 12), 
          command=view_contacts, width=15, bg="#934CAF", fg="white", activebackground="#a04568").pack(side="left", padx=10)
tk.Button(button_frame, text="Delete Contact", font=("Arial", 12),
          command=delete_contact, width=15, bg="#934CAF", fg="white", activebackground="#a04568").pack(side="left", padx=10)
root.mainloop()

if __name__=="__main__":
    print("Running contact book...")
    
    