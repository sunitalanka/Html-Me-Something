from helpers import alphabet_position, rotate_character
def encrypt(text,key):
     in_msg = text
     msg = list(in_msg)
     en_key = list(key)
     new_str = ""
     k = 0
     k_c = 0
     for char in msg:
        if char.isalpha():
           k_c = en_key[k]
        new_str += rotate_character(char, alphabet_position(k_c))
        if char.isalpha():
           k += 1
           if k == len(key):
             k = 0
    
     return (new_str)

def main():
    from sys import argv,exit
    if len(argv) == 2  and  argv[1].isalpha():
       en_text = input("Type a Message:")
       enc_k = str(argv[1])
       print(encrypt(en_text,enc_k))
    else:    
       print("usage: python vigenere.py keyword")
       print("Arguments: The string to be used as a key to encrypt your message.") 
       print("Should only contain alphabetic characters no numbers or special characters.")
       exit()  
    

            
if __name__=="__main__":
    main()     