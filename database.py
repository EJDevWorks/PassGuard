import sqlite3
from cryptography.fernet import Fernet
import os
from typing import List, Tuple
from file_crypto import encrypt_file, decrypt_file


# Ensure data folder exists
DATA_DIR = 'data'
os.makedirs(DATA_DIR, exist_ok=True)

# Database encryption/decryption
DB_PATH = os.path.join(DATA_DIR, 'databasepy.db')
DB_ENC_PATH = DB_PATH + '.encrypted'
KEY_FILE = os.path.join(DATA_DIR, 'filekey.key')

from file_crypto import encrypt_file, decrypt_file

# Decrypt database if encrypted version exists
if os.path.exists(DB_ENC_PATH):
	decrypt_file(DB_ENC_PATH, DB_PATH, key_file=KEY_FILE)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Key management
if not os.path.exists(KEY_FILE):
	key = Fernet.generate_key()
	with open(KEY_FILE, 'wb') as f:
		f.write(key)
else:
	with open(KEY_FILE, 'rb') as f:
		key = f.read()
fernet = Fernet(key)

cursor.execute('''
CREATE TABLE IF NOT EXISTS passwords (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	website TEXT NOT NULL,
	username TEXT NOT NULL,
	password TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL
)
''')
conn.commit()

# Encrypt database on exit
import atexit
def encrypt_db_on_exit():
	if os.path.exists(DB_PATH):
		encrypt_file(DB_PATH, DB_ENC_PATH, key_file=KEY_FILE)
		try:
			os.remove(DB_PATH)
		except Exception:
			pass
atexit.register(encrypt_db_on_exit)
def register_user(username: str, password: str) -> bool:
	try:
		encrypted_pwd = fernet.encrypt(password.encode()).decode()
		cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, encrypted_pwd))
		conn.commit()
		user_file = os.path.join(DATA_DIR, f'{username}.txt')
		with open(user_file, 'w') as f:
			f.write(f'Username: {username}\nPassword: {password}\n')
		encrypt_file(user_file, key_file=KEY_FILE)
		os.remove(user_file)  
		return True
	except sqlite3.IntegrityError:
		return False

def authenticate_user(username: str, password: str) -> bool:
	cursor.execute('SELECT password FROM users WHERE username=?', (username,))
	row = cursor.fetchone()
	if row:
		try:
			decrypted_pwd = fernet.decrypt(row[0].encode()).decode()
			return decrypted_pwd == password
		except Exception:
			return False
	return False

def add_password(website: str, username: str, password: str) -> None:
	encrypted_pwd = fernet.encrypt(password.encode()).decode()
	cursor.execute('INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)',
				   (website, username, encrypted_pwd))
	conn.commit()
	# Save password entry to user's encrypted file
	user_file = os.path.join(DATA_DIR, f'{username}.txt')
	entry = f'Website: {website}\nUsername: {username}\nPassword: {password}\n\n'
	# Decrypt, append, and re-encrypt
	enc_file = user_file + '.encrypted'
	if os.path.exists(enc_file):
		decrypt_file(enc_file, user_file, key_file=KEY_FILE)
	with open(user_file, 'a') as f:
		f.write(entry)
	encrypt_file(user_file, key_file=KEY_FILE)
	os.remove(user_file)

def get_passwords() -> List[Tuple[str, str, str]]:
		cursor.execute('SELECT website, username, password FROM passwords')
		rows = cursor.fetchall()
		result: List[Tuple[str, str, str]] = []
		for site, usr, enc_pwd in rows:
			try:
				pwd = fernet.decrypt(enc_pwd.encode()).decode()
			except Exception:
				pwd = "<decryption error>"
			result.append((site, usr, pwd))
		return result

def delete_password(website: str, username: str, password: str) -> None:
	# Find encrypted password
	encrypted_pwd = fernet.encrypt(password.encode()).decode()
	cursor.execute('DELETE FROM passwords WHERE website=? AND username=? AND password=?',
				   (website, username, encrypted_pwd))
	conn.commit()