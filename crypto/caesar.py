from helpers import alphabet_position, rotate_character

def encrypt(text, rotation):
       te_xt = list(text)
       new_str = ''
       for ch_ar in te_xt:
       	    n_char = rotate_character(ch_ar,rotation)
            new_str += n_char
       return new_str

def main():
     from sys import argv,exit
     if argv[1].isdigit():
        en_text = input("Type your Message: ") 
        rot_number = int(argv[1])
        print(encrypt(en_text,rot_number))
     else:
         print("usage: python caeser.py n")
         print("Arguments:The integer to be used as Rotation number to Encrypt your message.")
         print("Should only contain integer numbers No string characters and special characters")  
         exit()            
     


if __name__=="__main__":
   main()     







