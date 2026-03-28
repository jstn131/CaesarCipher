# Caesar Cipher logic
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S",
            "T", "U", "V", "W", "X", "Y", "Z"]

# Changed from a console based format to a 
# web based format. 
# encode and decode can now be imported and used
# by any other file, such as our flask web application!

# We will input a message and shift value
# The function will then do all work and 
# return the encoded message
def encode(msg, shift):
    encoded = ""    # Will append to this and return it at the end,
    msg = msg.upper() # Convert to uppercase for easier comparison
    for char in msg:
        if char in alphabet:    # If in our list, encode it
            new_position = (alphabet.index(char) + shift) % 26
            encoded += alphabet[new_position]
        else:
            encoded += char # If not in our list, either space or special char. Just append
    return encoded


# Logic from above same here but in reverse for shift.
def decode(msg, shift):
    decoded = ""
    msg = msg.upper()
    for char in msg:
        if char in alphabet:
            new_position = (alphabet.index(char) - shift) % 26
            decoded += alphabet[new_position]
        else:
            decoded += char
    return decoded