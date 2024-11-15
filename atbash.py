def atbash_cipher(text):
    # Create translation table
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = alphabet[::-1]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        reversed_alphabet + reversed_alphabet.upper()
    )
    
    # Translate the text
    return text.translate(translation_table)

# Example usage
plain_text = input("Enter text to encrypt: ")
encrypted_text = atbash_cipher(plain_text)
print("Encrypted:", encrypted_text)

# Decrypt by using the same function
decrypted_text = atbash_cipher(encrypted_text)
print("Decrypted:", decrypted_text)
