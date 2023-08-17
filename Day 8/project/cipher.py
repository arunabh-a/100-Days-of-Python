# Caesar Cipher: Day 8 Project
import ui

# print(ui.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def caesar(in_text, shift_amount, choice):
    result = ""
    listlen = len(ui.alphabet)
    alphinlet = ui.alphabet.index(letter)
    position = alphinlet + shift_amount
    for letter in in_text:
        if letter in ui.alphabet:
            
            if choice == "encode":
                position = alphinlet + shift_amount
                # To avoid Index Overflow
                if position > listlen - 1:
                    position %= listlen
            elif choice == "decode":
                position = alphinlet - shift_amount
                # To avoid Index Overflow
                if position > listlen - 1:
                    position %= listlen
            result += ui.alphabet[position]
        else:
            result += ui.alphabet[position]

    print(f"The {choice}d text: {result}\n\n")
caesar(in_text = text, shift_amount = shift, choice =  direction)