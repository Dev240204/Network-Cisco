#model 1 sender authentication
def _gcd(p, q):
    if q == 0:
        return p
    else:
        r = p % q
        return _gcd(q, r)

def exteuclid(a, b):    #to calculate the extended Euclidean algorithm to find modular multiplicative inverses
    r_1 = a
    r_2 = b
    s_1 = 1
    s_2 = 0
    t_1 = 0
    t_2 = 1
    while r_2 > 0:
        temp = r_1 // r_2
        r = r_1 - temp * r_2
        r_1 = r_2
        r_2 = r
        s = s_1 - temp * s_2
        s_1 = s_2
        s_2 = s
        t = t_1 - temp * t_2
        t_1 = t_2
        t_2 = t
    if t_1 < 0:
        t_1 = t_1 % a
    return (r_1, t_1)

p = int(input('Enter value of p: '))    # p = 823
q = int(input('Enter value of q: '))    # q = 953
n = p * q
Pn = (p - 1) * (q - 1)

possible_key = []       # Initialize an empty list to store possible encryption keys

for i in range(2, Pn):
    gcd = _gcd(Pn, i)   #Calculate the GCD of φ(n) and i using the _gcd() function
    if gcd == 1:        #Check if the GCD is equal to 1, indicating that i is coprime with φ(n)
        possible_key.append(i)

e = -1                  #Initialize a variable e to -1, which will store the encryption key.
for key in possible_key:
    r, d = exteuclid(Pn, key)
    if r == 1:          #Check if the GCD result r is equal to 1, indicating that the modular inverse exists.
        d = int(d)      # Convert the calculated modular multiplicative inverse d to an integer
        e = int(key)    #Convert the encryption key key to an integer and store it in the variable e.
        print("Encryption Key is: ", e)
        print("Decryption Key is: ", d)
        break

if e == -1:
    print("No possible encryption key")
    exit(0)

M = int(input('Enter original message(int only): ')) #14123

# Signature is created by Andy
S = (M**d) % n

# Andy sends the message M and Signature S to Bert
# Bert verifies the signature using Andy's public key (e, n) and checks if the received message matches the original message.

M1 = (S**e) % n

if M == M1:
    print("As M == M1, the Message is Accepted and the sender is verified as Andy!")
else:
    print("As M not equal to M1, the message is rejected!")
print()



# MODEL 2 for message confidentiality and sender's authentication

# p = 823
# q = 953
p = int(input('Enter value of p: '))
q = int(input('Enter value of q: '))
n = p * q
Pn = (p - 1) * (q - 1)

possible_key = []

for i in range(2, Pn):
    gcd = _gcd(Pn, i)
    if gcd == 1:
        possible_key.append(i)

e = -1
for key in possible_key:
    r, d = exteuclid(Pn, key)
    if r == 1:
        d = int(d)
        e = int(key)
        print("Encryption Key is: ", e)
        print("Decryption Key is: ", d)
        break

if e == -1:
    print("No possible encryption key")
    exit(0)

M = int(input('Enter original message(int only): ')) #14123

# Message encryption
C = (M**e) % n

# Signature is created by Andy
S = (C**d) % n

# Andy sends the message C (encrypted) and Signature S to Bert

# Bert decrypts the message C using Andy's public key (e, n)
M1 = (C**e) % n

if M == M1:
    print("Sender is verified as Andy.")
    # Now Bert can use the decrypted message for further processing.
    print("Decrypted Message:", M1)
else:
    print("As M not equal to M1, the sender is not verified, and the message is rejected!")