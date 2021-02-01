import random

class Snake:
    DIR_RIGHT = "R"
    DIR_LEFT = "L"
    DIR_UP = "U"
    DIR_DOWN = "D"

    def __init__(self, gameboard_size):
        self.x = 1
        self.y = 1
        self.x_food = 0
        self.y_food = 0


        self.length = 1
        self.coord_list = [(self.x, self.y)]
        self.direction = self.DIR_RIGHT
        self.gameboard_size = gameboard_size

        self.new_food()

    def get_coord_list(self):
        return self.coord_list

    def get_food_x_y(self):
        return [(self.x_food, self.y_food)]

    def increase_length(self):
        self.length = self.length + 1

    def calculate_new_x_y(self):
        x = self.x
        y = self.y
        direction = self.direction

        if direction == self.DIR_RIGHT:
            x = (x + 1) % (self.gameboard_size)
            if x == 0:
                x = 1
        elif direction == self.DIR_LEFT:
            x = x - 1
            if x == 0:
                x = self.gameboard_size - 1
        elif direction == self.DIR_DOWN:
            y = (y + 1) % (self.gameboard_size)
            if y == 0:
                y = 1
        elif direction == self.DIR_UP:
            y = y - 1
            if y == 0:
                y = self.gameboard_size - 1

        if (x, y) == (self.x_food, self.y_food):
            self.increase_length()
            self.new_food()

        if (x, y) in self.coord_list: # GAME OVER
            return False

        self.x = x
        self.y = y
        self.coord_list.insert(0, (x, y))
        if len(self.coord_list) > self.length:
            self.coord_list.pop()
        return True

    def new_food(self):
        success = False
        while success==False:
            x = random.randint(1, self.gameboard_size - 1)
            y = random.randint(1, self.gameboard_size - 1)
            if not (x, y) in self.coord_list:
                self.x_food = x
                self.y_food = y
                success = True

    def update(self, direction):
        if direction:
            self.direction = direction

        return self.calculate_new_x_y()
