import random
import string

class VernamCipher:
    @staticmethod
    def generate_key(length):
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
    
    @staticmethod
    def text_to_numbers(text):
        return [ord(c) - ord('A') for c in text.upper()]
    
    @staticmethod
    def numbers_to_text(numbers):
        return ''.join(chr(n + ord('A')) for n in numbers)
    
    @staticmethod
    def encrypt(plaintext, key):
        plaintext_nums = VernamCipher.text_to_numbers(plaintext)
        key_nums = VernamCipher.text_to_numbers(key)
        cipher_nums = [(p + k) % 26 for p, k in zip(plaintext_nums, key_nums)]
        return VernamCipher.numbers_to_text(cipher_nums)
    
    @staticmethod
    def decrypt(ciphertext, key):
        ciphertext_nums = VernamCipher.text_to_numbers(ciphertext)
        key_nums = VernamCipher.text_to_numbers(key)
        plaintext_nums = [(c - k) % 26 for c, k in zip(ciphertext_nums, key_nums)]
        return VernamCipher.numbers_to_text(plaintext_nums)

def main():
    message = "GODWINMONSERATE"
    print(f"Original message: {message}")
    key = VernamCipher.generate_key(len(message))
    print(f"Generated key: {key}")
    encrypted = VernamCipher.encrypt(message, key)
    print(f"Encrypted message: {encrypted}")
    decrypted = VernamCipher.decrypt(encrypted, key)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()