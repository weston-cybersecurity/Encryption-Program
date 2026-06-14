import base64
import os 
import time
from argon2 import Type
from argon2.low_level import hash_secret_raw
from cryptography.fernet import Fernet

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

        if os.path.isfile(file) and not file.endswith(".EncryptJace"):
            files.append(file)
    print(f"found FILES: {files}\n")
    time.sleep(1)

def set_encrypt():
    global key, salt

    while True:
        user_password = input("\n[$] Set A Password To Encrypt your Files\n$>> ").encode()
        
        if len(user_password) < 10:
            print("Your password are too short, Please more than 10 numbers.\n")
            continue

        confirm_password = input("Confirm Your Password Again\n$>> ").encode()

        if user_password == confirm_password:
            print("Password Confirmed Successful !\n")
            break
        else:
            print("[!] Password do not natch! Please try again from the beginning.\n")

    salt = os.urandom(16)
    key = derive_key(user_password, salt)

def Encryption(salt):
    for file in files:
        try:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            
            contents_encrypted = Fernet(key).encrypt(contents)
            
            raw_ciphertext = base64.urlsafe_b64decode(contents_encrypted)

            with open(file, "wb") as thefile:
                thefile.write(salt)
                thefile.write(raw_ciphertext)

            new_file = file + ".EncryptJace"
            os.rename(file, new_file)
            print(f"Encrypted Successful ! -> {new_file}")
            time.sleep(0.7)
        
        except Exception as e:
            print(f"When handle files '{file}' found mistake: {e}")


if __name__ == "__main__":
    check_files()

    if not files:
        print("No files found to encrypt!")
        exit()

    set_encrypt()
    print(f"[+] It going to Encryption...\n")
    time.sleep(3)
    
    Encryption(salt)
    input("[+] Done ! Have a Good Day ! Enter to leave")









