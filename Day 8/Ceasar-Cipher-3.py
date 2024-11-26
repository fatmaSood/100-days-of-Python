alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def ceasar(plain_text, shift_amount):
    if direction == "encode":
        new_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            new_text += alphabet[new_position]
        print(f"The encoded text is {new_text}")

    elif direction == "decode":
        new_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            new_text += alphabet[new_position]
        print(f"The decoded text is {new_text}")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
ceasar(plain_text=text, shift_amount=shift)
