import sqlite3

conn = sqlite3.connect('passguard.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS passwords (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	website TEXT NOT NULL,
	username TEXT NOT NULL,
	password TEXT NOT NULL
)
''')
conn.commit()

def add_password(website: str, username: str, password: str) -> None:
    cursor.execute('INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)',
                   (website, username, password))
    conn.commit()

def get_passwords() -> list[tuple[str, str, str]]:
    cursor.execute('SELECT website, username, password FROM passwords')
    return cursor.fetchall()

if __name__ == '__main__':
	add_password('example.com', 'user1', 'secret123')
	for entry in get_passwords():
		print(entry)