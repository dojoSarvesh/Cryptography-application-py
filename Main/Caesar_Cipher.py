def cs_encrypt(text,key1):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        
        if (char.isupper()):
            result += chr((ord(char) + key1-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        elif (char.islower()):
            result += chr((ord(char) + key1 - 97) % 26 + 97)
        else:
             result += char
    return result
def cs_decrypt(text,key1):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        
        if (char.isupper()):
            result += chr((ord(char) - key1-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        elif (char.islower()):
            result += chr((ord(char) - key1 - 97) % 26 + 97)
        else:
            result += char
    return result