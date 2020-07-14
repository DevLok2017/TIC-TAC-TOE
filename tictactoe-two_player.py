import os

os.system('cls')  # to clear cmd screen, use 'clear' if 'cls doesn't work


class Board:
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]  # initialize the empty board

    def display(self):
        print(" {} | {} | {} ".format(self.cells[1], self.cells[2], self.cells[3]) + " \t{} | {} | {} ".format(1, 2, 3))
        print(" --------- " + " \t--------- ")
        print(" {} | {} | {} ".format(self.cells[4], self.cells[5], self.cells[6]) + " \t{} | {} | {} ".format(4, 5, 6))
        print(" --------- " + " \t--------- ")
        print(" {} | {} | {} ".format(self.cells[7], self.cells[8], self.cells[9]) + " \t{} | {} | {} ".format(7, 8, 9))

    def update_cell(self, cell_no, player):     # update the board with player
        while(True):
            if cell_no<1 or cell_no>9:      # check if move is acceptable
                cell_no = int(input("\n Player O) Wrong Choice \n Please choose between < 1 - 9 >: "))
                
            elif board.cells[cell_no] != ' ':       # check if move is available
                cell_no = int(input("\n Player O) Wrong Choice {} is already occupied".format(cell_no) + 
                                    "\n Please choose another between < 1 - 9 >: "))
                
            else:
                break    
                
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self, player):       # check for winner, in the possible 8 combinations
        for combo in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False       # if board is not in any above combination, return false, game carries on
            if result:
                return True
        return False

    def is_tie(self):       # check for tie
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells >= 9:
            return True       # if all cells are used up, return true
        else:
            return False

    def reset(self):       # resets the board to initial position, for new game
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


if __name__ == '__main__':
    board = Board()       # object of Board class is created

    def print_header():
        print("\n WELCOME TO TIC-TAC-TOE \n\n")

    def refresh_screen():       # clears the screen for next player's input
        # clear screen
        os.system('cls')
        # print header
        print_header()
        # show the board
        board.display()


    while True:

        refresh_screen()

        # get input from 'O'
        o_choice = int(input("\n Player O) Choose between < 1 - 9 >: "))

        # update board
        board.update_cell(o_choice, "O")
        # check for O's win
        if board.is_winner("O"):
            refresh_screen()
            print("\n 'O' WINS!! \n")
            play_again = input(" Would you like to play again( Y / N ): ").upper()       # if player want to continue
            if play_again == 'Y':
                board.reset()       # reset to initial position
                continue
            else:
                break
        # check for tie
        if board.is_tie():
            refresh_screen()
            print("\n TIE!! \n")
            play_again = input(" Would you like to play again( Y / N ): ").upper()       # if player want to continue
            if play_again == 'Y':
                board.reset()       # reset to initial position
                continue
            else:
                break


        refresh_screen()
        # get X input
        x_choice = int(input("\n Player X) Choose between < 1 - 9 >: "))
        
        # update board
        board.update_cell(x_choice, "X")
        # check for X's win
        if board.is_winner("X"):
            refresh_screen()
            print("\n 'X' WINS!! \n")
            play_again = input(" Would you like to play again( Y / N ): ").upper()       # if player want to continue
            if play_again == 'Y':
                board.reset()       # reset to initial position
                continue
            else:
                break
        # check for tie
        if board.is_tie():
            refresh_screen()
            print("\n TIE!! \n")
            play_again = input(" Would you like to play again( Y / N ): ").upper()       # if player want to continue
            if play_again == 'Y':
                board.reset()       # reset to initial position
                continue
            else:
                break
