
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def generate_rsa_keys():
    private_key = RSA.generate(2048)
    public_key = private_key.public_key()

    private_key = private_key.export_key('DER')
    public_key = public_key.export_key('DER')

    return public_key, private_key


def encrypt_aes_key(aes_key,public_key):

    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))

    return cipher.encrypt(aes_key)


def decrypt_aes_key(aes_key,private_key):

    cipher = PKCS1_OAEP.new(RSA.import_key(private_key))

    return cipher.decrypt(aes_key)

