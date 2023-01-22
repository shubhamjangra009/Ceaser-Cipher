from cipherart import *
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
while True:   
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26

    def cipher(text,shift,direction):
        cipher_text=""
        for char in text:
            if char in alphabet:
                letter_pos=alphabet.index(char)
                if direction=='encode':
                    new_letter_pos=letter_pos+shift-26
                elif direction=='decode':
                    new_letter_pos=letter_pos-shift
                else:
                    print('Wrong direction input, Try again')
                    break
                new_letter=alphabet[new_letter_pos]
            else:
                new_letter=char
            cipher_text+=new_letter
        if direction=='encode' or direction=='decode':
            print(f'your {direction}d text is {cipher_text}')
         
    cipher(text,shift,direction)
        
    repeat=input("wanna repeat, type 'yes' or 'no': ").lower()
    if repeat=='yes':
        continue 
    else:
        exit() #or use quit()
        
    