from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run = True

def encrypt(original_text, shift_amount):
        cipher_text = ""
        for i in original_text.lower():
            if(i not in alphabet):
                cipher_text += i
            else:
                get_alph_index = alphabet.index(i) + shift_amount
                cipher_text += alphabet[get_alph_index]
        return cipher_text

def decrypt(encrypted_text, shift_amount):
        decrypt_text = ""
        for i in encrypted_text.lower():
            if(i not in alphabet):
                decrypt_text += i
            else:
                get_alph_index = alphabet.index(i) - shift_amount
                decrypt_text += alphabet[get_alph_index]
        return decrypt_text

print(logo)

while(run):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if(direction == "encode"):
        print(f"Here is the encoded result: {encrypt(text, shift)}\n")
    if(direction == "decode"):
        print(f"Here is the decoded result: {decrypt(text, shift)}\n")

    again = input("Type 'yes if you want to go again or 'no' to stop ").lower()
    if(again == "no"):
        run = False



        
