import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600


TILE_SIZE = 60
TILE_GAP = 10
TILE_COLORS = {0: (170, 170, 170),
               2: (237, 229, 218),
               4: (238, 225, 201),
               8: (243, 178, 122),
               16: (246, 150, 101),
               32: (247, 124, 95),
               64: (247, 95, 59),
               128: (237, 208, 115),
               256: (237, 204, 99),
               512: (236, 202, 80),
               1024: (220, 180, 60),
               2048: (200, 150, 30),
               4096: (10, 10, 10)}

FONT = pygame.font.SysFont('Arial', 25)

class View:
    def __init__(self, model, win):
        self.model = model
        self.win = win

    def draw(self):
        self.win.fill((100, 100, 100))
        for i in range(self.model.y):
            for j in range(self.model.x):
                if self.model.board[i][j] > 2048:
                    pygame.draw.rect(self.win, (187, 165, 61), (j*(TILE_SIZE+TILE_GAP)+10, i*(TILE_SIZE+TILE_GAP)+10, TILE_SIZE, TILE_SIZE))
                    pygame.draw.rect(self.win, TILE_COLORS[4096], (j*(TILE_SIZE+TILE_GAP)+15, i*(TILE_SIZE+TILE_GAP)+15, TILE_SIZE-10, TILE_SIZE-10))
                else:
                    pygame.draw.rect(self.win, TILE_COLORS[self.model.board[i][j]], (j*(TILE_SIZE+TILE_GAP)+10, i*(TILE_SIZE+TILE_GAP)+10, TILE_SIZE, TILE_SIZE))

                if self.model.board[i][j] != 0:
                    if self.model.board[i][j] > 2048:
                        self.get_text_widget_and_center((187, 165, 61), j * (TILE_SIZE + TILE_GAP) + 10 + TILE_SIZE/2, i * (TILE_SIZE + TILE_GAP) + 10 + TILE_SIZE/2, FONT, str(self.model.board[i][j]))
                    else:
                        self.get_text_widget_and_center((0, 0, 0), j * (TILE_SIZE + TILE_GAP) + 10 + TILE_SIZE/2, i * (TILE_SIZE + TILE_GAP) + 10 + TILE_SIZE/2, FONT, str(self.model.board[i][j]))

    def get_text_widget_and_center(self, rgb, c_x, c_y, font, text):
        widget = font.render(text, True, rgb)
        rect = widget.get_rect()
        rect.center = (c_x, c_y)
        self.win.blit(widget, rect)

class Model:
    def __init__(self):
        self.x = 8
        self.y = 8
        self.board = [[0] * self.x for _ in range(self.y)]
        self.end = False
        self.spawn_new_num()

    def move_left(self, check=False):
        has_moved = False
        for i in range(self.y):
            for j in range(self.x-1):
                if self.board[i][j+1] != 0:
                    done = False
                    has_merged = False
                    temp = 1
                    while not done:
                        if j+temp == 0:
                            done = True
                        elif (self.board[i][j+temp-1] == 0 or (self.board[i][j+temp-1] == self.board[i][j+temp] and not has_merged)) and ((not has_moved and check) or not check):
                            if self.board[i][j+temp-1] == 0:
                                if not check:
                                    self.board[i][j+temp-1] = self.board[i][j+temp]
                            elif self.board[i][j+temp-1] == self.board[i][j+temp]:
                                if not check:
                                    self.board[i][j+temp-1] *= 2
                                has_merged = True
                            if not check:
                                self.board[i][j+temp] = 0
                            has_moved = True
                            temp -= 1
                        else:
                            done = True
        if has_moved and not check:
            self.spawn_new_num()
            if self.check_for_end():
                self.end = True
        if check:
            return has_moved

    def move_right(self, check=False):
        has_moved = False
        for i in range(self.y):
            for j in range(self.x-2, -1, -1):
                if self.board[i][j] != 0:
                    done = False
                    has_merged = False
                    temp = 1
                    while not done:
                        if j+temp == self.x:
                            done = True
                        elif (self.board[i][j+temp] == 0 or (self.board[i][j+temp] == self.board[i][j+temp-1] and not has_merged)) and ((not has_moved and check) or not check):
                            if self.board[i][j+temp] == 0:
                                if not check:
                                    self.board[i][j+temp] = self.board[i][j+temp-1]
                            elif self.board[i][j+temp] == self.board[i][j+temp-1]:
                                if not check:
                                    self.board[i][j+temp] *= 2
                                has_merged = True
                            if not check:
                                self.board[i][j+temp-1] = 0
                            has_moved = True
                            temp += 1
                        else:
                            done = True
        if has_moved and not check:
            self.spawn_new_num()
            if self.check_for_end():
                self.end = True
        if check:
            return has_moved

    def move_up(self, check=False):
        has_moved = False
        for i in range(self.y-1):
            for j in range(self.x):
                if self.board[i+1][j] != 0:
                    done = False
                    has_merged = False
                    temp = 1
                    while not done:
                        if i+temp == 0:
                            done = True
                        elif (self.board[i+temp-1][j] == 0 or (self.board[i+temp-1][j] == self.board[i+temp][j] and not has_merged)) and ((not has_moved and check) or not check):
                            if self.board[i+temp-1][j] == 0:
                                if not check:
                                    self.board[i+temp-1][j] = self.board[i+temp][j]
                            elif self.board[i+temp-1][j] == self.board[i+temp][j]:
                                if not check:
                                    self.board[i+temp-1][j] *= 2
                                has_merged = True
                            if not check:
                                self.board[i+temp][j] = 0
                            has_moved = True
                            temp -= 1
                        else:
                            done = True
        if has_moved and not check:
            self.spawn_new_num()
            if self.check_for_end():
                self.end = True
        if check:
            return has_moved

    def move_down(self, check=False):
        has_moved = False
        for i in range(self.y-2, -1, -1):
            for j in range(self.x):
                if self.board[i][j] != 0:
                    done = False
                    has_merged = False
                    temp = 1
                    while not done:
                        if i+temp == self.y:
                            done = True
                        elif (self.board[i+temp][j] == 0 or (self.board[i+temp][j] == self.board[i+temp-1][j] and not has_merged)) and ((not has_moved and check) or not check):
                            if self.board[i+temp][j] == 0:
                                if not check:
                                    self.board[i+temp][j] = self.board[i+temp-1][j]
                            elif self.board[i+temp][j] == self.board[i+temp-1][j]:
                                if not check:
                                    self.board[i+temp][j] *= 2
                                has_merged = True
                            if not check:
                                self.board[i+temp-1][j] = 0
                            has_moved = True
                            temp += 1
                        else:
                            done = True
        if has_moved and not check:
            self.spawn_new_num()
            if self.check_for_end():
                self.end = True
        if check:
            return has_moved

    def spawn_new_num(self):
        done = False
        while not done:
            x, y = random.randint(0, self.x-1), random.randint(0, self.y-1)
            if self.board[y][x] == 0:
                done = True
                if random.randint(1, 10) == 10:
                    self.board[y][x] = 4
                else:
                    self.board[y][x] = 2

    def check_for_end(self):
        if not self.move_down(True) and not self.move_up(True) and not self.move_right(True) and not self.move_left(True):
            return True
        else:
            return False

class Controller:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.model = Model()
        self.view = View(self.model, self.win)

        pygame.display.set_caption('2048 in Python')

    def run(self):
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(60)

            self.model.move_up()
            self.model.move_right()
            self.model.move_down()
            self.model.move_right()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.model.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.model.move_right()
                    elif event.key == pygame.K_UP:
                        self.model.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.model.move_down()

            self.view.draw()

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    c = Controller()
    c.run()