import sys
from getpass import getpass
from .crypto import generate_key, encrypt_password, decrypt_password

password_store = {}
key = generate_key()

def add_password():
	name = input("Enter account name: ")
	pwd = getpass("Enter password: ")
	enc_pwd = encrypt_password(pwd, key)
	password_store[name] = enc_pwd
	print(f"Password for '{name}' added.")

def get_password():
	name = input("Enter account name: ")
	enc_pwd = password_store.get(name)
	if enc_pwd:
		pwd = decrypt_password(enc_pwd, key)
		print(f"Password for '{name}': {pwd}")
	else:
		print("No password found for that account.")

def main():
	while True:
		print("\nPassGuard CLI")
		print("1. Add password")
		print("2. Get password")
		print("3. Exit")
		choice = input("Choose an option: ")
		if choice == '1':
			add_password()
		elif choice == '2':
			get_password()
		elif choice == '3':
			print("Exiting...")
			sys.exit(0)
		else:
			print("Invalid choice.")

if __name__ == "__main__":
	main()
