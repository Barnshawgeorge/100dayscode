alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

test = "Hello world"
new = ""
shift = 2

for i in test.lower():
    if(i == " "):
        new += " "
    else:
        get_alph_index = alphabet.index(i) + shift
        new += alphabet[get_alph_index]
    
print(new) 


def shift_letter(index, shift):
    new_index = (index + shift) % len(alphabet)  # Modulo to wrap around
    return alphabet[new_index]

    
    if(direction == "encode"):
        print(f"Here is the encoded result: {encrypt(text, shift)}")
    if(direction == "decrypt"):
        print(f"Here is the decoded result: {decrypt(text, shift)}")
