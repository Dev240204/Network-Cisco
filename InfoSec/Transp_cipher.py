def encrypt_transposition(plain_text, key):
    plain_text_without_space = plain_text.replace(" ", "")
    num_columns = len(plain_text_without_space) // len(key)
    num_rows = len(key)
    matrix = [[' '] * num_rows for i in range(num_columns)]
    char_counter = 0

    # filling the matrix
    for i in range(num_columns):
        for j in range(num_rows):
            matrix[i][j] = plain_text_without_space[char_counter]
            char_counter += 1

    cipher_text = ""
    index_order = [0] * len(key)
    temp_index = 1

    # ordering the index
    for i in range(len(key)):
        for j in range(len(key)):
            current_char = int(key[j])
            if current_char == temp_index:
                index_order[i] = j
        temp_index += 1

    # writing the cipher text using index order  
    for i in range(num_rows):
        for j in range(num_columns):
            cipher_text += matrix[j][index_order[i]]

    return cipher_text

def decrypt_transposition(cipher_text, key):
    index_order = [0] * len(key)
    num_rows = len(key)
    num_columns = len(cipher_text) // len(key)
    matrix = [[' '] * num_rows for i in range(num_columns)]
    temp_index = 1

    # ordering the index 
    for i in range(len(key)):
        for j in range(len(key)):
            current_char = int(key[j])
            if current_char == temp_index:
                index_order[i] = j
        temp_index += 1

    # filling the matrix again using the cipher text
    char_counter = 0
    for i in range(num_rows):
        for j in range(num_columns):
            matrix[j][index_order[i]] = cipher_text[char_counter]
            char_counter += 1

    # writing the plain text again from the matrix 
    plain_text = ""
    for i in range(num_columns):
        for j in range(num_rows):
            plain_text += matrix[i][j]

    return plain_text

def main():
    plaintext = input("Enter the text to be encrypted: ")
    key = input("Enter the key: ")
    cipher = encrypt_transposition(plaintext, key)
    print("Cipher Text:", cipher)
    decrypted_text = decrypt_transposition(cipher, key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
