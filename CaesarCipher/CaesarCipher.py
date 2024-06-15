SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?,.<>|~`ÁÉÍÓÚÝáéíóúý"
MAX_KEY_SIZE = len(SYMBOLS)
# Holds the number of characters in the symbols variable (maximum shift number)


def main():
    mode = get_mode()
    message = get_message()
    if mode[0] != "b":
        key = get_key()
        print("Your translated message is:")
        print(get_translated_message(mode, message, key))
    else:
        for key in range(1, MAX_KEY_SIZE + 1):
            print(key, get_translated_message("decrypt", message, key))


def get_mode():
    while True:
        print("Do you wish to encrypt or decrypt or brute-force a message?")
        mode = input().lower()
        if mode in ["encrypt", "e", "decrypt", "d", "brute", "b"]:
            return mode
        else:
            print("Enter either \"encrypt\" or \"e\" or \"decrypt\" or \"d\".")


def get_message():
    print("Enter your message:")
    return input()


def get_key():
    while True:
        print("Enter the key number (1-%s)" % MAX_KEY_SIZE)
        key = int(input())
        if 1 <= key <= MAX_KEY_SIZE:
            return key
    # Gets the number of characters the message will get shifted by


def get_translated_message(mode, message, key):
    if mode[0] == "d":
        key = -key
    translated = ""

    for symbol in message:
        symbol_index = SYMBOLS.find(symbol)
        if symbol_index == -1: 
            # Symbol not found in SYMBOLS.
            # Just add this symbol without any change.
            translated += symbol
        else:
            # Encrypt or decrypt.
            symbol_index += key

            if symbol_index >= len(SYMBOLS):
                symbol_index -= len(SYMBOLS)
            elif symbol_index < 0:
                symbol_index += len(SYMBOLS)

            translated += SYMBOLS[symbol_index]
    return translated


if __name__ == "__main__":
    main()
