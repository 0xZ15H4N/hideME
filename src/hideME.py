#all imports
from art import *
import random
from random_word import RandomWords
import base64
import secrets
# this seems usefull ;xD
#sequence [945, 489, 109, 976, 514, 605, 457, 535, 416, 676, 621, 964, 452, 818, 250, 958, 324, 874, 805, 141, 67, 734, 350, 62, 963, 405, 637, 906]
#sequence [680, 698, 491, 85, 923, 443, 737, 704, 19, 765, 646, 96, 944, 153]

#global variables
font = ["dancingfonts","defleppard","fire_font-s",'nancyj-fancy',"rammstein","standard","3d_diagonal","wetletter"] # i have pre-selected some of the font!

#all user defined functions
def welcome():
    welcome_message = '''          hideME'''
    tprint(welcome_message,font=font[random.randint(0,len(font)-1)])
    print("\t\t\tMaintained by : 0xZ15H4N (https://github.com/1337-pr05)")

def options():
    print("[*] 1. To hide data in clear text")
    print("[*] 2. To hide data in based64")
    print("[*] 3. To hide data in Ceasar Ciphered")
    print("[*] 4. To hide Your Own ciphered Text")

def genrate_random_text(size):
    r = RandomWords()
    # Generate N(size) random words
    random_words = " ".join([r.get_random_word() for _ in range(size)])
    
    return random_words

def encrypt(hidden_text,Mode):
    if(Mode == 1 or Mode == 4 ):
        return hidden_text
    #base64
    elif(Mode==2):
        return base64.b64encode(hidden_text.encode("utf-8")).decode("utf-8")
    #ceasar cipher
    elif(Mode == 3):
        rot = 13  # Rotation (shift) value
        cipher = ""
        for i in hidden_text:
            if i.isalpha():  # Only alphabetic characters
                shift_base = 65 if i.isupper() else 97
                             # Shift within the alphabet range
                cipher += chr((ord(i) - shift_base + rot) % 26 + shift_base)
            else:
                cipher += i  # Non-alphabetic characters remain unchanged

    return cipher

def generate_secure_random_numbers(n, start=10, end=1000):
    return [secrets.randbelow(end - start + 1) + start for _ in range(n)]

def HideME(file,cipher_text):
    sequence = generate_secure_random_numbers(len(cipher_text))
    dissemble = list(cipher_text)
    with open(file,"r+") as f:
        for i in range(len(cipher_text)):
            f.seek(sequence[i],0)
            f.write(str(dissemble[i]))    
    return sequence     
        
        
def unHideME(file,sequnce):
    cipher_text = ''
    try:
        with open(file,"r+") as f:
            for i in sequence:
                f.seek(i,0)
                cipher_text += f.read(1)
        return decrypt(cipher_text)
    except FileNotFoundError:
        print("[*] File Not Found!")

def decrypt(cipher_text):
    plain_text = []
    plain_text.append(cipher_text)
    #Decode Base64
    try:
        base64_decoded = base64.b64decode(cipher_text).decode("utf-8")
        plain_text.append(base64_decoded)
    except Exception as e:
        plain_text.append("None")
    
    rot = 13  # Rotation (shift) value
    cipher = ""
    for i in cipher_text:
        if i.isalpha():  # Only alphabetic characters
            shift_base = 65 if i.isupper() else 97
                             # Shift within the alphabet range
            cipher += chr((ord(i) - shift_base + rot) % 26 + shift_base)
        else:
            cipher += i  # Non-alphabetic characters remain unchanged
    plain_text.append(cipher)
    
    return plain_text

if __name__ == "__main__":
    welcome()
    ch = input("Encrypt or decrypt [E/e or D/d] : ")
    if(ch == "E" or ch == "e"):
        options()
        ipt = int(input("[*] Enter the Choice : "))
        file = input("[*] Enter the file name in which you want to hide [hidden text] : ")
        hidden_text = input("[*] Enter the hidden text : ")
        cipher_text  = encrypt(hidden_text,ipt) 
        with open(file,"w") as f:
            f.write(genrate_random_text(1500))
        sequence = HideME(file,cipher_text)
        print("[*] The following Text has been Successfully hidden inside the file : ",file)
        print("[*] Sequence to Extract the file is", sequence)
    
    if(ch == "D" or ch == "d"):
        file = input("[*] Enter the file name : ")
        sequence = eval(input("[*] Enter The Sequence inclosed in  [] : "))
        hidden_text = unHideME(file,sequence)
        print("[*] The hidden data Extracted from the file is : ",hidden_text[0])
        print("[*] Base64 decyphered : ",hidden_text[1])
        print("[*] Cesar Ciphered : ",hidden_text[2])
        
        
    
    
    
    

        