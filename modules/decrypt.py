def decrypt(text, shift):
    """
    Decrypts the input text using a Caesar cipher by shifting in the opposite direction.

    Parameters:
    text (str): The string to be decrypted.
    shift (int): The number of positions the text was originally shifted.

    Returns:
    str: The decrypted string.
    """
    from modules.encrypt import encrypt
    return encrypt(text=text,shift=-shift)
#print(decrypt("mn",5))