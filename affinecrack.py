def affine_decrypt(ciphertext, a, b):
    plaintext = ""
    a_inverse = find_multiplicative_inverse(a, 26)
    for char in ciphertext:
        if char.isalpha():
            ciphertext_letter = ord(char) - 65  # Convert to numeric representation (0-25)
            plaintext_letter = (a_inverse * (ciphertext_letter - b)) % 26
            plaintext += chr(plaintext_letter + 65)  # Convert back to alphabetic representation
        else:
            plaintext += char
    return plaintext

def find_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_brute_force(ciphertext):
    possible_a_values = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    possible_b_values = list(range(26))
    for a in possible_a_values:
        for b in possible_b_values:
            decrypted_text = affine_decrypt(ciphertext, a, b)
            print(f"Key (a, b): ({a}, {b}) - Decrypted Text: {decrypted_text}")

# Example usage
ciphertext = "PRUUN, TOLSD!"
affine_brute_force(ciphertext)
