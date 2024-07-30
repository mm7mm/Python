import string
def info(masseg ,key):
    alphabet=string.ascii_lowercase
    encrypted_word=""
    for i in masseg:
        if i.lower() in alphabet:
            original_position=alphabet.index(i.lower())
            new_position=(original_position +key) %26
            encrypted_word += alphabet[new_position]
            if i.isupper():
                encrypted_letter=encrypted_letter.upper()
            encrypted_word+=encrypted_letter
        else:
            encrypted_word+=i
    print(encrypted_word)

word=input("Please type a word ").lower()
key_you=int(input("Enter your key: "))
info(word,key_you)