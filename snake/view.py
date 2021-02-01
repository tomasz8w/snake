

class View():

    def __init__(self, board_size):
        self.board_size = board_size
        self.snake_char = "o"
        self.food_char = "x"

    def set_board_size(self, d):
        self.board_size = d

    def update_gameboard(self, coords, food):
        line = ""
        for i in range(self.board_size):
            for j in range(self.board_size):
                if (j, i) in coords:
                    line = line + self.snake_char
                elif (j, i) in food:
                    line = line + self.food_char
                elif i == 0 or i == (self.board_size - 1):
                    line = line + "_"
                elif j == 0 or j == (self.board_size - 1):
                    line = line + "|"
                else:
                    line = line + " "
            print(line)
            line = ""
