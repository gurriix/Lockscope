
import pickle
import pathlib
import base64

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class AEScipher:

    def __init__(self): 
        self.block_size = 32
        self.key_path = r"C:\Users\User\Desktop\Lockscope\AESKey\key.pkl"
        self.files_path = pathlib.Path(r"C:\Users\User\Desktop\Test Files")
        self.size_bytes_path = r"C:\Users\User\Desktop\Lockscope\size_bytes.txt"
        self.iv_path = r"C:\Users\User\Desktop\Lockscope\iv.txt"

    def generate_aes_key(self):
        aes_key = Random.new().read(self.block_size)
        
        b64 = base64.b64encode(aes_key)
        with open(self.key_path, "wb") as key_file:
            pickle.dump(b64, key_file)

    
    def open_file(self, path):

        with open(path, "rb") as file:
            file.seek(100)
            rest_content = file.read()
        
        with open(path, "rb") as file:
            file_bytes = file.read(100)

        return file_bytes, rest_content


    def encrypt(self):

        print("\n-----ENCRYPT FILE-----")

        self.generate_aes_key()

        iv = get_random_bytes(16)

        with open(self.iv_path, "wb") as iv_file:
            iv_file.write(iv)

        with open(self.key_path, "rb") as key_file:
                aes_key = pickle.load(key_file)
        
        b64 = base64.b64decode(aes_key)

        cipher = AES.new(b64, AES.MODE_CBC, iv)
        

        for files in self.files_path.iterdir():

            if files.is_file():

                print(files)

                file_bytes, rest_content = self.open_file(files)

                cipher_content = pad(file_bytes, self.block_size)
                
                print("\n")
                print("Contenido del archivo a cifrar:\n" , file_bytes)
                print("Resto del contenido del archivo:\n" , rest_content)
                print("Conenido del archivo a cifrar tras aplicar padding:\n" , cipher_content)
                print("Cantidad de carácteres tras aplicar padding:\n" , len(cipher_content))

                encrypted = cipher.encrypt(cipher_content)

                print("Contenido del archivo encriptado:\n" , encrypted)

                print("Cantidad de carácteres del archivo encriptado:\n" , len(encrypted))

                with open(self.size_bytes_path, "w") as content_size:
                    content_size.write(str(len(encrypted)))

                concat_bytes = encrypted + rest_content

                print("\n")
                print("Contenido del archivo a cifrar una vez encriptado:\n" , encrypted)
                print("Resto del contenido del archivo:\n" , rest_content)

                with open(files, "wb") as cipher_file:
                    cipher_file.write(concat_bytes)
                
                print("\nContenido del archivo al completo una vez cifrado:\n" , concat_bytes)

                concat_bytes = b'\x00'
                encrypted = b'\x00'
                cipher_content = b'\x00'
                file_bytes = b'\x00'
                rest_content = b'\x00'



    def open_file_encrypted(self, path):

        with open(self.size_bytes_path, "r") as content_size:
            size = int(content_size.read())

        with open(path, "rb") as file:
            file.seek(size)
            rest_content = file.read()
        
        with open(path, "rb") as file:
            file_bytes = file.read(size)

        return file_bytes, rest_content
    

    def decrypt(self):
        
        print("\n-----DECRYPT FILE-----")

        with open(self.key_path, "rb") as key_file:
            aes_key = pickle.load(key_file)
        
        b64 = base64.b64decode(aes_key)

        with open(self.iv_path, "rb") as iv_file:
            iv = iv_file.read()

        cipher = AES.new(b64, AES.MODE_CBC, iv)

        for files in self.files_path.iterdir():

            if files.is_file():

                file_bytes, rest_content = self.open_file_encrypted(files)

                print("\n")
                print("Contenido del archivo a cifrar una vez encriptado:\n" , file_bytes)
                print("Resto del contenido del archivo:\n" , rest_content)

                file_bytes_decrypted = cipher.decrypt(file_bytes)

                print("Contenido del archivo a cifrar una vez quitado el padding:\n" , file_bytes_decrypted)

                decrypted = unpad(file_bytes_decrypted, self.block_size)

                print("Contenido del archivo tras quitar el padding:\n" , decrypted)
                print("Cantidad de carácteres una vez quitado el padding:\n" , len(decrypted))

                concat_bytes_decrypted = decrypted + rest_content

                with open(files, "wb") as plain_file:
                    plain_file.write(concat_bytes_decrypted)
                
                print("\nContenido del archivo al completo una vez descifrado:\n" , concat_bytes_decrypted)
            
                file_bytes_decrypted = b'\x00'
                decrypted = b'\x00'
                concat_bytes_decrypted = b'\x00'
                file_bytes = b'\x00'
                rest_content = b'\x00'

            
 


if __name__ == '__main__':
    cipher = AEScipher()
    try:
        #cipher.encrypt()
        cipher.decrypt()

    except KeyboardInterrupt:
        exit(1)

    
