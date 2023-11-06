# Generate RSA key

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def generate_RSA_key():
    private_rsa_key = rsa.generate_private_key(public_exponent=65537, key_size=4096, backend=default_backend()) # Generate a 2048 bits RSA key
    public_rsa_key = private_rsa_key.public_key() # Obtain the public key of the private RSA key generated

    pem_private_rsa_key = private_rsa_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, 
                                                        encryption_algorithm=serialization.NoEncryption()) # Generate PEM public file with th private key
    pem_public_rsa_key = public_rsa_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo) # Generate PEM public file with public key

    # RSA keys storage in a file
    with open(r"C:\Users\User\Desktop\Lockscope\Keys\RSA_private_key.pem", 'wb') as private_rsa_key_file:
        private_rsa_key_file.write(pem_private_rsa_key)
    
    with open(r"C:\Users\User\Desktop\Lockscope\Keys\RSA_public_key.pem", 'wb') as public_rsa_key_file:
        public_rsa_key_file.write(pem_public_rsa_key)
  

