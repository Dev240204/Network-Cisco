import random
import math

def select_prime_numbers():
    prime_numbers = [0, 0]
    count = 0
    while count < 2:
        rand_number = random.randint(1, 99)
        if is_prime(rand_number):
            prime_numbers[count] = rand_number
            count += 1
    return prime_numbers

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def calculate_fi_n(prime_numbers):
    fi_n = (prime_numbers[0] - 1) * (prime_numbers[1] - 1)
    return fi_n

def calculate_n(prime_numbers):
    n = prime_numbers[0] * prime_numbers[1]
    return n

def calculate_gcd(e, fi_n):
    while fi_n % e != 0:
        e, fi_n = fi_n % e, e
    return e == 1

def find_e(prime_numbers):
    fi_n = calculate_fi_n(prime_numbers)
    e = 2
    while e < fi_n and e > 1:
        if calculate_gcd(e, fi_n):
            break
        else:
            e += 1
    return e

def find_d(prime_numbers, e):
    fi_n = calculate_fi_n(prime_numbers)
    for i in range(fi_n):
        if (e * i) % fi_n == 1:
            return i
    return -1

def encrypt(message, prime_numbers):
    n = calculate_n(prime_numbers)
    e = find_e(prime_numbers)
    cipher = pow(message, e, n)
    return cipher

def decrypt(cipher, prime_numbers):
    e = find_e(prime_numbers)
    d = find_d(prime_numbers, e)
    n = calculate_n(prime_numbers)
    result = 1
    base = cipher
    exponent = d

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % n
        base = (base * base) % n
        exponent //= 2

    return result

if __name__ == "__main__":
    message = int(input("Enter your message that should be less than " + str(calculate_n(select_prime_numbers())) + ": "))

    prime_numbers = select_prime_numbers()
    print("1 Prime No: " + str(prime_numbers[0]) + ", 2 Prime No: " + str(prime_numbers[1]))
    print("Public Key: " + str(find_e(prime_numbers)))
    print("Private Key: " + str(find_d(prime_numbers, find_e(prime_numbers))))

    cipher = encrypt(message, prime_numbers)
    plain = decrypt(cipher, prime_numbers)
    print("Cipher: " + str(cipher))
    print("Plain: " + str(plain))
