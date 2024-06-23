def encrypt(text, shift) :
    """
    Encrypts the input text using a Caesar cipher.

    Parameters:
    text (str): The string to be encrypted.
    shift (int): The number of positions to shift each character.

    Returns:
    str: The encrypted string.
    """
    result = ""
    
    
    for i in range(len(text)):
        char = text[i]
        
       
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
      
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        else:
            result += char
            
    return result
# print(encrypt("hi",5))