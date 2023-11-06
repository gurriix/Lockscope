# Encryt and decrypt

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

def load_public_rsa_key():
    with open(r"C:\Users\User\Desktop\Lockscope\Keys\RSA_private_key.pem", 'rb') as public_key_file:
         pem_public_key = public_key_file.read()
    public_key = serialization.load_pem_public_key(pem_public_key)
    
    return public_key

def load_private_rsa_key():
    with open(r"C:\Users\User\Desktop\Lockscope\Keys\RSA_private_key.pem", 'rb') as private_key_file:
        pem_private_key = private_key_file.read()
    private_key = serialization.load_pem_private_key(pem_private_key)

    return private_key

def encrypt():
    public_key = load_public_rsa_key()

    with open(r"C:\Users\User\Desktop\Test Files\Constitucion.txt", 'rb') as pdf_file:
        plain_file = pdf_file.read()

    cipher_file = public_key.encrypt(plain_file , padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA512()), algorithm=hashes.SHA512(), label=None))

    with open(r"C:\Users\User\Desktop\Test Files\Constitucion.bin", 'wb') as pdf_file:
        pdf_file.write(cipher_file)


def decrypt():
    private_key = load_private_rsa_key()

    with open(r"C:\Users\User\Desktop\Test Files\Constitucion.bin", 'rb') as pdf_file:
        cipher_file = pdf_file.read()
    
    plain_file = private_key.decrypt(cipher_file, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA512()), algorithm=hashes.SHA512(), label=None))

    with open(r"C:\Users\User\Desktop\Test Files\Constitucion.pdf", 'wb') as pdf_file:
        pdf_file.write(plain_file)