# Generate RSA key

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_RSA_key():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048) # Generate a 2048 bits RSA key
    public_key = private_key.public_key() # Obtain the public key of the private RSA key generated

    pem_private_key = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, 
                                                encryption_algorithm=serialization.NoEncryption()) # Generate a PEM public file with th private key
    pem_public_key = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo) # Generate a PEM public file with public key

    # Stored the RSA keys in a file
    private_key_file = open(r"C:\Users\User\Desktop\Lockscope\Keys\RSA_private_key.pem", 'w')
    private_key_file.write(pem_private_key.decode())
    private_key_file.close()
    
    public_key_file = open(r"C:\Users\User\Desktop\Lockscope\Keys\RSA_public_key.pem", 'w')
    public_key_file.write(pem_public_key.decode())
    public_key_file.close()


