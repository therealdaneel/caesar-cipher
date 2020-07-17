import re

def shift(message, amount):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    shifted_letter = ""
    for letter in message:
        if letter.upper() not in alphabet:
            shifted_letter += letter
            continue
        index = (alphabet.index(letter.upper()) + amount)%(len(alphabet))
        if amount > 0:
            try:
                shifted_letter += alphabet[index]
            except Exception as e:
                shifted_letter += letter
        elif amount < 0:
            shifted_letter += alphabet[index]
        else:
            print(message.lower())
            break
    return shifted_letter.lower()

text = input("input text: ")
shift_length = input("input shift amount: ")
if re.fullmatch(r"-?\d+", shift_length):
    pass
else:
    while not re.fullmatch(r"-?\d+", shift_length):
        print("invalid number given")
        shift_length = input("input shift amount: ")

print(shift(text, int(shift_length)))