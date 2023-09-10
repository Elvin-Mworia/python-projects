try:
    import pyperclip
except ImportError:
    print("Install pyperclip module using pip")
    pass


LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('''The Vigenère cipher is a polyalphabetic substitution cipher that was
  powerful enough to remain unbroken for centuries.''')
    
    #let the user specify if they are encrypting or decrypting
    while True:
        response=input('Do you want to (e) encrypt or (d) decrypt?').strip().lower()
        if response.startswith('e'):
            mode='encrypt'
            break
        elif response.startswith('d'):
            mode='decrypt'
            break
        print('Please enter the letter d or e.')

    while True:#let the user specify the key to use
        response=input('''Please the specify the key to use.It can be a word or any combination of letters >''').upper()
        if response.isalpha():
            myKey=response
            break

    #let the user specify the message to encrypt/decrypt
    myMessage=input(f'enter the message to {mode}>')

    if mode=='encrypt':
        translated=encryptMessage(myMessage,myKey)
    elif mode=='decrypt':
        translated=decryptMessage(myMessage,myKey)
    
    print(f'{mode.title()} \n {translated}')

    try:
        pyperclip.copy(translated)
        print(f'Full {mode}ed text copied to clipboard')
    except:
        print("Install pyperclip to copy translated text to clipboard.")

def encryptMessage(message,key):
    '''Encrypt the message using the key'''
    return translateMessage(message,key,'encrypt')

def decryptMessage(message,key):
    '''Decrypt the message using the key'''
    return translateMessage(message,key,'decrypt')
    

def translateMessage(message,key,mode):
    #encrypt or decrypt the message using the key
    translated=[] #stores the encrypted/decrypted message

    keyIndex=0
    key=key.upper()

    for symbol in message: #loop through each character in message
        num=LETTERS.find(symbol.upper())
        if num !=-1:#-1 means symbol.upper() was not in LETTERS
            if mode == 'encrypt':
                # Add if encrypting:
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                # Subtract if decrypting:
                num -= LETTERS.find(key[keyIndex]) 
            
            num %=len(LETTERS) #Handle the potential wrap-around

            #add the encrypted/decrypted symbol to be translated
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex +=1 #move to the next letter in the key
            if keyIndex==len(key):
                keyIndex=0

        else:
            #just add the symbol without encrypting/decrypting
            translated.append(symbol)

    return ''.join(translated)
                
if __name__=='__main__':
    main()
