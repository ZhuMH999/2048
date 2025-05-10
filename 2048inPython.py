import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600

TILE_SIZE = 50
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

FONT = pygame.font.SysFont('Times New Roman', 25)
MENU_FONT = pygame.font.SysFont('Times New Roman', 20)

class View:
    def __init__(self, model, win):
        self.model = model
        self.win = win

    def draw(self):
        self.win.fill((100, 100, 100))
        x, y = pygame.mouse.get_pos()
        if self.model.x is not None:
            for i in range(self.model.y):
                for j in range(self.model.x):
                    if i == self.model.new_y and j == self.model.new_x:
                        pygame.draw.rect(self.win, (255, 0, 0), (j * (TILE_SIZE + TILE_GAP) + 10, i * (TILE_SIZE + TILE_GAP) + 10, TILE_SIZE, TILE_SIZE))
                    elif self.model.board[i][j] > 2048:
                        pygame.draw.rect(self.win, (187, 165, 61), (j*(TILE_SIZE+TILE_GAP)+10, i*(TILE_SIZE+TILE_GAP)+10, TILE_SIZE, TILE_SIZE))
                        pygame.draw.rect(self.win, TILE_COLORS[4096], (j*(TILE_SIZE+TILE_GAP)+15, i*(TILE_SIZE+TILE_GAP)+15, TILE_SIZE-10, TILE_SIZE-10))
                    else:
                        pygame.draw.rect(self.win, TILE_COLORS[self.model.board[i][j]], (j*(TILE_SIZE+TILE_GAP)+10, i*(TILE_SIZE+TILE_GAP)+10, TILE_SIZE, TILE_SIZE))

                    if self.model.board[i][j] != 0:
                        if self.model.board[i][j] > 2048:
                            self.get_text_widget_and_center((187, 165, 61), j * (TILE_SIZE + TILE_GAP) + 10 + TILE_SIZE/2, i * (TILE_SIZE + TILE_GAP) + 10 + TILE_SIZE/2, FONT, str(self.model.board[i][j]))
                        else:
                            self.get_text_widget_and_center((0, 0, 0), j * (TILE_SIZE + TILE_GAP) + 10 + TILE_SIZE/2, i * (TILE_SIZE + TILE_GAP) + 10 + TILE_SIZE/2, FONT, str(self.model.board[i][j]))

            self.get_text_widget_and_center((0, 0, 0), self.model.x / 2 * (TILE_SIZE + TILE_GAP) + 10, self.model.y * (TILE_SIZE + TILE_GAP) + 10 + TILE_SIZE/2, FONT, 'Score: ' + str(self.model.score))
            if self.model.x > 4:
                self.get_text_widget_and_center((0, 0, 0), self.model.x * (TILE_SIZE + TILE_GAP) + 100, 10 + TILE_SIZE/2, MENU_FONT, 'Auto Move')

                if self.model.x * (TILE_SIZE + TILE_GAP) + 30 < x < self.model.x * (TILE_SIZE + TILE_GAP) + 50 and TILE_SIZE/2 < y < TILE_SIZE/2 + 20 and not self.model.end:
                    pygame.draw.rect(self.win, (120, 120, 120), (self.model.x * (TILE_SIZE + TILE_GAP) + 30, TILE_SIZE / 2, 20, 20))
                else:
                    if self.model.auto_move:
                        pygame.draw.rect(self.win, (118, 150, 86), (self.model.x * (TILE_SIZE + TILE_GAP) + 30, TILE_SIZE/2, 20, 20))
                    else:
                        pygame.draw.rect(self.win, (70, 70, 70), (self.model.x * (TILE_SIZE + TILE_GAP) + 30, TILE_SIZE / 2, 20, 20))

            if self.model.x * (TILE_SIZE + TILE_GAP) + 30 < x < self.model.x * (TILE_SIZE + TILE_GAP) + 130 and TILE_SIZE / 2 + 30 < y < TILE_SIZE / 2 + 70 and not self.model.end:
                pygame.draw.rect(self.win, (120, 120, 120), (self.model.x * (TILE_SIZE + TILE_GAP) + 30, TILE_SIZE / 2 + 30, 100, 40), border_radius=4)
            else:
                pygame.draw.rect(self.win, (70, 70, 70), (self.model.x * (TILE_SIZE + TILE_GAP) + 30, TILE_SIZE / 2 + 30, 100, 40), border_radius=4)

            self.get_text_widget_and_center((200, 200, 200), self.model.x * (TILE_SIZE + TILE_GAP) + 80, TILE_SIZE / 2 + 50, MENU_FONT, 'Home')

            if self.model.end:
                pygame.draw.rect(self.win, (90, 90, 90), (250, 195, 300, 190), border_radius=4)
                pygame.draw.rect(self.win, (238, 238, 210), (255, 200, 290, 180), border_radius=4)
                self.get_text_widget_and_center((118, 150, 86), 400, 230, MENU_FONT, 'Game Over!')
                self.get_text_widget_and_center((118, 150, 86), 400, 250, MENU_FONT, 'Your score was: ' + str(self.model.score))

                pygame.draw.rect(self.win, (100, 100, 100), (345, 335, 110, 40), border_radius=4)
                if 345 < x < 455 and 335 < y < 375:
                    pygame.draw.rect(self.win, (170, 170, 170), (350, 340, 100, 30), border_radius=4)

                self.get_text_widget_and_center((238, 238, 210), 400, 355, MENU_FONT, 'Quit Game')

        else:
            pygame.draw.rect(self.win, (80, 80, 80), (280, 175, 240, 250), border_radius=4)
            pygame.draw.rect(self.win, (238, 238, 210), (285, 180, 230, 240), border_radius=4)
            self.get_text_widget_and_center((118, 150, 86), 400, 200, MENU_FONT, 'Play a game?')
            for i in range(3):
                pygame.draw.rect(self.win, (100, 100, 100), (295, 220 + i * 60, 210, 50), border_radius=4)
                if 295 < x < 505 and 220 + i * 60 < y < 270 + i * 60:
                    pygame.draw.rect(self.win, (170, 170, 170), (300, 225 + i * 60, 200, 40), border_radius=4)
                self.get_text_widget_and_center((238, 238, 210), 400, 245 + i * 60, MENU_FONT, str((i+1)*2+2) + 'x' + str((i+1)*2+2) + ' board')

    def get_text_widget_and_center(self, rgb, c_x, c_y, font, text):
        widget = font.render(text, True, rgb)
        rect = widget.get_rect()
        rect.center = (c_x, c_y)
        self.win.blit(widget, rect)

class Model:
    def __init__(self):
        self.x = None
        self.y = None
        self.new_x = None
        self.new_y = None
        self.board = []
        self.score = 0
        self.end = False
        self.run = True
        self.auto_move = False

    def move(self, direction, check=False):
        # delta, y range, x range, i index, x index, move_cond, new_pos, current_pos
        directions = [[-1, range(self.y), range(self.x-1), lambda i, j: i, lambda i, j: j+1, lambda i, j, temp: j+temp > 0, lambda i, j, temp: (i, j+temp-1), lambda i, j, temp: (i, j+temp)],  # move left
                      [1, range(self.y), range(self.x-2, -1, -1), lambda i, j: i, lambda i, j: j, lambda i, j, temp: j+temp < self.x, lambda i, j, temp: (i, j+temp), lambda i, j, temp: (i, j+temp-1)],  # move right
                      [-1, range(self.y-1), range(self.x), lambda i, j: i+1, lambda i, j: j, lambda i, j, temp: i+temp > 0, lambda i, j, temp: (i+temp-1, j), lambda i, j, temp: (i+temp, j)],  # move up
                      [1, range(self.y-2, -1, -1), range(self.x), lambda i, j: i, lambda i, j: j, lambda i, j, temp: i+temp < self.y, lambda i, j, temp: (i+temp, j), lambda i, j, temp: (i+temp-1, j)]]  # move down
        
        params = directions[direction]
        has_moved = False
        for i in params[1]:  # range of y
            for j in params[2]:  # range of x
                i_index = params[3](i, j)  # i
                j_index = params[4](i, j)  # j

                if self.board[i_index][j_index] != 0:
                    done = False
                    has_merged = False
                    temp = 1

                    while not done:
                        new_i, new_j = params[6](i, j, temp)
                        current_i, current_j = params[7](i, j, temp)

                        if not params[5](i, j, temp):
                            done = True
                        elif (self.board[new_i][new_j] == 0 or (self.board[new_i][new_j] == self.board[current_i][current_j] and not has_merged)) and ((not has_moved and check) or not check):
                            if self.board[new_i][new_j] == 0:
                                if not check:
                                    self.board[new_i][new_j] = self.board[current_i][current_j]
                            elif self.board[new_i][new_j] == self.board[current_i][current_j]:
                                if not check:
                                    self.board[new_i][new_j] *= 2
                                    self.score += self.board[new_i][new_j]
                                has_merged = True
                            if not check:
                                self.board[current_i][current_j] = 0
                            has_moved = True
                            temp += params[0]
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
            self.new_x, self.new_y = random.randint(0, self.x-1), random.randint(0, self.y-1)
            if self.board[self.new_y][self.new_x] == 0:
                done = True
                if random.randint(1, 10) == 10:
                    self.board[self.new_y][self.new_x] = 4
                else:
                    self.board[self.new_y][self.new_x] = 2

    def check_for_end(self):
        if not self.move(0, True) and not self.move(1, True) and not self.move(2, True) and not self.move(3, True):
            return True
        else:
            return False

    def check_for_click_pos(self, x, y):
        if self.x is None:
            done = False
            if 295 < x < 505:
                if 220 < y < 270:
                    self.x = self.y = 4
                    done = True
                elif 280 < y < 330:
                    self.x = self.y = 6
                    done = True
                elif 340 < y < 390:
                    self.x = self.y = 8
                    done = True
            if done:
                self.board = [[0] * self.x for _ in range(self.y)]
                self.spawn_new_num()
        else:
            if not self.end:
                if self.x * (TILE_SIZE + TILE_GAP) + 30 < x < self.x * (TILE_SIZE + TILE_GAP) + 50 and TILE_SIZE / 2 < y < TILE_SIZE / 2 + 20:
                    if self.auto_move:
                        self.auto_move = False
                    else:
                        self.auto_move = True
                elif self.x * (TILE_SIZE + TILE_GAP) + 30 < x < self.x * (TILE_SIZE + TILE_GAP) + 130 and TILE_SIZE / 2 + 30 < y < TILE_SIZE / 2 + 70:
                    self.x = None
            elif self.end:
                if 345 < x < 455 and 335 < y < 375:
                    self.run = False

class Controller:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.model = Model()
        self.view = View(self.model, self.win)

        pygame.display.set_caption('2048 in Python')

    def run(self):
        clock = pygame.time.Clock()

        while self.model.run:
            clock.tick(60)

            if self.model.auto_move:
                self.model.move(1)
                self.model.move(3)
                self.model.move(1)
                self.model.move(2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.model.run = False
                elif event.type == pygame.KEYDOWN and self.model.x is not None:
                    if event.key == pygame.K_LEFT:
                        self.model.move(0)
                    elif event.key == pygame.K_RIGHT:
                        self.model.move(1)
                    elif event.key == pygame.K_UP:
                        self.model.move(2)
                    elif event.key == pygame.K_DOWN:
                        self.model.move(3)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        self.model.check_for_click_pos(x, y)

            self.view.draw()

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    c = Controller()
    c.run()