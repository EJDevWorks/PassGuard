import tkinter as tk
from tkinter import messagebox, filedialog
from database import add_password, get_passwords, delete_password, authenticate_user, register_user
from file_crypto import encrypt_file, decrypt_file


root = tk.Tk()
root.title("PassGuard Login")
root.geometry("400x300")
root.configure(bg="#222831")

for i in range(6):
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
    def encrypt_file_gui():
        file_path = filedialog.askopenfilename(title="Select file to encrypt")
        if file_path:
            encrypted_path = encrypt_file(file_path)
            messagebox.showinfo("Success", f"Encrypted file saved as:\n{encrypted_path}")

    def decrypt_file_gui():
        file_path = filedialog.askopenfilename(title="Select file to decrypt")
        if file_path:
            decrypted_path = decrypt_file(file_path)
            messagebox.showinfo("Success", f"Decrypted file saved as:\n{decrypted_path}")
    pm_window = tk.Toplevel(root)
    pm_window.title("PassGuard - Password Manager")
    pm_window.geometry("520x460")
    pm_window.configure(bg="#222222")

    for i in range(9):
        pm_window.grid_rowconfigure(i, weight=1)
    for i in range(2):
        pm_window.grid_columnconfigure(i, weight=1)

    title_label_pm = tk.Label(pm_window, text="Password Manager", bg="#222222", fg="#00adb5", font=("Segoe UI", 18, "bold"))
    title_label_pm.grid(row=0, column=0, columnspan=2, pady=(20, 10), sticky="nsew")

    website_label = tk.Label(pm_window, text="Website:", bg="#222222", fg="#f0f0f0", font=("Segoe UI", 12))
    website_label.grid(row=1, column=0, sticky="e", padx=(40, 10), pady=8)
    website_entry = tk.Entry(pm_window, bg="#333333", fg="#f0f0f0", font=("Segoe UI", 12), insertbackground="#f0f0f0", width=28, relief="flat")
    website_entry.grid(row=1, column=1, sticky="w", padx=(10, 40), pady=8)

    username_label_pm = tk.Label(pm_window, text="Username:", bg="#222222", fg="#f0f0f0", font=("Segoe UI", 12))
    username_label_pm.grid(row=2, column=0, sticky="e", padx=(40, 10), pady=8)
    username_entry_pm = tk.Entry(pm_window, bg="#333333", fg="#f0f0f0", font=("Segoe UI", 12), insertbackground="#f0f0f0", width=28, relief="flat")
    username_entry_pm.grid(row=2, column=1, sticky="w", padx=(10, 40), pady=8)

    password_label_pm = tk.Label(pm_window, text="Password:", bg="#222222", fg="#f0f0f0", font=("Segoe UI", 12))
    password_label_pm.grid(row=3, column=0, sticky="e", padx=(40, 10), pady=8)
    password_entry_pm = tk.Entry(pm_window, show="*", bg="#333333", fg="#f0f0f0", font=("Segoe UI", 12), insertbackground="#f0f0f0", width=28, relief="flat")
    password_entry_pm.grid(row=3, column=1, sticky="w", padx=(10, 40), pady=8)

    status_lbl = tk.Label(pm_window, text="", bg="#222222", fg="#f0f0f0", font=("Segoe UI", 10))
    status_lbl.grid(row=4, column=0, columnspan=2)

   
    def save():
        website = website_entry.get().strip()
        user = username_entry_pm.get().strip()
        pwd = password_entry_pm.get()
        if not (website and user and pwd):
            messagebox.showwarning("Missing info", "Please fill Website, Username, and Password.")
            return
        try:
            add_password(website, user, pwd)
            status_lbl.config(text="Saved successfully.", fg="#9fff9f")
            website_entry.delete(0, tk.END)
            username_entry_pm.delete(0, tk.END)
            password_entry_pm.delete(0, tk.END)
        except Exception as e:
            status_lbl.config(text=f"Error saving: {e}", fg="red")

   
    def show_passwords():
        show_window = tk.Toplevel(pm_window)
        show_window.title("Saved Passwords")
        show_window.geometry("480x360")
        show_window.configure(bg="#111")

        container = tk.Frame(show_window, bg="#111")
        container.pack(fill="both", expand=True, padx=8, pady=8)

        hdr = tk.Frame(container, bg="#222")
        hdr.pack(fill="x", padx=4, pady=(0,6))
        tk.Label(hdr, text="#", bg="#222", fg="white", font=("Segoe UI", 10, "bold"), width=4).pack(side="left")
        tk.Label(hdr, text="Website", bg="#222", fg="white", font=("Segoe UI", 10, "bold"), width=24).pack(side="left")
        tk.Label(hdr, text="Username", bg="#222", fg="white", font=("Segoe UI", 10, "bold"), width=18).pack(side="left")
        tk.Label(hdr, text="Password", bg="#222", fg="white", font=("Segoe UI", 10, "bold"), width=18).pack(side="left")

        def refresh():
            for w in container.winfo_children():
                if w is hdr:  
                    continue
                w.destroy()

            rows = get_passwords()
            if not rows:
                tk.Label(container, text="No saved passwords.", bg="#111", fg="white", font=("Segoe UI", 12)).pack(pady=20)
                return

            for idx, (site, usr, pwd) in enumerate(rows, start=1):
                row_frame = tk.Frame(container, bg="#111")
                row_frame.pack(fill="x", padx=4, pady=2)

                tk.Label(row_frame, text=str(idx), bg="#111", fg="white", width=4, anchor="w").pack(side="left")
                tk.Label(row_frame, text=site, bg="#111", fg="white", width=24, anchor="w").pack(side="left")
                tk.Label(row_frame, text=usr, bg="#111", fg="white", width=18, anchor="w").pack(side="left")
                tk.Label(row_frame, text=pwd, bg="#111", fg="white", width=18, anchor="w").pack(side="left")

                def make_delete(s: str, u: str, p: str):
                    def _delete():
                        if messagebox.askyesno("Delete", f"Delete entry for {s} / {u}?"):
                            try:
                                deleted = delete_password(s, u, p)
                                if deleted:
                                    messagebox.showinfo("Deleted", "Entry deleted.")
                                else:
                                    messagebox.showwarning("Not found", "No matching entry found to delete.")
                                refresh()
                            except Exception as e:
                                messagebox.showerror("Error", f"Error deleting: {e}")
                    return _delete

                del_btn = tk.Button(row_frame, text="Delete", command=make_delete(site, usr, pwd),
                                    bg="#c40021", fg="white", font=("Segoe UI", 10, "bold"), relief="raised", padx=6)
                del_btn.pack(side="right", padx=(6,0))

        refresh()

    save_btn = tk.Button(pm_window, text="Save", command=save, bg="#0078D7", fg="white", font=("Segoe UI", 12),
                         relief="flat", padx=20, pady=5, activebackground="#005fa3")
    save_btn.grid(row=5, column=0, columnspan=2, pady=8, sticky="nsew")

    show_btn = tk.Button(pm_window, text="Show Passwords", command=show_passwords,
                         bg="#21c400", fg="#222222", font=("Segoe UI", 12, "bold"),
                         relief="raised", padx=10, pady=5, activebackground="#1e9e00", bd=2)
    show_btn.grid(row=6, column=0, columnspan=2, pady=(4, 10), sticky="nsew")

    encrypt_btn = tk.Button(pm_window, text="Encrypt File", command=encrypt_file_gui,
                            bg="#393e46", fg="#00adb5", font=("Segoe UI", 12, "bold"), relief="flat", padx=20, pady=5)
    encrypt_btn.grid(row=7, column=0, columnspan=2, pady=(4, 4), sticky="nsew")

    decrypt_btn = tk.Button(pm_window, text="Decrypt File", command=decrypt_file_gui,
                            bg="#393e46", fg="#00adb5", font=("Segoe UI", 12, "bold"), relief="flat", padx=20, pady=5)
    decrypt_btn.grid(row=8, column=0, columnspan=2, pady=(0, 10), sticky="nsew")

    def on_close():
        root.deiconify()
        pm_window.destroy()

    pm_window.protocol("WM_DELETE_WINDOW", on_close)


def login():
    username = username_entry.get().strip()
    password = password_entry.get()
    if not (username and password):
        messagebox.showwarning("Missing", "Enter username and password.")
        return

    try:
        if authenticate_user(username, password):
            print(f"Login successful: {username}")
            root.withdraw()
            open_password_manager()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")
    except Exception as e:
        messagebox.showerror("Error", f"Authentication error: {e}")

def open_registration():
    reg_window = tk.Toplevel(root)
    reg_window.title("Register Account")
    reg_window.geometry("350x260")
    reg_window.configure(bg="#222831")

    tk.Label(reg_window, text="Register", bg="#222831", fg="#00adb5", font=("Segoe UI", 18, "bold")).pack(pady=10)
    tk.Label(reg_window, text="Username:", bg="#222831", fg="#eeeeee", font=("Segoe UI", 12)).pack()
    reg_username = tk.Entry(reg_window, bg="#393e46", fg="#eeeeee", font=("Segoe UI", 12), insertbackground="#eeeeee", relief="flat")
    reg_username.pack(pady=5)
    tk.Label(reg_window, text="Password:", bg="#222831", fg="#eeeeee", font=("Segoe UI", 12)).pack()
    reg_password = tk.Entry(reg_window, show="*", bg="#393e46", fg="#eeeeee", font=("Segoe UI", 12), insertbackground="#eeeeee", relief="flat")
    reg_password.pack(pady=5)

    feedback_lbl = tk.Label(reg_window, text="", bg="#222831", fg="white", font=("Segoe UI", 11))
    feedback_lbl.pack(pady=6)

    def register():
        u = reg_username.get().strip()
        p = reg_password.get()
        if not (u and p):
            feedback_lbl.config(text="Please enter both fields.", fg="red")
            return
        try:
            ok = register_user(u, p)
            if ok:
                feedback_lbl.config(text="Registration successful! You can now log in.", fg="green")
            else:
                feedback_lbl.config(text="Username already exists.", fg="red")
        except Exception as e:
            feedback_lbl.config(text=f"Error: {e}", fg="red")

    tk.Button(reg_window, text="Register", command=register, bg="#00adb5", fg="#222831", font=("Segoe UI", 12, "bold"),
              relief="flat", padx=20, pady=5, activebackground="#007b8a").pack(pady=8)


login_button = tk.Button(root, text="Login", command=login, bg="#00adb5", fg="#222831",
                         font=("Segoe UI", 14, "bold"), relief="flat", padx=20, pady=5, activebackground="#007b8a")
login_button.grid(row=3, column=0, columnspan=2, pady=8, sticky="nsew")

register_button = tk.Button(root, text="Register", command=open_registration, bg="#393e46", fg="#00adb5",
                            font=("Segoe UI", 12, "bold"), relief="flat", padx=20, pady=5, activebackground="#222831")
register_button.grid(row=4, column=0, columnspan=2, pady=(0, 10), sticky="nsew")


root.mainloop()