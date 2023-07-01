def encrypt(key, text):
    text = text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in text:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def decrypt(key, text):
    text = text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in text:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

encrypt_decrypt = input("Do you want to (e)ncrypt or (d)ecrypt? ")

if encrypt_decrypt == "e":
    key = int(input("Please enter the key (0 to 25) to use: "))
    text = input("Enter the message to encrypt: ")
    print ("Cipher: " + encrypt(key,text))
elif encrypt_decrypt == "d":
    key = int(input("Please enter the key (0 to 25) to use: "))
    text = input("Enter the message to encrypt: ")
    print ("Decrypting: " + decrypt(key,text))