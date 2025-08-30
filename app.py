from database import add_password
import tkinter as tk
from typing import List
widgets: List[tk.Widget] = []






root = tk.Tk()
root.title("PassGuard")
root.geometry("500x400")
root.configure(bg="#222222") 

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

logo = tk.PhotoImage(file="Logo.png.png")
logo = logo.subsample(4)
logo_label = tk.Label(root, image=logo, bg="#222222")
logo_label.grid(row=0, column=0, columnspan=2, pady=(20, 10), sticky="nsew")

website_label = tk.Label(root, text="Website:", bg="#222222", fg="#f0f0f0", font=("Segoe UI", 12))
website_label.grid(row=1, column=0, sticky="e", padx=(40,10), pady=8)
website_entry = tk.Entry(root, bg="#333333", fg="#f0f0f0", font=("Segoe UI", 12), insertbackground="#f0f0f0", width=28, relief="flat")
website_entry.grid(row=1, column=1, sticky="w", padx=(10,40), pady=8)

username_label = tk.Label(root, text="Username:", bg="#222222", fg="#f0f0f0", font=("Segoe UI", 12))
username_label.grid(row=2, column=0, sticky="e", padx=(40,10), pady=8)
username_entry = tk.Entry(root, bg="#333333", fg="#f0f0f0", font=("Segoe UI", 12), insertbackground="#f0f0f0", width=28, relief="flat")
username_entry.grid(row=2, column=1, sticky="w", padx=(10,40), pady=8)

password_label = tk.Label(root, text="Password:", bg="#222222", fg="#f0f0f0", font=("Segoe UI", 12))
password_label.grid(row=3, column=0, sticky="e", padx=(40,10), pady=8)
password_entry = tk.Entry(root, show="*", bg="#333333", fg="#f0f0f0", font=("Segoe UI", 12), insertbackground="#f0f0f0", width=28, relief="flat")
password_entry.grid(row=3, column=1, sticky="w", padx=(10,40), pady=8)

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    add_password(website, username, password)
    print(f"Saved: Website={website}, Username={username}")

save_btn = tk.Button(root, text="Save", command=save, bg="#0078D7", fg="white", font=("Segoe UI", 12), relief="flat", padx=20, pady=5, activebackground="#005fa3")
save_btn.grid(row=4, column=0, columnspan=2, pady=18, sticky="nsew")

root.mainloop()