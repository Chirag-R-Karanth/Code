def caesercypher(text, shift):
    """
    Encrypts or decrypts a message using the Caesar cipher.

    Args:
        text (str): The message to be processed.
        shift (int): The number of positions to shift each letter.

    Returns:
        str: The encrypted or decrypted message.
    """
    result = ""

    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                start = ord('A')
                shifted_char_code = (ord(char) - start + shift) % 26 + start
                result += chr(shifted_char_code)
            # Handle lowercase letters
            else:
                start = ord('a')
                shifted_char_code = (ord(char) - start + shift) % 26 + start
                result += chr(shifted_char_code)
        else:
            # Keep non-alphabetic characters as they are
            result += char

    return result

# --- Examples of use ---

# Encryption
message = "Hello, World!"
shift_value = 3
encrypted_message = caesercypher(message, shift_value)
print(f"Original message: {message}")
print(f"Encrypted message (shift {shift_value}): {encrypted_message}")

# Decryption (to decrypt, you can use a negative shift or a shift of 26 - shift_value)
decrypted_message = caesercypher(encrypted_message, -shift_value)
# Or: decrypted_message = caesar_cipher(encrypted_message, 26 - shift_value)
print(f"Decrypted message (shift {-shift_value}): {decrypted_message}")