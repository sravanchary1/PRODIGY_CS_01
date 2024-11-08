def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    shift = shift if mode == "encrypt" else -shift
    
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

while True:
    print("\nCaesar Cipher Program")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ")
    
    if choice == "3":
        print("Exiting the program.")
        break
    elif choice in ("1", "2"):
        message = input("Enter your message: ")
        shift = int(input("Enter shift value: "))
        
        if choice == "1":
            encrypted_message = caesar_cipher(message, shift, mode="encrypt")
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = caesar_cipher(message, shift, mode="decrypt")
            print("Decrypted message:", decrypted_message)
    else:
        print("Invalid option. Please choose 1, 2, or 3.")