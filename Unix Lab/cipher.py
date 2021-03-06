import sys 

def encrypt(message, key):
    # Discard all the punctuation marks, digits, blanks, and anything else from the input string.
    INCLUSION_STRING = "QWERTYUIOPASDFGHJKLZXCVBNM"
    encrypted_message = ""

    for character in message:
        if character in INCLUSION_STRING:
            encrypted_message += chr(( ord(character) + key - 65) % 26 + 65)
    return encrypted_message

def print_encrypted_message(encoded_message):
    """
    Print the final encoded message in blocks of five letters to the screen (stdout), ten blocks per line. 
    The last line may be shorter than five blocks, and the last block may be shorter than five letters.
    """
    line_count = 0
    for index, char in enumerate(encoded_message):
        if line_count == 10:
            print("")
            line_count = 0
        print(char, end="")
        if index % 5 == 4:
            print(" ", end="")
            line_count += 1
    print("")
   
    


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please add a key argument!")
    elif len(sys.argv) == 2:
        try:
            key = int(sys.argv[1])
        except Exception:
            print("This was not a valid key! Try again with a number!")
    else:
        print("Please only add one key argument!")
    
    message = input("Enter your unencoded message: ")
    # Convert the message to all uppercase.
    message = message.upper()
    # Final Method
    print_encrypted_message(encrypt(message, key))
