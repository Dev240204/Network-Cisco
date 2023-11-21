# Program to implement RailFence Technique
def encrypt(plaintext, depth):
    plaintext = plaintext.upper().replace(" ", "")
    grid = [[" " for i in range(len(plaintext))] for j in range(depth)]
    row = 0
    flag = False
    for i in range(len(plaintext)):
        grid[row][i] = plaintext[i]
        if row == 0:
            flag = False
        elif row == depth - 1:
            flag = True

        if flag:
            row -= 1
        else:
            row += 1

    encrypted_text = []
    for i in range(depth):
        for j in range(len(plaintext)):
            if grid[i][j] != " ":
                encrypted_text.append(grid[i][j])
    encrypted_text = "".join(encrypted_text)
    return encrypted_text

def decrypt(cipher, depth):
    grid = [[" " for i in range(len(cipher))] for j in range(depth)]
    flag = False
    row= 0

    for i in range(len(cipher)):
        if row == 0:
            flag = False
        elif row == depth - 1:
            flag = True

        grid[row][i] = "*"

        if flag:
            row -= 1
        else:
            row += 1
    
    index = 0
    for i in range(depth):
        for j in range(len(cipher)):
            if (grid[i][j] == "*") and (index < len(cipher)):
                grid[i][j] = cipher[index]
                index += 1

    decrypted_text = []
    row= 0
    for i in range(len(cipher)):
        if row == 0:
            flag = False
        elif row == depth - 1:
            flag = True

        if grid[row][i] != "*":
            decrypted_text.append(grid[row][i])

        if flag:
            row -= 1
        else:
            row += 1
    return "".join(decrypted_text)

def main():
    while True:
        print("1.Encrypt")
        print("2.Decrypt")
        print("3.Exit")
        choice = int(input("Enter the choice number : "))
        if choice == 1:
            text = input("Enter the Plain Text : ")
            depth = int(input("enter the depth : "))
            print("Encrypted Text : ", encrypt(text, depth))
        elif choice == 2:
            text = input("Enter the Cipher Text : ")
            depth = int(input("enter the depth : "))
            print("Decrypted Text : ", decrypt(text, depth))
        elif choice == 3:
            print("Exit")
            break
        else:
            print("Invalid choice")

main()
