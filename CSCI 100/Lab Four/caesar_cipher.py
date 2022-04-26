# An encoder/decoder for our spies to secretly send messages.

encryption_option = input("Would you like to Encode or Decode? ") 

# should_encode will be true if the user 
should_encode = "encode" in encryption_option.lower()
should_decode = "decode" in encryption_option.lower()

# Ask the user for their message and cipher number.
cipher_number = int(input("What is your cipher number? "))
message = input("What is your message? ")

encrypted_message = ""
if should_encode:
    for char in message:
        if char in (",", " ", '"', ".", "!", "@", "#", "$", "-", "+", "="):
            encrypted_message += char
        elif char.isupper():
            encrypted_message += chr((ord(char) + cipher_number-65) % 26 + 65)

        elif char.islower():
            encrypted_message += chr((ord(char) + cipher_number - 97) % 26 + 97)        

    print(encrypted_message)
elif should_decode:
    unencrypted_message = ""
    for char in message:
        if char in (",", " "):
            unencrypted_message += char
        elif char.isupper():
            unencrypted_message += chr((ord(char) - cipher_number - 65) % 26 + 65)

        elif char.islower():
            unencrypted_message += chr((ord(char) - cipher_number - 97) % 26 + 97)        

    print(unencrypted_message)
else:
    print("We only support encrypting/decrypting, sorry!")


def All_Knowing_Decrypter(message):
    decrypted_message = ""
    
    for i in range(1, 27):
        for char in message:
            if char in (",", " ", '"', ".", "!", "@", "#", "$", "-", "+", "="):
                decrypted_message += char
            elif char.isupper():
                decrypted_message += chr((ord(char) + i-65) % 26 + 65)
    
            elif char.islower():
                decrypted_message += chr((ord(char) + i - 97) % 26 + 97)
    
                   
        print(f"Possible message {i} : {decrypted_message} \n")
        decrypted_message = ""
