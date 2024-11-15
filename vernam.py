
def stringEncryption(text, key):
	# Initializing cipherText
	cipherText = ""
	cipher = []
	for i in range(len(key)):
		cipher.append(ord(text[i]) - ord('A') + ord(key[i])-ord('A'))
	for i in range(len(key)):
		if cipher[i] > 25:
			cipher[i] = cipher[i] - 26
	for i in range(len(key)):
		x = cipher[i] + ord('A')
		cipherText += chr(x)
	return cipherText
def stringDecryption(s, key):
	plainText = ""
	plain = []

	for i in range(len(key)):
		plain.append(ord(s[i]) - ord('A') - (ord(key[i]) - ord('A')))

	for i in range(len(key)):
		if (plain[i] < 0):
			plain[i] = plain[i] + 26

	for i in range(len(key)):
		x = plain[i] + ord('A')
		plainText += chr(x)

	return plainText

def randomKeyGenerator(length):
	key = ""
	for i in range(length):
		key += chr(ord('A') + i)
	return key

plainText = input("Enter message to encrypt: ")

key = input("Enter key: ")
if key == "":
	key = randomKeyGenerator(len(plainText))
elif len(key) != len(plainText) and key != "":
	print("Key length should be equal to message length")
	exit()

encryptedText = stringEncryption(plainText.upper(), key.upper())

mode = input("Enter mode (encrypt/decrypt): ")
if mode.lower() == "encrypt":
	print("Encrypted message:", encryptedText)
elif mode.lower() == "decrypt":
	print("Decrypted message:", stringDecryption(plainText.upper(), key.upper()))
else:
	print("Invalid mode")

