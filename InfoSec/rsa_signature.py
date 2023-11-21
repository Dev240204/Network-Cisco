def _gcd(p, q):
    if q == 0:
        return p
    else:
        r = p % q
        return _gcd(q, r)

def exteuclid(a, b):
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

p = 823
q = 953
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
    print("No possible encryption key!!!")
    exit(0)

M = 12345

# Signature is created by Andy
S = (M**d) % n

# Andy sends the message M and Signature S to Bert
# Bert verifies the signature using Andy's public key (e, n)

M1 = (S**e) % n

if M == M1:
    print("As M == M1, the Message is Accepted and the sender is verified as Andy!")
else:
    print("As M not equal to M1, the message is rejected!")




# MODEL 2 for message confidentiality and sender's authentication

def _gcd(p, q):
    if q == 0:
        return p
    else:
        r = p % q
        return _gcd(q, r)

def exteuclid(a, b):
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

p = 823
q = 953
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

M = 14123

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

