import os
import zlib
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=150000,
    )
    return kdf.derive(password.encode())


def encrypt_data(data: bytes, password: str) -> bytes:
    # 📦 Compress
    compressed = zlib.compress(data)

    salt = os.urandom(16)
    key = derive_key(password, salt)

    aesgcm = AESGCM(key)
    nonce = os.urandom(12)

    encrypted = aesgcm.encrypt(nonce, compressed, None)

    return salt + nonce + encrypted


def decrypt_data(data: bytes, password: str) -> bytes:
    try:
        salt = data[:16]
        nonce = data[16:28]
        ciphertext = data[28:]

        key = derive_key(password, salt)
        aesgcm = AESGCM(key)

        decrypted = aesgcm.decrypt(nonce, ciphertext, None)

        # 📦 Decompress
        return zlib.decompress(decrypted)

    except Exception:
        raise ValueError("Wrong password or corrupted data")


def get_seed(password: str) -> int:
    return int(hashlib.sha256(password.encode()).hexdigest(), 16)