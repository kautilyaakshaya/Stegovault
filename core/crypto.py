import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def derive_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return kdf.derive(password.encode())


def encrypt(data: bytes, password: str):
    salt = os.urandom(16)
    key = derive_key(password, salt)

    aes = AESGCM(key)
    nonce = os.urandom(12)

    encrypted = aes.encrypt(nonce, data, None)
    return salt + nonce + encrypted


def decrypt(data: bytes, password: str):
    try:
        salt = data[:16]
        nonce = data[16:28]
        ciphertext = data[28:]

        key = derive_key(password, salt)
        aes = AESGCM(key)

        return aes.decrypt(nonce, ciphertext, None)
    except Exception:
        return None  # Safe failure