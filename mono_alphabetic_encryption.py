import random

# Generate a random permutation of numbers 0 to 25
key = random.sample(range(26), 26)
print(f"Key: {key}")

# Take plaintext input
plaintext = "Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thankyou very much. They werethe last people you’d expect to be involved in anything strange or mysterious, because they just didn’thold with such nonsense.Mr. Dursley was the director of a firm called Grunnings, whichmade drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thinand blonde and had nearly twice the usual amount of neck, whichcame in very useful as she spent so much of her time craning overgarden fences, spying on the neighbors. The Dursleys had a smallson called Dudley and in their opinion there was no finer boy anywhere.The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it."

def encrypt_with_monoalphabetic_cipher(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.islower():  # Check if it's a lowercase letter
            # Find the index of the letter in the alphabet (0-25), then find the corresponding letter in the key
            encrypted_char = chr(key[ord(char) - ord('a')] + ord('A'))  # Convert to uppercase after encryption
            encrypted_text += encrypted_char
        else:
            # Keep the character as it is if it's not a lowercase letter
            encrypted_text += char
    return encrypted_text

# Encrypt the plaintext
encrypted_text = encrypt_with_monoalphabetic_cipher(plaintext, key)

# Print the encrypted text
print(f"Encrypted Text: {encrypted_text}")