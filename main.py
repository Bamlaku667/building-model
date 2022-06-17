import random

import pygame as pg
from OpenGL.GL import *




class Checkers:
    def __init__(self):
        self.width = 800  # board width
        self.height = 800  # board height
        self.cols = 8
        self.rows = 8
        self.cell_size = self.width // self.cols
        self.clock = pg.time.Clock()
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height), pg.OPENGL | pg.DOUBLEBUF)
        glClearColor(0.1, 0.2, 0.2, 1)  # initialize openGl
        self.main()

    def main(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()

            self.clock.tick(60)           # for constant frame rating



        pg.quit()

players = ['x', 'o']
turn = random.randrange(2)
print(turn)
print("%s's turn" % players[turn ])



