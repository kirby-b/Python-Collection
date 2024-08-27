import random

player_score = 0
computer_score = 0
ties = 0

try:
    def main():
        print("Welcome to Tic-Tac-Toe!")

        while True:
            # Return the board.
            the_board = [" "] * 10
            player_letter, computer_letter = input_player_letter()
            turn = who_goes_first()
            print("The " + turn + " will go first.")
            game_is_playing = True

            while game_is_playing:
                if turn == "player":
                    # Players turn
                    draw_board(the_board)
                    move = get_player_move(the_board)
                    make_move(the_board, player_letter, move)

                    if is_winner(the_board, player_letter):
                        draw_board(the_board)
                        print("Hooray! You have won the game!")
                        keep_score("p")
                        game_is_playing = False
                    else:
                        if is_board_full(the_board):
                            draw_board(the_board)
                            print("The game is a tie!")
                            keep_score("t")
                            break
                        else:
                            turn = "computer"
                else:
                    # Computer's turn
                    move = get_computer_move(the_board, computer_letter)
                    make_move(the_board, computer_letter, move)

                    if is_winner(the_board, computer_letter):
                        draw_board(the_board)
                        print("The computer has beaten you! You lose.")
                        keep_score("c")
                        game_is_playing = False
                    else:
                        if is_board_full(the_board):
                            draw_board(the_board)
                            print("The game is a tie!")
                            keep_score("t")
                            break
                        else:
                            turn = "player"


    def draw_board(b):
        # This function prints out the board that was passed

        # Board is a list of 10 strings (b) representing the board (ignoring 0)

        print(b[7] + "|" + b[8] + "|" + b[9])
        print("-+-+-")
        print(b[4] + "|" + b[5] + "|" + b[6])
        print("-+-+-")
        print(b[1] + "|" + b[2] + "|" + b[3])


    def input_player_letter():
        # Lets the player choose their letter.
        # Returns a list with the player's letter as the first item and the computer's letter as the second.

        letter = ""
        while not (letter == "X" or letter == "O"):
            print("Do you want to be X or O?")
            letter = input().upper()
        # The first element is player, the second is the computer
        if letter == "X":
            return ["X", "O"]
        else:
            return ["O", "X"]


    def who_goes_first():
        # Randomly choose which player goes first.
        if random.randint(0, 1) == 0:
            return "computer"
        else:
            return "player"


    def make_move(b, letter, move):
        b[move] = letter


    def is_winner(b, le):
        # Given a board(b) and a players letter(le), this function returns True if that player has won.

        return ((b[7] == le and b[8] == le and b[9] == le) or  # Across the top
                (b[4] == le and b[5] == le and b[6] == le) or  # Across the middle
                (b[1] == le and b[2] == le and b[3] == le) or  # Across the bottom
                (b[7] == le and b[4] == le and b[1] == le) or  # Down the left side
                (b[8] == le and b[5] == le and b[2] == le) or  # Down the middle
                (b[9] == le and b[6] == le and b[3] == le) or  # Down the right side
                (b[7] == le and b[5] == le and b[3] == le) or  # Diagonal
                (b[9] == le and b[5] == le and b[1] == le))  # Diagonal


    def get_board_copy(b):
        # Make a copy of the board list and returns it.
        board_copy = []
        for i in b:
            board_copy.append(i)
        return board_copy


    def is_space_free(b, move):
        # Return True if space is free.
        return b[move] == " "


    def get_player_move(b):
        # Lets the player move.
        move = " "
        while move not in " 1 2 3 4 5 6 7 8 9".split() or not is_space_free(b, int(move)):
            print("What is your next move? (1-9)")
            move = input()
        return int(move)


    def choose_random_move_from_list(b, move_list):
        # Returns a valid move from the passed list on the passed board.
        # Returns none if no valid move.
        possible_moves = []
        for i in move_list:
            if is_space_free(b, i):
                possible_moves.append(i)

        if len(possible_moves) != 0:
            return random.choice(possible_moves)
        else:
            return None


    def get_computer_move(b, computer_letter):
        # Given a board and the computer's letter, determine where to move and return that move.
        if computer_letter == "X":
            player_letter = "O"
        else:
            player_letter = "X"

        # Here is the algorithm for our Tic-Tac-Toe AI:
        # Checks if it can win in the next move.
        for i in range(1, 10):
            board_copy = get_board_copy(b)
            if is_space_free(board_copy, i):
                make_move(board_copy, computer_letter, i)
                if is_winner(board_copy, computer_letter):
                    return i

        # Checks if player is about to win on their next move and blocks them.
        for i in range(1, 10):
            board_copy = get_board_copy(b)
            if is_space_free(board_copy, i):
                make_move(board_copy, player_letter, i)
                if is_winner(board_copy, player_letter):
                    return i

        # Try to take one of the corners, if they are free.
        move = choose_random_move_from_list(b, [1, 3, 7, 9])
        if move is not None:
            return move

        # Try to take the center, if it is free.
        if is_space_free(b, 5):
            return 5

        # Move on one of the sides.
        return choose_random_move_from_list(b, [2, 4, 6, 8])


    def is_board_full(b):
        # Returns True if every space on the board has been taken. Otherwise, returns false.
        for i in range(1, 10):
            if is_space_free(b, i):
                return False
        return True


    def keep_score(winner):
        global player_score
        global computer_score
        global ties
        if winner == "p":
            player_score += 1
        elif winner == "c":
            computer_score += 1
        elif winner == "t":
            ties += 1
        else:
            pass
        # Calculates the new scores

        print(f"Player Score:{player_score}\nComputer Score:{computer_score}\nTies:{ties}")
        # Prints current scores


    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    print("Thank you for playing. Here is your final score:")
    keep_score("donttrustyoutuberswhodontshowproof")
