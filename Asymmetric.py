
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from os import chmod


class RSAcipher:
    
    # Initialization of variables
    def __init__(self):
        self.private_key_path = r"C:\Users\User\Desktop\Lockscope V2\Keys\private_key.pem"
        self.public_key_path = r"C:\Users\User\Desktop\Lockscope V2\Keys\public_key.pem"
        self.size_bytes_path = r"C:\Users\User\Desktop\Lockscope V2\size_bytes.txt"
        self.bit_len = 2048
        self.file_path = r"C:\Users\User\Desktop\Test Files\calendario_ETSISI.pdf"
        
    # Generation of private and public RSA keys
    def generate_rsa_keys(self):
        private_key = RSA.generate(self.bit_len)
        public_key = private_key.public_key()

        private_key = private_key.export_key("PEM")
        public_key = public_key.export_key("PEM")

        with open(self.private_key_path, 'wb') as content_file:
            content_file.write(private_key)

        with open(self.public_key_path, 'wb') as content_file:
            content_file.write(public_key)

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
        with open(self.file_path, "rb") as file:
            file.seek(100)
            rest_content = file.read()
        
        with open(self.file_path, "rb") as file:
            file_bytes = file.read(100)

        return file_bytes, rest_content
    
    #Method to do the encryption of the file opened with open_file()
    def encryption(self):
        
        self.generate_rsa_keys()

        file_bytes, rest_content = self.open_file()

        print(file_bytes)
        print(rest_content)

        encrypted = self.encrypt(file_bytes)
        
        print(len(encrypted))

        with open(self.size_bytes_path, "w") as content_size:
            content_size.write(str(len(encrypted)))
        
        print("\n")
        print(encrypted)

        concat_bytes = encrypted + rest_content

        print("\n")
        print(encrypted)
        print(rest_content)

        with open(self.file_path, "wb") as cipher_file:
            cipher_file.write(concat_bytes)

        return concat_bytes

    # Method to open the file when was been encrypted
    def open_file_encrypted(self):
        with open(self.size_bytes_path, "r") as content_size:
            size = int(content_size.read())

        print(size)

        with open(self.file_path, "rb") as file:
            file.seek(size)
            rest_content = file.read()
        
        with open(self.file_path, "rb") as file:
            file_bytes = file.read(size)

        return file_bytes, rest_content
    
    # Method which takes the encrypted file using the method open_file_encryted() and decrypt the content
    def decryption(self):

        encrypted_bytes, rest_bytes = self.open_file_encrypted()

        print("\n\n")
        print(encrypted_bytes)
        print(rest_bytes)

        decrypted = self.decrypt(encrypted_bytes)

        print("\n")
        print(decrypted)

        concat_content = decrypted + rest_bytes

        print("\n")
        print(concat_content)
     
        with open(self.file_path, "wb") as decrypt_file:
            decrypt_file.write(concat_content)
        
        return concat_content


    
    
    
    
    

    


   

    
   

    
