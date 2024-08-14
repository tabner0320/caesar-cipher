
def caesar_cipher(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Leave non-alphabetical characters unchanged
        else:
            result += char
    
    return result

# Example Usage:
text = "HELLO"
shift = 3
print(caesar_cipher(text, shift))  # Output: KHOOR

