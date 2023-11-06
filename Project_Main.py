# Main

import Generate_rsa_key
import Encrypt_decrypt

def main():
    Generate_rsa_key.generate_RSA_key()
    Encrypt_decrypt.encrypt()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit() 