def calculate_frequency(text):
    frequency = {chr(i + 97): 0 for i in range(26)}  # Initialize frequency dictionary for 'a' to 'z'
    for char in text.lower():  # Convert text to lowercase to standardize
        if char in frequency:
            frequency[char] += 1
    total = sum(frequency.values())
    if total > 0:
        frequency = {char: count / total for char, count in frequency.items()}  # Normalize frequencies
    return frequency

# Frequencies of letters in the English alphabet (p_i values)
english_freq = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
    'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
    'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
    'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974,
    'z': 0.00074
}

# Ciphertext input
ciphertext = "ZHE WKUHH LV D IXWXUH".replace(" ", "").upper()  # Remove spaces and convert to uppercase for analysis

# List frequencies for letters in ciphertext (q_i values)
ciphertext_freq = calculate_frequency(ciphertext)

# Create a dictionary to hold I_j values
I_j_values = {}

# Calculate I_j for each possible shift j
for j in range(26):
    I_j = 0
    for i in range(26):
        char_from_english = chr((i + 97) % 126)  # Ensure we're using lowercase letters
        char_from_ciphertext = chr((i + j + 97) % 126)
        if char_from_english in english_freq and char_from_ciphertext in ciphertext_freq:
            I_j += english_freq[char_from_english] * ciphertext_freq[char_from_ciphertext]
    I_j_values[j] = I_j
    print(f"For j = {j}, I_j = {I_j:.4f}")


# Find the key by identifying the shift with I_j value nearest to 0.065
nearest_I_j_value = min(I_j_values.values(), key=lambda x: abs(x - 0.065))
key = [k for k, v in I_j_values.items() if v == nearest_I_j_value][0]


print(f"Estimated Key: {key}")
