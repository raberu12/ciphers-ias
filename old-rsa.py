import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Calculate the modular multiplicative inverse of e modulo phi."""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

def generate_keypair(p, q):
    """Generate public and private keypair."""
    print(f"Generating keypair with p={p} and q={q}")
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    
    # Calculate n and phi
    n = p * q
    print(f"n={n}")
    phi = (p - 1) * (q - 1)
    print(f"phi={phi}")
    
    e = 17
    if gcd(e, phi) != 1:
        raise ValueError("e and phi are not coprime")
    print(f"e={e}")
    
    # Calculate private key d
    d = mod_inverse(e, phi)
    print(f"d={d}")
    
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    """Encrypt the plaintext using public key."""
    e, n = public_key
    # Convert plaintext to number and encrypt
    message = int(plaintext)
    if message >= n:
        raise ValueError("Message is too large for the current key size")
    cipher = pow(message, e, n)
    return cipher

def decrypt(private_key, ciphertext):
    """Decrypt the ciphertext using private key."""
    d, n = private_key
    # Decrypt and convert back to string
    plaintext = pow(ciphertext, d, n)
    return str(plaintext)

# Example usage
def main():
    # Generate keypair using p=7, q=11 as in the example
    p = 7
    q = 11
    public_key, private_key = generate_keypair(p, q)
    
    # Print the keys
    print(f"Public Key (e,n): {public_key}")
    print(f"Private Key (d,n): {private_key}")
    
    # Example message
    message = "8"
    print(f"\nOriginal message: {message}")
    
    # Encrypt the message
    encrypted_msg = encrypt(public_key, message)
    print(f"Encrypted message: {encrypted_msg}")
    
    # Decrypt the message
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")

if __name__ == "__main__":
    main()