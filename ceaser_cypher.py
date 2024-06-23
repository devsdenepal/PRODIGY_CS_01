from modules import encrypt,decrypt,logo, slow_type
#print the logo
logo.logo()
choice = input("Choose one to continue! \n1. Encrypt-->e \n2.Decrypt-->d\n-->").lower()
if 'e' in choice:
    text = input('Please enter the text to encrypt!\n-->')
    shift = int(input('Please enter letter shift to encrypt!\n-->'))
    slow_type.slowType(encrypt.encrypt(text,shift))
elif 'd' in choice:
    text = input('Please enter the text to decrypt!\n-->')
    shift = int(input('Please enter letter shift to decrypt!\n-->'))
    slow_type.slowType(decrypt.decrypt(text,shift))
