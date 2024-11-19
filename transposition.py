import math

def encryptMessage(msg, key):
    cipher = ""
    # Track positions of repeated letters using enumeration
    key_order = [(c, i) for i, c in enumerate(key)]
    # Sort by character first, then by original position
    key_sorted = sorted(key_order)
    
    msg_len = float(len(msg))
    msg_lst = list(msg)
    
    # Calculate dimensions
    col = len(key)
    row = int(math.ceil(msg_len / col))
    
    # Pad message
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    
    # Create matrix
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]
    
    # Read off columns according to sorted key positions
    for _, original_pos in key_sorted:
        cipher += ''.join(row[original_pos] for row in matrix)
    
    return cipher

def decryptMessage(cipher, key):
    # Track positions of repeated letters using enumeration
    key_order = [(c, i) for i, c in enumerate(key)]
    # Sort by character first, then by original position
    key_sorted = sorted(key_order)
    
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    
    # Calculate dimensions
    col = len(key)
    row = int(math.ceil(msg_len / col))
    
    # Create empty matrix
    dec_cipher = [[None] * col for _ in range(row)]
    
    # Calculate column lengths
    col_lengths = [row] * col
    
    # Fill in matrix column by column
    msg_idx = 0
    for _, original_pos in key_sorted:
        for j in range(row):
            dec_cipher[j][original_pos] = msg_lst[msg_idx]
            msg_idx += 1
    
    # Convert matrix to string and remove padding
    msg = ''
    for i in range(row):
        for j in range(col):
            if dec_cipher[i][j] != '_':
                msg += dec_cipher[i][j]
    
    return msg

msg = "GODWINMONSERATE"
key = "CEBUCITY"

cipher = encryptMessage(msg, key)
print("Original Message: {}".format(msg))
print("Key: {}".format(key))
print("Encrypted Message: {}".format(cipher))

decrypted = decryptMessage(cipher, key)
print("Decrypted Message: {}".format(decrypted))