import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
load_dotenv()

def encrypt_file(filename, key):
    f = Fernet(key)
    contents = open(filename).read()
    enc = f.encrypt(contents.encode('ascii'))
    open(filename + '.fernet', 'wb').write(enc)

def decrypt_file(filename, key):
    f = Fernet(key)
    contents = open(filename).read()
    dec = f.decrypt(contents.encode('ascii'))
    open(filename + '.decrypted', 'wb').write(dec)

if __name__ == "__main__":
    # tests for dev
    key = os.environ['SECRET_KEY']
    encrypt_file('../flag.txt', key)

    decrypt_file('../flag.txt.fernet', key)
