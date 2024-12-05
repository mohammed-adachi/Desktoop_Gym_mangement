import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import requests

def submit_form():
    # Collecter les données
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    dob = entry_dob.get()
    cin = entry_cin.get()
    profession = entry_profession.get()
    address = entry_address.get("1.0", tk.END).strip()
    phone = entry_phone.get()
    sport_type = combo_sport.get()
    photo_path = entry_photo.get()

    # Envoyer les données au backend Django
    if first_name and last_name and cin and phone and sport_type:
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": dob,
            "cin": cin,
            "profession": profession,
            "address": address,
            "phone": phone,
            "sport_type": sport_type,
        }
        files = {"photo": open(photo_path, "rb")} if photo_path else None
        response = requests.post("http://127.0.0.1:8000/api/members/", data=data, files=files)
        if response.status_code == 201:
            tk.messagebox.showinfo("Success", "Member added successfully!")
        else:
            tk.messagebox.showerror("Error", f"Failed to add member: {response.text}")
    else:
        tk.messagebox.showerror("Error", "Please fill all required fields.")

# Fenêtre principale
root = tk.Tk()
root.title("Gym Management System - Add Member")
root.geometry("600x600")

# Champs de formulaire
tk.Label(root, text="First Name:").grid(row=0, column=0, pady=5)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1)

tk.Label(root, text="Last Name:").grid(row=1, column=0, pady=5)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1)

tk.Label(root, text="Date of Birth (YYYY-MM-DD):").grid(row=2, column=0, pady=5)
entry_dob = tk.Entry(root)
entry_dob.grid(row=2, column=1)

tk.Label(root, text="CIN:").grid(row=3, column=0, pady=5)
entry_cin = tk.Entry(root)
entry_cin.grid(row=3, column=1)

tk.Label(root, text="Profession:").grid(row=4, column=0, pady=5)
entry_profession = tk.Entry(root)
entry_profession.grid(row=4, column=1)

tk.Label(root, text="Address:").grid(row=5, column=0, pady=5)
entry_address = tk.Text(root, height=4, width=30)
entry_address.grid(row=5, column=1)

tk.Label(root, text="Phone:").grid(row=6, column=0, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=6, column=1)

tk.Label(root, text="Type of Sport:").grid(row=7, column=0, pady=5)
combo_sport = ttk.Combobox(root, values=["Fitness", "Yoga", "Boxing", "Swimming", "Other"])
combo_sport.grid(row=7, column=1)

tk.Label(root, text="Photo:").grid(row=8, column=0, pady=5)
entry_photo = tk.Entry(root)
entry_photo.grid(row=8, column=1)
tk.Button(root, text="Browse", command=lambda: entry_photo.insert(0, filedialog.askopenfilename())).grid(row=8, column=2)

# Bouton de soumission
tk.Button(root, text="Submit", command=submit_form).grid(row=9, column=1, pady=20)

# Lancer l'application
root.mainloop()
