# Used to encode and decode data
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*",
              "(", ")", "-", "_", "=", "+", "{", "[", "]", "}", "\\", ":", ";", "\"", "'", ",", "<", ".", ">", "/", "?"]


def encrypt(code, shift):
    encrypted = ""
    for letter in code:
        if letter == " ":
            encrypted = encrypted + "|"
        else:
            location = (characters.index(letter) +
                        int(shift)) % len(characters)
            encrypted = encrypted + characters[location]
    return encrypted


def decrypt(code, shift):
    decrypted = ""
    for letter in code:
        if letter == "|":
            decrypted = decrypted + " "
        else:
            location = (characters.index(letter) - int(shift))
            if location < 0:
                location = len(characters) - 1 + location
            decrypted = decrypted + characters[location]
    return decrypted
