print("\nWelcome to Ceaser Cipher")

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'a', 'b', 'c', 'd', 'e', 'f',
             'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


def ceaser(message, shift_amt, cipher_mode):
    cipher_text = ""
    for letter in message:
        position = alphabets.index(letter)
        if cipher_mode == "encode":
            new_position = position + shift_amt
            new_letter = alphabets[new_position]
            cipher_text += new_letter

        elif cipher_mode == "decode":
            new_position = position - shift_amt
            new_letter = alphabets[new_position]
            cipher_text += new_letter

    if cipher_mode == "encode":
        print(f"The encrypted text is {cipher_text}.")
    elif cipher_mode == "decode":
        print(f"The decrypted text is {cipher_text}.")


end = True
while end:

    mode = input("\nType 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    msg = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    ceaser(message=msg, shift_amt=shift, cipher_mode=mode)

    again = input("\nType 'yes' to go again or type 'no' to end:\n").lower()

    if again == "no":
        end = False
        print("\nThanks for using Ceaser's cipher. Goodbye!")
