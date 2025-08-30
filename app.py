import tkinter as tk

root = tk.Tk()
root.title("PassGuard Login")
root.geometry("400x300")
root.configure(bg="#222831")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

title_label = tk.Label(root, text="Login Page", bg="#222831", fg="#00adb5", font=("Segoe UI", 20, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10), sticky="nsew")

username_label = tk.Label(root, text="Username:", bg="#222831", fg="#eeeeee", font=("Segoe UI", 14))
username_label.grid(row=1, column=0, sticky="e", padx=(40, 10), pady=8)
username_entry = tk.Entry(root, bg="#393e46", fg="#eeeeee", font=("Segoe UI", 14), insertbackground="#eeeeee", relief="flat")
username_entry.grid(row=1, column=1, sticky="w", padx=(10, 40), pady=8)

password_label = tk.Label(root, text="Password:", bg="#222831", fg="#eeeeee", font=("Segoe UI", 14))
password_label.grid(row=2, column=0, sticky="e", padx=(40, 10), pady=8)
password_entry = tk.Entry(root, show="*", bg="#393e46", fg="#eeeeee", font=("Segoe UI", 14), insertbackground="#eeeeee", relief="flat")
password_entry.grid(row=2, column=1, sticky="w", padx=(10, 40), pady=8)


def open_password_manager():
    pm_window = tk.Toplevel(root)
    pm_window.title("PassGuard - Password Manager")
    pm_window.geometry("500x400")
    pm_window.configure(bg="#222222")

    for i in range(7):
        pm_window.grid_rowconfigure(i, weight=1)
    for i in range(2):
        pm_window.grid_columnconfigure(i, weight=1)

    title_label_pm = tk.Label(pm_window, text="Password Manager", bg="#222222", fg="#00adb5",
                              font=("Segoe UI", 18, "bold"))
    title_label_pm.grid(row=0, column=0, columnspan=2, pady=(20, 10), sticky="nsew")

    website_label = tk.Label(pm_window, text="Website:", bg="#222222", fg="#f0f0f0", font=("Segoe UI", 12))
    website_label.grid(row=1, column=0, sticky="e", padx=(40, 10), pady=8)
    website_entry = tk.Entry(pm_window, bg="#333333", fg="#f0f0f0", font=("Segoe UI", 12),
                             insertbackground="#f0f0f0", width=28, relief="flat")
    website_entry.grid(row=1, column=1, sticky="w", padx=(10, 40), pady=8)

    username_label_pm = tk.Label(pm_window, text="Username:", bg="#222222", fg="#f0f0f0", font=("Segoe UI", 12))
    username_label_pm.grid(row=2, column=0, sticky="e", padx=(40, 10), pady=8)
    username_entry_pm = tk.Entry(pm_window, bg="#333333", fg="#f0f0f0", font=("Segoe UI", 12),
                                 insertbackground="#f0f0f0", width=28, relief="flat")
    username_entry_pm.grid(row=2, column=1, sticky="w", padx=(10, 40), pady=8)

    password_label_pm = tk.Label(pm_window, text="Password:", bg="#222222", fg="#f0f0f0", font=("Segoe UI", 12))
    password_label_pm.grid(row=3, column=0, sticky="e", padx=(40, 10), pady=8)
    password_entry_pm = tk.Entry(pm_window, show="*", bg="#333333", fg="#f0f0f0", font=("Segoe UI", 12),
                                 insertbackground="#f0f0f0", width=28, relief="flat")
    password_entry_pm.grid(row=3, column=1, sticky="w", padx=(10, 40), pady=8)

    saved_passwords = []  
    del saved_passwords[:]

    def save():
        website = website_entry.get()
        username = username_entry_pm.get()
        password = password_entry_pm.get()
        if website and username and password:
            saved_passwords.append((website, username, password))
            print(f"Saved: Website={website}, Username={username}, Password={password}")
            website_entry.delete(0, tk.END)
            username_entry_pm.delete(0, tk.END)
            password_entry_pm.delete(0, tk.END)
        else:
            del saved_passwords[:]

    def show_passwords():
        show_window = tk.Toplevel(pm_window)
        show_window.title("Saved Passwords")
        show_window.geometry("400x300")
        show_window.configure(bg="#111")

        def refresh():
            for widget in show_window.winfo_children():
                widget.destroy()
            for idx, (site, user, pwd) in enumerate(saved_passwords, start=1):
                frame = tk.Frame(show_window, bg="#111")
                frame.pack(fill="x", padx=10, pady=5)
                tk.Label(frame, text=f"{idx}. {site} | {user} | {pwd}", bg="#111", fg="white", font=("Segoe UI", 12)).pack(side="left")
                def make_delete(index):
                    return lambda: (saved_passwords.pop(index), refresh())
                del_btn = tk.Button(frame, text="Delete", command=make_delete(idx-1), bg="#c40021", fg="white", font=("Segoe UI", 10, "bold"), relief="raised", padx=10)
                del_btn.pack(side="right")
        refresh()

    save_btn = tk.Button(pm_window, text="Save", command=save, bg="#0078D7", fg="white", font=("Segoe UI", 12),
                         relief="flat", padx=20, pady=5, activebackground="#005fa3")
    save_btn.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")

    show_btn = tk.Button(pm_window, text="Show Passwords", command=show_passwords,
                         bg="#21c400", fg="#222222", font=("Segoe UI", 14, "bold"),
                         relief="raised", padx=30, pady=10, activebackground="#1e9e00", bd=3)
    show_btn.grid(row=5, column=0, columnspan=2, pady=(10, 0), sticky="nsew")

    

    def on_close():
        root.deiconify()
        pm_window.destroy()

    pm_window.protocol("WM_DELETE_WINDOW", on_close)



def login():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Login attempt: {username}, Password: {password}")
    root.withdraw()
    open_password_manager()


login_button = tk.Button(root, text="Login", command=login, bg="#00adb5", fg="#222831",
                         font=("Segoe UI", 14, "bold"), relief="flat",
                         padx=20, pady=5, activebackground="#007b8a")
login_button.grid(row=3, column=0, columnspan=2, pady=18, sticky="nsew")

root.mainloop()
