import numpy as np

def matrix_inverse(matrix, mod):
    det = int(np.linalg.det(matrix))
    det_inv = pow(det, -1, mod)
    adj_matrix = np.round(det_inv * np.linalg.inv(matrix)).astype(int) % mod
    return adj_matrix

def encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    key_size = len(key_matrix)
    plaintext_len = len(plaintext)

    if plaintext_len % key_size != 0:
        padding = key_size - (plaintext_len % key_size)
        plaintext += "X" * padding

    ciphertext = ""
    for i in range(0, len(plaintext), key_size):
        block = plaintext[i:i + key_size]
        block_vector = np.array([ord(char) - ord('A') for char in block])
        encrypted_block = np.dot(key_matrix, block_vector) % 26
        ciphertext += ''.join([chr(char + ord('A')) for char in encrypted_block])

    return ciphertext

def decrypt(ciphertext, key_matrix):
    key_size = len(key_matrix)
    plaintext = ""
    ciphertext = ciphertext.replace(" ", "").upper()

    for i in range(0, len(ciphertext), key_size):
        block = ciphertext[i:i + key_size]
        block_vector = np.array([ord(char) - ord('A') for char in block])
        decrypted_block = np.dot(key_matrix, block_vector) % 26
        plaintext += ''.join([chr(char + ord('A')) for char in decrypted_block])

    return plaintext

def main():
    choice = input("Choose 'E' for Encryption or 'D' for Decryption: ").upper()

    if choice not in ('E', 'D'):
        print("Invalid choice.")
        return

    key_size = int(input("Enter the size of the key matrix: "))

    if key_size <= 1:
        print("Key matrix size should be greater than 1.")
        return

    key_matrix = []
    print("Enter the key matrix elements row by row (separate by space):")
    for _ in range(key_size):
        row = input().split()
        if len(row) != key_size:
            print(f"Each row of the key matrix should have {key_size} elements.")
            return
        key_matrix.append([int(x) % 26 for x in row])

    key_matrix = np.array(key_matrix)

    if key_matrix.shape[0] != key_matrix.shape[1]:
        print("Key matrix should be square.")
        return

    if choice == 'E':
        plaintext = input("Enter the plaintext: ")
        ciphertext = encrypt(plaintext, key_matrix)
        print("Ciphertext:", ciphertext)
    else:
        ciphertext = input("Enter the ciphertext: ")
        decrypted_text = decrypt(ciphertext, key_matrix)
        print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()