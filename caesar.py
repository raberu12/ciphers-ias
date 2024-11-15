def caesar(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
            
    return result

plaintext = input("Enter message to encrypt: ")

for i in range(26):
    print(f"Shift {i}: {caesar(plaintext, i)}")
