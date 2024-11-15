def vigenere_cipher(text, key, mode):
    result = []
    key = key.lower()
    text = text.lower()
    
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            if mode == 'encrypt':
                new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif mode == 'decrypt':
                new_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            
            result.append(new_char)
            key_index += 1
        else:
            result.append(char) 
            
    return ''.join(result)

text = input("Enter a message: ")
key = input("Enter key: ")
mode = input("Enter mode (encrypt/decrypt): ")
encrypted_text = vigenere_cipher(text, key, mode)
print(f"{mode} text:", encrypted_text)
