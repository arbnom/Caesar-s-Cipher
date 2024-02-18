import random

def caesar_cipher_encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        # Convert to lowercase if it's not
        char = char.lower()
        # Check if the character is a lowercase letter
        if char.islower():
            encrypted_char = chr((ord(char) - 97 + key) % 26 + 97)
            encrypted_text += encrypted_char.upper()  # Convert to uppercase
        else:
            # Keep the character unchanged if it's not a letter
            encrypted_text += char.upper()
    return encrypted_text

# Choose a random key between 1 and 25
key = random.randint(1, 25)
print(f"Key: {key}")

# Set the plaintext directly
plaintext = "web three is a future"

# Encrypt the plaintext
encrypted_text = caesar_cipher_encrypt(plaintext, key)

# Print the encrypted text
print(f"Encrypted Text: {encrypted_text}")
