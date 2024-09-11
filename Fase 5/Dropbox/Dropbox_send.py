import dropbox
import time

api_key = 'sl.B6BvZhHkQt0LnAW2uZYmnPpuk4uqRf5c3tXvwaOby_3cH3nsL7fL4Mo476WJ05-OUud6JH_RYH77yLtrugr-bAAFqHDFEPEg37KQqQeI-gJI26aApkLwkZGidmLa4i74NpmS4DFwKqV2oZCbpq9Fa6I'

dbx = dropbox.Dropbox(api_key)

def local_paths():
    local_aes_key_path = "/home/tfg/server/Fase5/keys/key.pkl"
    local_private_key_path = "/home/tfg/server/Fase5/keys/private_key.pem"

    return local_aes_key_path, local_private_key_path

def dropbox_paths():
    dropbox_private_key_path = "/keys/private_key.pem"
    dropbox_aes_key_path = "/keys/key.pkl"

    return dropbox_aes_key_path, dropbox_private_key_path

def upload_files(key,public_key,private_key):

    dropbox_aes_key_path, dropbox_private_key_path = dropbox_paths()
    local_aes_key_path, local_private_key_path = local_paths()
		
		with open(local_aes_key_path, "rb") as f:
		    aes_key = f.read()
            
    with open(local_private_key_path, "rb") as f:
        private_key = f.read()
        
    try:
        dbx.files_upload(aes_key, dropbox_aes_key_path)
        dbx.files_upload(private_key, dropbox_private_key_path)
    except Exception:
        print("API error")

if __name__ == '__main__':
		send_files()
