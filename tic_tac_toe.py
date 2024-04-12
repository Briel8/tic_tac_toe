class tic_tac_toe:
    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.board_positions = [1, 2, 3, 4, 5, 6,7, 8, 9]
        self.symbol = 'X'
        self.winner = ""

    def check_winner(self):
        if self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X': # diagonal left to right
            self.winner = "player one"
            return self.winner
        elif self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X': # diagonal ringt to left
            self.winner = "player one"
            return self.winner
        elif self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X': # first column
            self.winner = "player one"
            return self.winner
        elif self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X': # second column
            self.winner = "player one"
            return self.winner
        if self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X': # third column
            self.winner = "player one"
            return self.winner
        elif self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2] == 'X': # first row
            self.winner = "player one"
            return self.winner
        elif self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2] == 'X': # second row
            self.winner = "player one"
            return self.winner
        elif self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2] == 'X': # second row
            self.winner = "player one"
            return self.winner
        
        # Player two wins When
        if self.board[0][0] == '0' and self.board[1][1] == '0' and self.board[2][2] == '0': # diagonal left to right
            self.winner = "player two"
            return self.winner
        elif self.board[0][2] == '0' and self.board[1][1] == '0' and self.board[2][0] == '0': # diagonal ringt to left
            self.winner = "player two"
            return self.winner
        elif self.board[0][0] == '0' and self.board[1][0] == '0' and self.board[2][0] == '0': # first column
            self.winner = "player two"
            return self.winner
        elif self.board[0][1] == '0' and self.board[1][1] == '0' and self.board[2][1] == '0': # second column
            self.winner = "player two"
            return self.winner
        if self.board[0][2] == '0' and self.board[1][2] == '0' and self.board[2][2] == '0': # third column
            self.winner = "player two"
            return self.winner
        elif self.board[0][0] == '0' and self.board[0][1] == '0' and self.board[0][2] == '0': # first row
            self.winner = "player two"
            return self.winner
        elif self.board[1][0] == '0' and self.board[1][1] == '0' and self.board[1][2] == '0': # second row
            self.winner = "player two"
            return self.winner
        elif self.board[2][0] == '0' and self.board[2][1] == '0' and self.board[2][2] == '0': # second row
            self.winner = "player two"
            return self.winner

    def turn(self):
        if self.symbol == 'X':
            self.symbol = '0'
        else:
            self.symbol = 'X'

# display the score board
    def display_board(self):
        for i in range(0, len(self.board)):
            print("\n+---+---+---+")
            print("|", end="")
            for j in range(0, len(self.board[i])):
                print("", self.board[i][j], end=" |")
        print("\n+---+---+---+")

    # ask the x player where to put the x on the board
    def fill_board(self):
        """Enter the position"""
        position = int(input("Enter the position:\n"))
        if position < 10 and position >0:
            # look at where the position is in the board.
            for i in range(0, len(self.board)):
                for j in range(0, len(self.board[i])):
                    if self.board[i][j] == position:
                        self.board[i][j] = self.symbol
            self.turn()
        else:
            print("Invalid option try again")
    
    def play(self):
        count = 1
        while count <= 9:
            self.display_board()
            self.fill_board()
            if count >= 2:
                self.check_winner()
                if self.winner == "player one" or self.winner == "player two":
                    self.display_board()
                    print(f"Congratulations {self.winner}!")
                    break
            count += 1 
        

# Driver code
game = tic_tac_toe()
game.play()