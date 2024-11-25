import math
import random
from typing import Tuple, Union

class RSA:
    def __init__(self, key_size: int = 32):
        """Initialize RSA with given key size in bits."""
        self.key_size = key_size
        self.public_key = None
        self.private_key = None

    @staticmethod
    def is_prime(n: int, k: int = 5) -> bool:
        """
        Test if a number is prime using Miller-Rabin primality test.
        k determines the accuracy of the test.
        """
        if n < 2: 
            return False
        if n == 2 or n == 3: 
            return True
        if n % 2 == 0: 
            return False

        # Write n-1 as 2^r * d
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        # Witness loop
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def generate_prime(self) -> int:
        """Generate a random prime number of specified bit length."""
        while True:
            # Generate random odd number of specified bit length
            num = random.getrandbits(self.key_size)
            num |= (1 << self.key_size - 1) | 1  # Make sure it's odd and has correct bit length
            if self.is_prime(num):
                return num

    @staticmethod
    def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        """Extended Euclidean Algorithm."""
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = RSA.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    @staticmethod
    def mod_inverse(e: int, phi: int) -> int:
        """Calculate the modular multiplicative inverse of e modulo phi."""
        gcd, x, _ = RSA.extended_gcd(e, phi)
        if gcd != 1:
            raise ValueError("Modular inverse does not exist")
        return x % phi

    def generate_keypair(self) -> None:
        """Generate public and private keypair."""
        # Generate two distinct primes
        p = self.generate_prime()
        q = self.generate_prime()
        while p == q:  # Ensure p and q are different
            q = self.generate_prime()

        n = p * q
        phi = (p - 1) * (q - 1)

        # Common choices for e are 65537 (2^16 + 1) as it's prime and has only two 1s in binary
        e = 65537
        while math.gcd(e, phi) != 1:
            e = random.randrange(3, phi, 2)

        d = self.mod_inverse(e, phi)

        self.public_key = (e, n)
        self.private_key = (d, n)

    def encrypt(self, message: Union[str, int]) -> int:
        """
        Encrypt a message using the public key.
        Message can be either a string of digits or an integer.
        """
        if self.public_key is None:
            raise ValueError("Please generate keys first using generate_keypair()")
        
        e, n = self.public_key
        
        # Convert string message to integer if necessary
        if isinstance(message, str):
            try:
                message = int(message)
            except ValueError:
                raise ValueError("Message must be a string of digits or an integer")

        if message >= n:
            raise ValueError("Message is too large for the current key size")
        
        return pow(message, e, n)

    def decrypt(self, ciphertext: int) -> str:
        """Decrypt a ciphertext using the private key."""
        if self.private_key is None:
            raise ValueError("Please generate keys first using generate_keypair()")
        
        d, n = self.private_key
        return str(pow(ciphertext, d, n))

def main():
    # Create RSA instance with 32-bit key size
    # Note: In practice, you'd want at least 2048 bits for security
    # but we're using 32 bits for demonstration purposes
    rsa = RSA(key_size=32)
    
    # Generate new keypair
    print("Generating keypair...")
    rsa.generate_keypair()
    print(f"Public Key (e,n): {rsa.public_key}")
    print(f"Private Key (d,n): {rsa.private_key}")
    
    # Example message
    message = "12345"
    print(f"\nOriginal message: {message}")
    
    try:
        # Encrypt the message
        encrypted_msg = rsa.encrypt(message)
        print(f"Encrypted message: {encrypted_msg}")
        
        # Decrypt the message
        decrypted_msg = rsa.decrypt(encrypted_msg)
        print(f"Decrypted message: {decrypted_msg}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()