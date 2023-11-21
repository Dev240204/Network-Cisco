import random
import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_primes():
    p = random.randint(100, 500)
    q = random.randint(100, 500)

    while not is_prime(p):
        p += 1

    while not is_prime(q) or q == p:
        q += 1

    return p, q

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)

    d = mod_inverse(e, phi)

    return ((n, e), (n, d))

def encrypt(public_key, message):
    n, e = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted

def decrypt(private_key, encrypted_message):
    n, d = private_key
    decrypted = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted)

if __name__ == '__main__':
    p, q = generate_primes()
    public_key, private_key = generate_keypair(p, q)

    message = "Hellosot"
    print("Original message:", message)

    encrypted_message = encrypt(public_key, message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)
