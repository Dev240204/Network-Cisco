from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import base64

def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return cipher.nonce + ciphertext + tag

def decrypt(ciphertext, key):
    nonce = ciphertext[:16]
    tag = ciphertext[-16:]
    ciphertext = ciphertext[16:-16]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext

def main():
    key = get_random_bytes(16) 

    plaintext = "Hello Engineers!!!".encode('utf-8')

    ciphertext = encrypt(plaintext, key)
    decrypted_text = decrypt(ciphertext, key)

    print("Original: " + plaintext.decode('utf-8'))
    print("Ciphertext (Base64): " + base64.b64encode(ciphertext).decode('utf-8'))
    print("Decrypted: " + decrypted_text.decode('utf-8'))

if __name__ == "__main__":
    main()