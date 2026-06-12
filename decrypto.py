import base64
import os
import time
from argon2 import Type
from argon2.low_level import hash_secret_raw
from cryptography.fernet import Fernet, InvalidToken

files = []

TIME_COST = 3
MEMORY_COST = 65536
PARALLELISM = 4
HASH_LEN = 32

def derive_key(password: bytes, salt: bytes) -> bytes:
    raw_hash = hash_secret_raw(
        secret=password,
        salt=salt,
        time_cost=TIME_COST,
        memory_cost=MEMORY_COST,
        parallelism=PARALLELISM,
        hash_len=HASH_LEN,
        type=Type.ID
    )
    return base64.urlsafe_b64encode(raw_hash)


def check_files():
    for file in os.listdir():
        if file in ["encrypto.py", "decrypto.py", "encrypto.exe", "decrypto.exe", "salt.key", "desktop.ini"]:
            continue
        if os.path.isfile(file) and file.endswith(".EncryptJace"):
            files.append(file)
        
    print(f"Found The Files {files}\n")
    time.sleep(0.5)


def Decryption(user_enter):
    print("It going to decrypt...")
    time.sleep(2.5)

    for file in files:
        try:
            with open(file, "rb") as thefile:
                salt = thefile.read(16)
                ciphertext = thefile.read()

            setkey = derive_key(user_enter.encode(), salt)

            contents_encrypted = base64.urlsafe_b64encode(ciphertext)
        
            contents_decrypted = Fernet(setkey).decrypt(contents_encrypted)

            with open(file, 'wb') as thefile:
                thefile.write(contents_decrypted)
            print(f"Congrats, your file is decrypted: {file}")

            if file.endswith(".EncryptJace"):
                new_file = file.replace(".EncryptJace", "")
                os.rename(file, new_file)
            time.sleep(0.5)
        except InvalidToken:
            print(f"\n[!] Incorrect password for {file} or file corrupted.")
            break

if __name__ == "__main__":
    check_files()
    if not files:
        print("[!] No file found to encryption !\n")
        exit()
    
    psd_input = input("Enter The Password To Decrypted All Of Your Files\n$>> ")
    Decryption(psd_input)




  





