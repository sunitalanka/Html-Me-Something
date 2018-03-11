def alphabet_position(letter):
      
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
     
      letter = letter.lower()

      n_place = alphabet.find(letter)         
           
      return n_place

def rotate_character(char,rot):
   
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_char = ''

    if char.isalpha():
       if char in alphabet:
	       new_rot = alphabet_position(char) + rot
	       if new_rot < 26:
	     	  new_char += alphabet[new_rot]
	       else:
	          new_char += alphabet[new_rot % 26]
       elif char in alphabet.upper():
	       new_rot = alphabet_position(char) + rot
	       if new_rot < 26:
	     	  new_char += alphabet[new_rot].upper()
	       else:
	          new_char += alphabet[new_rot % 26].upper()
       return new_char
    else:
	    return char