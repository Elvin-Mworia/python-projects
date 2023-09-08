#A classic two player board game
ALL_SPACES=[str(x) for x in range(1,10)]

X,O,BLANK= 'X','0','' #constants for string value


def getBlankBoard():
    ''' create a new blank tictactoe board'''
    board={}
    for space in ALL_SPACES:
        board[space]=BLANK #all spaces start as blank
    return board

def getBoardStr(board):
    '''return a text-representation of the board'''
    return '''
        {}|{}|{}  1 2 3
        -+-+-
        {}|{}|{}  4 5 6
        -+-+-
        {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'],
                            board['4'], board['5'], board['6'],
                            board['7'], board['8'], board['9'])


def isValidSpace(board,space):
    #returns true if the space on the board is validnspace number and is blank

    return space in ALL_SPACES and board[space]==BLANK

def isWinner(board,player):
    #returns true if the player is winner in the current game

    b,p=board,player

        # Check for 3 marks across 3 rows, 3 columns, and 2 diagonals
    return ((b['1'] == b['2'] == b['3'] == p) or  # Across top
            (b['4'] == b['5'] == b['6'] == p) or  # Across middle
            (b['7'] == b['8'] == b['9'] == p) or  # Across bottom
            (b['1'] == b['4'] == b['7'] == p) or  # Down left
            (b['2'] == b['5'] == b['8'] == p) or  # Down middle
            (b['3'] == b['6'] == b['9'] == p) or  # Down right
            (b['3'] == b['5'] == b['7'] == p) or  # Diagonal
            (b['1'] == b['5'] == b['9'] == p))    # Diagonal

def isBoardFull(board):
    #returns true if every space in the board has been taken
    for space in ALL_SPACES:
        if board[space]==BLANK:
            return False
    return True

def updateBoard(board,space,mark):
    #sets the space on the board to mark
    board[space]=mark


def main():
    print('Welcome to Tic-Tac-Toe!')
    gameboard=getBlankBoard()# gets a blank TTT board dictioanary
    currentPlayer,nextPlayer=X,O

    while True:#main game loop
        print(getBoardStr(gameboard))

        #keep asking the player until they enter a number 1-9
        move=None
        while not isValidSpace(gameboard,move):
            print(f'What is {currentPlayer}\'s move?')
            move=input('> ')
            
        updateBoard(gameboard,move,currentPlayer)#make the move

        #check if the game is over
        if isWinner(gameboard,currentPlayer):
            print(getBoardStr(gameboard))
            print(f'{currentPlayer} has won the game!')
            break
        elif isBoardFull(gameboard):#check for tie
            print(getBoardStr(gameboard))
            print('The game is a tie!')
            break
        #switch to the next player
        currentPlayer,nextPlayer=nextPlayer,currentPlayer
    print('Thanks for playing!')

if (__name__=='__main__'):
    main()

