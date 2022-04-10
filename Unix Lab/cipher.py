import sys 


def encrypt(key):
    pass


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
    