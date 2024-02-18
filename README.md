# Caeser-s-Cipher
This repository hosts a collection of Python scripts designed to illustrate fundamental cryptographic concepts. It serves as a companion to the blog on Caeser's cipher, providing hands-on examples to reinforce learning and exploration.

## Files Description

- **caesar_cipher.py**
  - Provides functionality to encrypt a plaintext message using the Caesar cipher. The script randomly selects a key and demonstrates the encryption process.

- **brute_force.py**
  - Implements a brute-force approach to decrypt a message encrypted with the Caesar cipher. It tries all possible shifts and prints the decrypted text for each key.

- **frequency_analysis.py**
  - Utilizes frequency analysis to estimate the key of a Caesar cipher encrypted message. It compares the frequency of letters in the ciphertext with those in standard English to find the most likely key.

- **frequency_analysis_debug.py**
  - A debugging variant of `frequency_analysis.py`, likely containing additional print statements or modified logic to troubleshoot and fine-tune the frequency analysis process.

- **mono_alphabetic_encryption.py**
  - Implements a monoalphabetic cipher for encrypting plaintext. This script likely outlines a more complex encryption scheme compared to the Caesar cipher, using a fixed substitution method.
