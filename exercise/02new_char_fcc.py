text = "We need to be more secure!"
shift = -3
alphabet = "abcdefghijklmnopqrstuvwxyz"

encrypted_text = ''

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text = alphabet[new_index]
    print("character:", char, "encrypted text:", encrypted_text)
