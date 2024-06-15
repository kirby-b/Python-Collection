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


def get_mode(mode):
    m = mode.lower()
    if m in ["encrypt", "e", "decrypt", "d", "brute", "b"]:
        return m
    else:
        return "invalid"


def get_message():
    print("Enter your message:")
    return input()


def get_key(key):
    if 1 <= int(key) <= MAX_KEY_SIZE:
        return key
    else:
        return 0
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
