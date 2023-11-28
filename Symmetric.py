
import pickle

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad


class AEScipher:

    def __init__(self): 
        self.block_size = 32
        self.key_path = r"C:\Users\User\Desktop\Lockscope V2\AESKey\key.pkl"
        self.file_path = r"C:\Users\User\Desktop\Test Files\Prueba.txt"
        self.size_bytes_path = r"C:\Users\User\Desktop\Lockscope V2\size_bytes.txt"

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

        self.generate_aes_key()

        file_bytes, rest_content = self.open_file()

        cipher_content = pad(file_bytes, self.block_size)
        
        print("\n")
        print(file_bytes)
        print(rest_content)
        print(cipher_content)

        with open(self.key_path, "rb") as key_file:
            aes_key = pickle.load(key_file)
        
        cipher = AES.new(aes_key, AES.MODE_CBC)

        encrypted = cipher.encrypt(cipher_content)

        print(encrypted)

        print(len(encrypted))

        with open(self.size_bytes_path, "w") as content_size:
            content_size.write(str(len(encrypted)))

        concat_bytes = encrypted + rest_content

        print("\n")
        print(encrypted)
        print(rest_content)

        with open(self.file_path, "wb") as cipher_file:
            cipher_file.write(concat_bytes)

        return concat_bytes


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
    

    def decrypt(self):

        with open(self.key_path, "rb") as key_file:
            aes_key = pickle.load(key_file)
        
        print("\n")
        print(aes_key)

        cipher = AES.new(aes_key, AES.MODE_CBC)

        file_bytes, rest_content = self.open_file_encrypted()

        print("\n")
        print(file_bytes)
        print(rest_content)

        decrypted = unpad(cipher.decrypt(file_bytes), self.block_size)

        print(decrypted)

        concat_bytes_decrypted = decrypted + rest_content

        with open(self.file_path, "wb") as plain_file:
            plain_file.write(concat_bytes_decrypted)

        return concat_bytes_decrypted



if __name__ == '__main__':
    cipher = AEScipher()
    try:
        print(cipher.encrypt())
        print(cipher.decrypt())

    except KeyboardInterrupt:
        exit(1)

    
