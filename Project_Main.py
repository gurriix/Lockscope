# Main

import Generate_rsa_key

def main():
    Generate_rsa_key.generate_RSA_key()

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        exit() 