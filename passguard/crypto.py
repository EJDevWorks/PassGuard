from cryptography.fernet import Fernet

def generate_key():
	"""Generate a new encryption key."""
	return Fernet.generate_key()

def encrypt_password(password: str, key: bytes) -> bytes:
	"""Encrypt a password using the provided key."""
	f = Fernet(key)
	return f.encrypt(password.encode())

def decrypt_password(token: bytes, key: bytes) -> str:
	"""Decrypt an encrypted password using the provided key."""
	f = Fernet(key)
	return f.decrypt(token).decode()
