#before start to play the game run this commands in order
#1) python3 -m venv venv
#2) pip3 install replit
from replit import clear
from logo import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, direction_cipher):
    cipher_text = ''
    for position in range(len(plain_text)):
        letter = plain_text[position]
        
        #this if statement is necessary as "non-letter" filter
        if letter in alphabet:
            cipher_letter_position = alphabet.index(letter)
            #handling the shift_amount dividing it by one to do not allow the user to enter a value > len(alphabet)
            if shift_amount > 26:
                shift_amount = shift_amount % 1 == 0
                #encoding and decoding logic 
            if direction_cipher == 'encode':
                cipher_letter = alphabet[cipher_letter_position + shift_amount]
            elif direction_cipher == 'decode':
                cipher_letter = alphabet[cipher_letter_position - shift_amount]
            cipher_text += cipher_letter
        else:
            cipher_text += letter

    if direction_cipher == 'encode':
        print(f"The encrypted text is {cipher_text}")
    elif direction_cipher == 'decode':
        print(f"The decrypted text is {cipher_text}")

#initializing the string to reset the program
reset_program = ''

#while clicle necessary to decide if continue to play
while not reset_program == 'no':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    clear()

    #handling the direction input to start the game
    while not direction == 'encode' and not direction == 'decode':
        print("You've entered an invalid value. Please try again")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    #conditional block where the user decides to encode or decode the cipher message
    if direction == 'encode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(plain_text=text, shift_amount=shift, direction_cipher='encode')
    elif direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(plain_text=text, shift_amount=shift, direction_cipher='decode')
    
    reset_program = input("Do you want restart the cipher program?\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if reset_program == 'no':
        print("Goodbye!")
