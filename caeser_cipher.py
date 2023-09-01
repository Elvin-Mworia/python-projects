try:
    import pyperclip
except ImportError:
    print("Install pyperclip module using pip")
    pass
'''Every possible symbol can be encrypted/decrypted 
You can add numbers and punctuation marks to encrypt those as well'''

SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print("Caesar Cipher encrypts letters by shifting them over by a \n key number.For example,a key of 2 means the letterA is \n encrypted into C,the letter B into D and so on.")
print("")

#let the user enter if they are encrypting or decrypting
while True:
    #keep asking until the user enters e or d
    print('Do you want to encrypt(e) or decrypt (d)?')
    response=input('> ').strip().lower()
    if response.startswith('e'):
        mode='encrypt'
        break
    elif response.startswith('d'):
        mode='decrypt'
        break
    print('Please enter the letter e or d.')

#let the user enter the key to use:
while True:
    #keep asking until the user enters a valid key.
    maxKey=len(SYMBOLS)-1
    print(f'Please enter the key (0 to {maxKey} to use. )')
    response=input('> ').strip().upper()
    if not response.isdecimal():
        continue

    if 0<=int(response)< len(SYMBOLS):
        key=int(response)
        break

#let the user enter the message to encrypt or decrypt
print(f'Enter the message to {mode}.')
message=input('> ').strip().upper() 

translated=''#stored the decrypted/encrypted form of the message

for symbol in message:
    if symbol in SYMBOLS:
        num=SYMBOLS.find(symbol) #returns the index of the symbol
        if mode == 'encrypt':
            num=num+key
        elif mode== 'decrypt':
            num=num-key
        #Handle the wrap-around if num is larger  than the length of SYMBOLS or less than 0
        if num>=len(SYMBOLS):
            num=num-len(SYMBOLS)
        elif num<0:
            num=num+len(SYMBOLS)

        #add encrypted or decrypted number's symbols to translated
        translated+=SYMBOLS[num]
    else:
            translated+=symbol 
print(translated)

try:
    pyperclip.copy(translated)
except:
    print("Install pyperclip to copy translated text to clipboard.")
