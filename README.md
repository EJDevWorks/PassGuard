## PassGuard 🔒

PassGuard is a local password management tool built with Python, Tkinter, and SQLite3. It allows you to securely store and view your account credentials on your own computer.

## Features ✨

Secure Login – Protect your password vault with a master account.

Local Storage – All data is stored locally using SQLite3; nothing is sent online.

Add & View Passwords – Create new passwords and view saved credentials easily.

Simple Installation – Run the executable and start using it immediately.

## Important ⚠️

Write down your master username and password when you register.

Your credentials cannot be recovered if lost.

Keep your device secure to prevent unauthorized access.


## Installation & Usage 💻

Download and run the application:
https://github.com/EJDevWorks/PassManage/blob/main/PassManage.exe

**How to use the .exe:**
1. Double-click `PassManage.exe` to start PassManage.
2. Register a new account with a master username and password.
3. Log in to start adding and viewing passwords.

**Where your data is saved:**
- All files are stored locally in a folder named `data` next to the `.exe`.
- The database file is `data/databasepy.db`.
- The encryption key is `data/filekey.key`.
- Encrypted user files are saved as `data/<username>.txt.encrypted`.
- Decrypted files (when you use the decrypt function) are saved as `data/<filename>.decrypted`.

**To back up or move your data:**
- Copy the entire `data` folder to your desired location.


## Usage 🛠️

Login: Enter your registered master username and password.

Add Passwords: Click Add, then enter your account credentials.

View Passwords: Access your saved passwords anytime from the main window.

Encrypt/Decrypt Files:
- When you encrypt a file, the encrypted version is saved in the `data` folder.
- When you decrypt a file, the decrypted version is also saved in the `data` folder.

## Security 🔐

Uses local encryption to secure your passwords.

Data never leaves your device.


## Demo Picture



