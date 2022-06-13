
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
board_width = 800
board_height = 800



class Board:
    def __init__(self):
        self.board = [[white, black, white, black, white, black, white, black ],
                      [black, white, black, white, black, white, black, white ],
                      [white, black, white, black, white, black, white, black ],
                      [black, white, black, white, black, white, black, white],
                      [white, black, white, black, white, black, white, black ],
                      [black, white, black, white, black, white, black, white],
                      [white, black, white, black, white, black, white, black],
                      [black, white, black, white, black, white, black, white]]
