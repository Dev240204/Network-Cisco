def encrypt(text, salt):
    encrypted_result = ""
    text = text.lower()
    
    for i in range(len(text)):
        character = text[i]
        encrypted_result += chr((ord(character) + salt - 97) % 26 + 97)
        
    return encrypted_result


def decrypt(text, salt):
    decrypted_result = ""
    text = text.lower()
    
    for i in range(len(text)):
        character = text[i]
        decrypted_result += chr((ord(character) - salt - 97) % 26 + 97)
        
    return decrypted_result


def brute_force_attack(text):
    for i in range(26):
        print(i, "  ", decrypt(text, i))


def analyze_frequency(text):
    frequency_count = {}
    
    for i in range(len(text)):
        character = text[i]
        
        if character in frequency_count:
            frequency_count[character] += 1
        else:
            frequency_count[character] = 1
    
    print(frequency_count)


def main():
    print("Enter the text to be encrypted:")
    text = input()
    print("Enter the salt value:")
    salt = int(input())
    
    encrypted_text = encrypt(text, salt)
    decrypted_text = decrypt(encrypted_text, salt)

    while(True):
        switch = int(input("Enter 1 to encrypt\nEnter 2 to decrypt\nEnter 3 for brute force decryption\nEnter 4 for frequecy analysis\nEnter 0 to exit\n"))
        if switch == 1:
            print("The encrypted text is:")
            print(encrypted_text)
        elif switch == 2:
            print("The decrypted text is:")
            print(decrypted_text)
        elif switch == 3:
            print("Brute force decryption attempts:")
            brute_force_attack(encrypted_text)
        elif switch == 4:
            print("Frequency analysis results:")
            analyze_frequency(encrypted_text)
        elif switch == 0:
            break

if __name__ == "__main__":
    main()
