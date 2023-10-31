# Encryt and decrypt

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.serialization import load_pem_private_key


def encrypt():

    with open(r"C:\Users\User\Desktop\Lockscope\Keys\RSA_public_key.pem", 'r') as public_key_file:
        pem_public_key = public_key_file.read()
    
    public_key = load_pem_public_key(pem_public_key)

    with open(r"C:\Users\User\Desktop\Test Files\calendario_ETSISI.pdf", 'r') as pdf_file:
        plain_file = pdf_file.read()

    cipher_file = public_key.encrypt(plain_file, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    with open(r"C:\Users\User\Desktop\Test Files\calendario_ETSISI.bin", 'w') as pdf_file:
        pdf_file.write(cipher_file)


def decrypt():

    with open(r"C:\Users\User\Desktop\Lockscope\Keys\RSA_private_key.pem", 'r') as private_key_file:
        pem_private_key = private_key_file.read()
    
    private_key = load_pem_private_key(pem_private_key)

    with open(r"C:\Users\User\Desktop\Test Files\calendario_ETSISI.bin", 'r') as pdf_file:
        cipher_file = pdf_file.read()

    plain_file = private_key.encrypt(cipher_file, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    with open(r"C:\Users\User\Desktop\Test Files\calendario_ETSISI.pdf", 'w') as pdf_file:
        pdf_file.write(plain_file)