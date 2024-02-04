import random

def main()
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        # Return the board.
        theBoard = [" "] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print("The " + turn + " will go first.")
        gameIsPlaying = True
    
        while gameIsPlaying:
            if turn == "player":
                # Players turn
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
    
                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print("Hooray! You have won the game!")
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print("The game is a tie!")
                        break
                    else:
                        turn = "computer"
            else:
                # Computer's turn
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
    
                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print("The computer has beaten you! You lose.")
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print("The game is a tie!")
                        break
                    else:
                        turn = "player"
        print("Do you want to play again? (yes or no)")
        if not input().lower().startswith("y"):
            break

def drawBoard(b):
    # This function prints out the board that was passed

    # Board is a list of 10 strings (b) representing the board (ignoring 0)

    print(b[7] + "|" + b[8] + "|" + b[9])
    print("-+-+-")
    print(b[4] + "|" + b[5] + "|" + b[6])
    print("-+-+-")
    print(b[1] + "|" + b[2] + "|" + b[3])

def inputPlayerLetter():
    # Lets the player choose their letter.
    # Returns a list with the player's letter as the first item and the computer's letter as the second.
    
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()
    #The first element is player, the second is the computer
    if letter == "X":
        return["X","O"]
    else:
        return["O","X"]
    
def whoGoesFirst():
    # Randomly choose which player goes first.
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "player"

def makeMove(b, letter, move):
    b[move] = letter

def isWinner(b,l):
    # Given a board(b) and a players letter(l), this function returns True if that player has won.

    return ((b[7] == l and b[8] == l and b[9] == l) or # Across the top
            (b[4] == l and b[5] == l and b[6] == l) or # Across the middle
            (b[1] == l and b[2] == l and b[3] == l) or # Across the bottom
            (b[7] == l and b[4] == l and b[1] == l) or # Down the left side
            (b[8] == l and b[5] == l and b[2] == l) or # Down the middle
            (b[9] == l and b[6] == l and b[3] == l) or # Down the right side
            (b[7] == l and b[5] == l and b[3] == l) or # Diagonal
            (b[9] == l and b[5] == l and b[1] == l)) # Diagonal

def getboardC(b):
    # Make a copy of the board list and returns it.
    boardC = []
    for i in b:
        boardC.append(i)
    return boardC

def isSpaceFree(b, move):
    # Return True if space is free.
    return b[move] == " "

def getPlayerMove(b):
    # Lets the player move.
    move = " "
    while move not in " 1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(b, int(move)):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)

def chooseRandomMoveFromList(b, moveList):
    # Returns a valid move from the passed list on the passed board.
    # Returns none if no valid move.
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(b, i):
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(b,computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"
    
    # Here is the algorithm for our Tic-Tac-Toe AI:
    # Checks if it can win in the next move.
    for i in range(1,10):
        boardC = getboardC(b)
        if isSpaceFree(boardC, i):
            makeMove(boardC, computerLetter, i)
            if isWinner(boardC, computerLetter):
                return i
    
    # Checks if player is about to win on their next move and blocks them.
    for i in range(1,10):
        boardC = getboardC(b)
        if isSpaceFree(boardC, i):
            makeMove(boardC, playerLetter, i)
            if isWinner(boardC, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(b, [1,3,7,9])
    if move != None:
        return move
    
    # Try to take the center, if it is free.
    if isSpaceFree(b, 5):
        return 5
    
    # Move on one of the sides.
    return chooseRandomMoveFromList(b, [2,4,6,8])

def isBoardFull(b):
    # Returns True if every space on the board has been taken. Otherwise, returns false.
    for i in range(1,10):
        if isSpaceFree(b, i):
            return False
    return True

if __name__ == "__main__":
    main()
