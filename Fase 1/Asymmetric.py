
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


class RSAcipher:
    
    # Initialization of variables
    def __init__(self):
        self.private_key_path = r"C:\Users\User\Desktop\Lockscope\Fase 1\RSAKeys\private_key.pem"
        self.public_key_path = r"C:\Users\User\Desktop\Lockscope\Fase 1\RSAKeys\public_key.pem"
        self.size_bytes_path = r"C:\Users\User\Desktop\Lockscope\Fase 1\size_bytes.txt"
        self.bit_len = 2048
        self.file_path = r"C:\Users\User\Desktop\Test Files\Forest.jpg"
        
    # Generation of private and public RSA keys
    def generate_rsa_keys(self):
        private_key = RSA.generate(self.bit_len)
        public_key = private_key.public_key()

        private_key = private_key.export_key("PEM")
        public_key = public_key.export_key("PEM")

        with open(self.private_key_path, 'wb') as f:
            f.write(private_key)

        with open(self.public_key_path, 'wb') as f:
            f.write(public_key)

    # Encrypt method
    def encrypt(self, data):
        with open(self.public_key_path, 'rb') as f:
            public_key = f.read()

        cipher = PKCS1_OAEP.new(RSA.import_key(public_key))

        return cipher.encrypt(data)
    
    # Decrypt method
    def decrypt(self, data):
        with open(self.private_key_path, 'rb') as f:
            private_key = f.read()

        cipher = PKCS1_OAEP.new(RSA.import_key(private_key))

        return cipher.decrypt(data)

    # Method to open the file to cipher
    def open_file(self):

        with open(self.file_path, "rb") as f:
            f.seek(100)
            rest_content = f.read()
        
        with open(self.file_path, "rb") as f:
            cipher_data = f.read(100)

        return cipher_data, rest_content
    
    #Method to do the encryption of the file opened with open_file()
    def encryption(self):
        
        print("\n-----ENCRYPT-----")

        self.generate_rsa_keys()

        cipher_data, rest_content = self.open_file()

        print("\nContenido del archivo a cifrar:\n", cipher_data)
        print("Resto del contenido del archivo:\n",rest_content)

        encrypted_data = self.encrypt(cipher_data)
        
        print("\nTamaño del contenido encriptado:\n", len(encrypted_data))

        with open(self.size_bytes_path, "w") as content_size:
            content_size.write(str(len(encrypted_data)))

        concat_bytes = encrypted_data + rest_content

        print("\nContenido del archivo cifrado:\n", encrypted_data)
        print("Resto del contenido del archivo:\n", rest_content)

        with open(self.file_path, "wb") as encrypted_file:
            encrypted_file.write(concat_bytes)

        return concat_bytes

    # Method to open the file when was been encrypted
    def open_file_encrypted(self):
        with open(self.size_bytes_path, "r") as content_size:
            size_cipher_data = int(content_size.read())

        with open(self.file_path, "rb") as f:
            f.seek(size_cipher_data)
            rest_content = f.read()
        
        with open(self.file_path, "rb") as f:
            cipher_data = f.read(size_cipher_data)

        return cipher_data, rest_content
    
    # Method which takes the encrypted file using the method open_file_encryted() and decrypt the content
    def decryption(self):

        print("\n-----DECRYPT-----")

        encrypted_data, rest_content = self.open_file_encrypted()

        print("\nContenido del archivo cifrado:\n", encrypted_data)
        print("Resto del contenido del archivo:\n", rest_content)

        decrypted_data = self.decrypt(encrypted_data)

        print("\nContenido del archivo descifrado:\n", decrypted_data)

        concat_content = decrypted_data + rest_content

        print("\nContenido total del archivo:\n", concat_content)
     
        with open(self.file_path, "wb") as decrypted_file:
            decrypted_file.write(concat_content)
        
        return concat_content


if __name__ == '__main__':
    try:
        rsa_cipher_process = RSAcipher()

        rsa_cipher_process.encryption()
        #rsa_cipher_process.decryption()
        
    except KeyboardInterrupt:
        exit(1)
    
    
    

    


   

    
   

    
