import argparse
from modules import encrypt, decrypt, logo, slow_type

def main():
    # Define the argument parser
    parser = argparse.ArgumentParser(description='Encrypt or decrypt a text using a Caesar cipher.')
    parser.add_argument('-m', '--mode', choices=['e', 'd'], help='Mode: e for encrypt, d for decrypt')
    parser.add_argument('-t', '--text', help='The text to be encrypted or decrypted')
    parser.add_argument('-s', '--shift', type=int, help='The letter shift for encryption or decryption')

    args = parser.parse_args()

    # Print the logo
    logo.logo()

    if args.mode and args.text and args.shift is not None:
        # If all command-line arguments are provided, use them
        mode = args.mode
        text = args.text
        shift = args.shift
    else:
        # Otherwise, fall back to interactive input
        mode = input("Choose one to continue! \n1. Encrypt-->e \n2.Decrypt-->d\n-->").lower()
        if 'e' in mode :print("=== encrypting mode ===")
        else: print("=== encrypting mode ===")
        text = input('Please enter the text to encrypt/decrypt!\n-->')
        shift = int(input('Please enter letter shift to encrypt/decrypt!\n-->'))

    if 'e' in mode:
        slow_type.slowType(encrypt.encrypt(text, shift))
    elif 'd' in mode:
        slow_type.slowType(decrypt.decrypt(text, shift))

if __name__ == '__main__':
    main()
