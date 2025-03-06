import dropbox
from dropbox.exceptions import ApiError
import time

api_key = 'sl.token'

dbx = dropbox.Dropbox(api_key)

def local_paths():
    local_aes_key_path = "/home/tfg/server/Fase5/keys/key.pkl"
    local_private_key_path = "/home/tfg/server/Fase5/keys/private_key.pem"
    local_public_key_path = "/home/tfg/server/Fase5/keys/public_key.pem"

    return local_aes_key_path, local_private_key_path, local_public_key_path

def dropbox_paths():
    dropbox_private_key_path = "/keys/private_key.pem"
    dropbox_public_key_path = "/keys/public_key.pem"
    dropbox_aes_key_path = "/keys/key.pkl"

    return dropbox_aes_key_path, dropbox_private_key_path, dropbox_public_key_path

def delete_files(file1,file2,file3):
		try:
				dbx.files_delete(file1)
				dbx.files_delete(file2)
				dbx.files_delete(file3)
		except ApiError:
				print("API error")

def download_files():
    
    dropbox_aes_key_path, dropbox_private_key_path, dropbox_public_key_path = dropbox_paths()
    local_aes_key_path, local_private_key_path, local_public_key_path = local_paths()

    while True:
        try:
            metadata1, res1 = dbx.files_download(dropbox_aes_key_path)
            metadata2, res2 = dbx.files_download(dropbox_private_key_path)
            metadata3, res3 = dbx.files_download(dropbox_public_key_path)
            
            aes_key = res1.content
            private_key = res2.content
	          public_key = res3.content

            with open(local_aes_key_path, "wb") as f:
                f.write(aes_key)
            
            with open(local_private_key_path, "wb") as f:
                f.write(private_key)
                
            with open(local_public_key_path, "wb") as f:
                f.write(public_key)
            break
        
        except Exception as error:
            if error.error.is_path() and error.error.get_path().is_not_found():
                print("File not uploaded yet. Waiting...")
                time.sleep(10)
            else:
                raise
                
       delete_files(dropbox_aes_key_path, dropbox_private_key_path, dropbox_public_key_path)
       
       
       
if __name__ == '__main__':
		download_files()
