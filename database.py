import sqlite3

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()


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
def register_user(username: str, password: str) -> bool:
	try:
		cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
		conn.commit()
		return True
	except sqlite3.IntegrityError:
		return False 

def authenticate_user(username: str, password: str) -> bool:
	cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
	return cursor.fetchone() is not None

def add_password(website: str, username: str, password: str) -> None:
	cursor.execute('INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)',
				   (website, username, password))
	conn.commit()

def get_passwords() -> list[tuple[str, str, str]]:
	cursor.execute('SELECT website, username, password FROM passwords')
	return cursor.fetchall()

def delete_password(website: str, username: str, password: str) -> None:
	cursor.execute('DELETE FROM passwords WHERE website=? AND username=? AND password=?',
				   (website, username, password))
	conn.commit()