import random
import time

#--BOARD PARENT CLASS

class Board:
    def __init__(self,board):
        self.board = board

    def drawBoard(board):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print(' 7   | 8   | 9   ')
        print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
        print('     |     |     ')
        print('------------------')

        print(' 4   | 5   | 6   ')
        print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
        print('     |     |     ')
        print('------------------')

        print(' 1   | 2   | 3   ')
        print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
        print('     |     |    ')

    def inputPlayerLetter(self):
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            letter = str(input(self.playerOneName + ', do you want to be X or O?').upper())

        # the first element in the tuple is the player's letter, the second is the second player's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def isBoardFull(board):
        for i in range(1, 10):
            if Player.isSpaceFree(board, i):
                return False
        return True

    
#--PLAYER SUBCLASS    
    
class Player(Board):
    def __init__(self, board, playerOneName, playerTwoName):
        super().__init__(board)
        self.playerOneName = playerOneName
        self.playerTwoName = playerTwoName

    def whoGoesFirst():
        # Randomly chooses which player goes first (1 or 2).
        if random.randint(0, 1) == 0:
            return 'Player 1'
        else:
            return 'Player 2'

    def isWinner(bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

    def playAgain():
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you both want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(board, letter, move):
        board[int(move)] = letter

    def isSpaceFree(board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    
#--GET PLAYER MOVES

    def getPlayerMove(board):
        # Let player one type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not Player.isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def getSecondPlayerMove(board):

        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not Player.isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

#--BEGINNING


def main():
    print('Welcome to Tic Tac Toe!')
    playerOneName = input("What is player one's name: ")
    playerTwoName = input("What is player two's name: ")
    playerOneScore = 0
    playerTwoScore = 0
    board = 0
    a = Player(board,playerOneName,playerTwoName)

    while True:
    # Reset the board
        theBoard = [' '] * 10
        playerOneLetter, playerTwoLetter = a.inputPlayerLetter()
        turn = Player.whoGoesFirst()
        print(turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
#--PLAYER ONE'S TURN
            if turn == 'Player 1':
                print('\nIt\'s ' + playerOneName + '\'s turn...')
                move = Player.getPlayerMove(theBoard)
                Player.makeMove(theBoard, playerOneLetter, move)
                Board.drawBoard(theBoard)

                if Player.isWinner(theBoard, playerOneLetter):
                    print('Hooray! ' + playerOneName + ' is the winner!')
                    playerOneScore += 1
                    print('''Player One score:''' + str(playerOneScore) + ''' 
Player Two score:''' + str(playerTwoScore))
                    gameIsPlaying = False
                else:
                    if Board.isBoardFull(theBoard):
                        Board.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 2'
            else:
#--PLAYER TWO'S TURN
                print('\nIt\'s ' + playerTwoName + '\'s turn...')
                move = Player.getSecondPlayerMove(theBoard)
                Player.makeMove(theBoard, playerTwoLetter, move)
                Player.drawBoard(theBoard)

                if Player.isWinner(theBoard, playerTwoLetter):
                    Board.drawBoard(theBoard)
                    print('Hooray! ' + playerTwoName + ' is the winner!')
                    playerTwoScore += 1
                    print('''Player One score:''' + str(playerOneScore) + '''
Player Two score:''' + str(playerTwoScore))
                    gameIsPlaying = False
                else:
                    if Board.isBoardFull(theBoard):
                        Board.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 1'

        if not Player.playAgain():
            break

main ()
