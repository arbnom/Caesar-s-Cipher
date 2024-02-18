def caesar_cipher_decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        # Check if the character is an uppercase letter
        if 'A' <= char <= 'Z':
            # Perform decryption only on uppercase letters
            decrypted_char = chr((ord(char) - 65 - key) % 26 + 65)
            decrypted_text += decrypted_char.lower()  # Convert decrypted letters to lowercase for consistency
        else:
            # Leave non-letter characters unchanged
            decrypted_text += char
    return decrypted_text

# Ciphertext input is provided directly in the code
ciphertext = "ZHE WKUHH LV D IXWXUH"

# Try all possible keys from 1 to 25
for i in range(1, 26):
    # Decrypt the ciphertext using the current key
    decrypted_text = caesar_cipher_decrypt(ciphertext, i)
    # Print the decrypted text
    print(f"Key {i}: {decrypted_text}")
