# Caesar Cipher: Day 8 Project

def caesar(in_text, shift_amount, choice):
    result = ""
    listlen = len(ui.alphabet)
    for letter in in_text:
        if letter in ui.alphabet:
            alphinlet = ui.alphabet.index(letter) #CMOL
            position = alphinlet + shift_amount # CMOL
        
            
            if choice == "encode":
                position = alphinlet + shift_amount
            elif choice == "decode":
                position = alphinlet - shift_amount
            
            # To avoid Index Overflow
            if position > listlen - 1:
                position %= listlen
            result += ui.alphabet[position]
        else:
            result += letter

    print(f"The {choice}d text: {result}\n\n")

import ui

print(ui.logo)
while reinit == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    caesar(in_text = text, shift_amount = shift, choice =  direction)

    rest_req = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if rest_req == "no":
        reinit = False
        print("Utility Closed, Goodbye")
