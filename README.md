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


- All files are stored locally in a folder named `data` located in the same directory as the `PassManage.exe` file. For example, if you run the app from your Desktop, you will find the `data` folder on your Desktop next to the `.exe`.
- The database file is encrypted with Fernet and stored as `data/databasepy.db.encrypted`.
- The database is only decrypted to `data/databasepy.db` while the app is running, and re-encrypted on exit.
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



## Encryption & Decryption Details 📁🔐

**How encryption works:**
- The password database (`databasepy.db`) is encrypted using Fernet symmetric encryption. When the app starts, it decrypts `data/databasepy.db.encrypted` to `data/databasepy.db` for use. When the app closes, it re-encrypts the database and deletes the unencrypted version.
- User files and any files you choose to encrypt are also encrypted with Fernet and stored in the `data` folder with the `.encrypted` extension.
- The encryption key is stored in `data/filekey.key`. Keep this file safe—if lost, you cannot decrypt your data.

**How decryption works:**
- When you decrypt a file (using the app's decrypt function), the decrypted version is saved in the `data` folder with the `.decrypted` extension, and the encrypted file is deleted for security.
- The database is only decrypted while the app is running; otherwise, it remains encrypted.

**Where are files stored?**
- All files (database, encrypted files, decrypted files, key) are stored in the `data` folder, which is located in the same directory as the `PassManage.exe` file. For example, if you run the app from your Desktop, you will find the `data` folder on your Desktop next to the `.exe`.

**To back up or move your data:**
- Copy the entire `data` folder to your desired location. This includes your encrypted database, key, and any encrypted/decrypted files.

**Security notes:**
- Data never leaves your device.
- If you lose `filekey.key`, you will not be able to recover your encrypted data.





