from snake import view, snake
from snake.view import View
from snake.snake import Snake
import time
import msvcrt, os


def main():
    board_size = 15
    v = View(board_size)
    s = Snake(board_size)

    key_mapping = {
        'H': s.DIR_UP,
        'M': s.DIR_RIGHT,
        'P': s.DIR_DOWN,
        'K': s.DIR_LEFT
    }

    clear = lambda: os.system('cls')
    clear()

    while True:
        if msvcrt.kbhit():
            msvcrt.getch() # skip 0xe0
            key = msvcrt.getch().decode('utf-8')
            if key in key_mapping:
                if not s.update(key_mapping[key]):
                    return
        else:
            if not s.update(None):
                return
        #print(s.get_food_x_y())
        #print(s.get_coord_list())

        v.update_gameboard(s.get_coord_list(), s.get_food_x_y())
        time.sleep(0.1)
        clear = lambda : os.system('cls')
        clear()


if __name__ == "__main__":
    main()