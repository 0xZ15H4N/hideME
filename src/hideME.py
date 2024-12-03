#all imports
import time
from art import *
import random
import requests
import json

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
    print("[*] 4. To hide data in Utf-8")
    print("[*] 5. To hide data in Latin-1")
    print("[*] 7. To hide Your Own ciphered Text")
    print("[*] 8. To hide data in To quit!" )

def genrate_random_text(size):
    url = "https://random-word-api.herokuapp.com/word"
    r = requests.get(url,params={
            "number" : f"{size}"
        })
    return r






if __name__ == "__main__":
    welcome()
    options()
    ipt = int(input("Enter the Choice"))
    file = input("Enter the file name in which you want to hide  [hidden text]")
    hidden_text = input("Enter the hidden text")
    print(genrate_random_text(10).text) # words will be there!
    #f = open(file,'a+')
    #if(f.read() 
    #match(ipt):
    #    case(1):
            
            
        