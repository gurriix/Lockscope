
import pickle

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class AEScipher:

    def __init__(self): 
        self.block_size = 32
        self.key_path = r"C:\Users\User\Desktop\Lockscope\AESKey\key.pkl"
        self.file_path = r"C:\Users\User\Desktop\Test Files\Forest.jpg"
        self.size_bytes_path = r"C:\Users\User\Desktop\Lockscope\size_bytes.txt"
        self.iv_path = r"C:\Users\User\Desktop\Lockscope\iv.txt"

    def generate_aes_key(self):
        aes_key = Random.new().read(self.block_size)
        
        with open(self.key_path, "wb") as key_file:
            pickle.dump(aes_key, key_file)

    
    def open_file(self):

        with open(self.file_path, "rb") as file:
            file.seek(100)
            rest_content = file.read()
        
        with open(self.file_path, "rb") as file:
            file_bytes = file.read(100)

        return file_bytes, rest_content


    def encrypt(self):

        print("\n-----ENCRYPT FILE-----")

        self.generate_aes_key()

        file_bytes, rest_content = self.open_file()

        cipher_content = pad(file_bytes, self.block_size)
        
        print("\n")
        print("Contenido del archivo a cifrar:\n" , file_bytes)
        print("Resto del contenido del archivo:\n" , rest_content)
        print("Conenido del archivo a cifrar tras aplicar padding:\n" , cipher_content)
        print("Cantidad de carácteres tras aplicar padding:\n" , len(cipher_content))

        with open(self.key_path, "rb") as key_file:
            aes_key = pickle.load(key_file)
        
        iv = get_random_bytes(16)

        with open(self.iv_path, "wb") as iv_file:
            iv_file.write(iv)
        
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)

        encrypted = cipher.encrypt(cipher_content)

        print("Contenido del archivo encriptado:\n" , encrypted)

        print("Cantidad de carácteres del archivo encriptado:\n" , len(encrypted))

        with open(self.size_bytes_path, "w") as content_size:
            content_size.write(str(len(encrypted)))

        concat_bytes = encrypted + rest_content

        print("\n")
        print("Contenido del archivo a cifrar una vez encriptado:\n" , encrypted)
        print("Resto del contenido del archivo:\n" , rest_content)

        with open(self.file_path, "wb") as cipher_file:
            cipher_file.write(concat_bytes)

        return concat_bytes


    def open_file_encrypted(self):

        with open(self.size_bytes_path, "r") as content_size:
            size = int(content_size.read())

        with open(self.file_path, "rb") as file:
            file.seek(size)
            rest_content = file.read()
        
        with open(self.file_path, "rb") as file:
            file_bytes = file.read(size)

        return file_bytes, rest_content
    

    def decrypt(self):
        
        print("\n-----DECRYPT FILE-----")

        with open(self.key_path, "rb") as key_file:
            aes_key = pickle.load(key_file)

        with open(self.iv_path, "rb") as iv_file:
            iv = iv_file.read()

        cipher = AES.new(aes_key, AES.MODE_CBC, iv)

        file_bytes, rest_content = self.open_file_encrypted()

        print("\n")
        print("Contenido del archivo a cifrar una vez encriptado:\n" , file_bytes)
        print("Resto del contenido del archivo:\n" , rest_content)

        file_bytes_decrypted = cipher.decrypt(file_bytes)

        print("Contenido del archivo a cifrar una vez quitado el padding:\n" , file_bytes_decrypted)

        decrypted = unpad(file_bytes_decrypted, self.block_size)

        print("Contenido del archivo tras quitar el padding:\n" , decrypted)
        print("Cantidad de carácteres una vez quitado el padding:\n" , len(decrypted))

        concat_bytes_decrypted = decrypted + rest_content

        with open(self.file_path, "wb") as plain_file:
            plain_file.write(concat_bytes_decrypted)

        return concat_bytes_decrypted
 


if __name__ == '__main__':
    cipher = AEScipher()
    try:
        print("\nContenido del archivo al completo una vez cifrado:\n" , cipher.encrypt())
        print("\nContenido del archivo al completo una vez descifrado:\n" , cipher.decrypt())

    except KeyboardInterrupt:
        exit(1)

    
