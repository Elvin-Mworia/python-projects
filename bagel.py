import random

NUM_DIGITS=3
MAX_GUESSES=10


def getSecretNum():
    
    numbers=list('0123456789')
    random.shuffle(numbers)# shuffling into random order
    secretNum=''
    for i in range(NUM_DIGITS):
        secretNum+=str(numbers[i])
    return secretNum

def getClues(guess,secretNum):
    '''Returns a string with the pico ,fermi,bagels clues for a guess and secret number pair'''
    if guess == secretNum:
        return 'You got it'
    clues=[]

    for i in range(len(guess)):
        if guess[i]==secretNum[i]:
         #a correct digit is in the incorrect place
          clues.append('Fermi')
        elif guess[i] in secretNum:
            #A correct digit is in the incorrect place
            clues.append('Pico')
    if len(clues)==0:
        return 'Bagels' #there is no correct digit at all
    else:
        clues.sort()
        return ' '.join(clues)
2

def main():
    print(f'''Bagel a deductive logic game by Elvin Mworia.8. I am thinking of a {NUM_DIGITS}th no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
   Pico         One digit is correct but in the wrong position.
   Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.''')

while True: #main game loop
    secretNum=getSecretNum() #generates the secret number the player needs to guess
    print("I have thought up a number.")
    print(f"You have {MAX_GUESSES} guesses to get it.")

    numGuesses=1
    while numGuesses<=MAX_GUESSES:
        guess=''
        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print(f"Guess {numGuesses}")
            guess=input('>')
        
        clues=getClues(guess,secretNum)
        print(clues)
        numGuesses+=1
        #if player is correct break out of the loop
        if guess==secretNum:
            break
        if numGuesses>MAX_GUESSES:
            print("You ran out of guesses.")
            print(f"The answer was {secretNum}")


    print('Do you want to play again? (yes or no)')
    if not input('> ').lower().startswith('y'):
        break
    print('Thanks for playing.')

if __name__=='__main__':
    main()

    
