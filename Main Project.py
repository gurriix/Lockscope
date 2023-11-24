
from Asymmetric import RSAcipher

def main():
    rsa_cipher_process = RSAcipher()
    
    rsa_cipher_process.encryption()
    rsa_cipher_process.decryption()
    
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(1)