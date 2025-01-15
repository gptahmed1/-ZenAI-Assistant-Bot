from cryptography.fernet import Fernet
import hashlib

class SecurityManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
    
    def encrypt_message(self, message: str) -> bytes:
        return self.cipher_suite.encrypt(message.encode())
    
    def decrypt_message(self, encrypted_message: bytes) -> str:
        return self.cipher_suite.decrypt(encrypted_message).decode()
    
    @staticmethod
    def hash_message(message: str) -> str:
        return hashlib.sha256(message.encode()).hexdigest()