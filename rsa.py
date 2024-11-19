import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open("private_key.pem", "wb") as private_file:
        private_file.write(private_pem)

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open("public_key.pem", "wb") as public_file:
        public_file.write(public_pem)

    print("Keys saved to 'private_key.pem' and 'public_key.pem'")

def encrypt_message(public_key_pem, message):
    public_key = serialization.load_pem_public_key(public_key_pem, backend=default_backend())

    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return base64.b64encode(encrypted).decode('utf-8')


def decrypt_message(private_key_pem, encrypted_message_base64):
    private_key = serialization.load_pem_private_key(private_key_pem, password=None, backend=default_backend())

    encrypted_message = base64.b64decode(encrypted_message_base64)

    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return decrypted.decode()

generate_keys()  

with open("public_key.pem", "rb") as public_file:
    public_key_pem = public_file.read()

with open("private_key.pem", "rb") as private_file:
    private_key_pem = private_file.read()


message = "GODWIN MONSERATE"
print(f"Original message: {message}")

encrypted_message_base64 = encrypt_message(public_key_pem, message)
print(f"Encrypted message (Base64): {encrypted_message_base64}")

# Decrypt the message
decrypted_message = decrypt_message(private_key_pem, encrypted_message_base64)
print(f"Decrypted message: {decrypted_message}")
