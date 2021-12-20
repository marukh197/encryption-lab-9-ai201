def encrypt(STRING,SHIFT):
    ENCRYPTION = ""
    # LOOP TO TRAVERSE THE TEXT 
    for i in range(len(STRING)):
        char = STRING[i]
        # CONDITION TO ENCRYPT UPPERCASE LETTERS 
        if (char.isupper()):
            ENCRYPTION += chr((ord(char) + SHIFT-65) % 26 + 65)
       # CONDITION TO ENCRYPT LOWERCASE LETTERS
        else:
            ENCRYPTION += chr((ord(char) + SHIFT - 97) % 26 + 97)
    return ENCRYPTION
# function to decrypt the text
def decrypt(STRING,SHIFT):
    DECRYPTION = ""
    # LOOP TO TRAVERSE THE TEXT 
    for i in range(len(STRING)):
        char = STRING[i]
        # CONDITION TO ENCRYPT UPPERCASE LETTERS 
        if (char.isupper()):
            DECRYPTION += chr((ord(char) - SHIFT-65) % 26 + 65)
       # CONDITION TO ENCRYPT LOWERCASE LETTERS
        else:
            DECRYPTION += chr((ord(char) - SHIFT -97) % 26 + 97)
    return DECRYPTION

print("    --------  ENCRYPTION  ---------")
print()
text =str(input("ENTER THE STRING TO ENCRYPT ")) 
shift=int(input("ENETR THE LENGTH OF SHIFT   "))
print()
print( "TEXT TO BE ENCRYPTED  : " + text)
print ("SHIFT                 : " + str(shift))
print ("TEXT AFTER ENCRYPTION : " + encrypt(text,shift))
print()
print("    --------  DECRYPTION  ---------")
print()
text1 =str(input("ENTER THE STRING TO DECRYPT ")) 
print()
print( "TEXT TO BE DECRYPTED  : " + text1)
print ("SHIFT                 : " + str(shift))
print ("TEXT AFTER DECRYPTION : " + decrypt(text1,shift))
