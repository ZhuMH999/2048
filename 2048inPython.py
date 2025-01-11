import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

FONT = pygame.font.SysFont('Times New Roman', 30)

class View:
    def __init__(self, model, win):
        self.model = model
        self.win = win

    def draw(self):
        self.win.fill((100, 100, 100))
        for i in range(self.model.y):
            for j in range(self.model.x):
                if self.model.board[i][j] != 0:
                    self.get_text_widget_and_center((0, 0, 0), j*50+25, i*50+25, FONT, str(self.model.board[i][j]))

    def get_text_widget_and_center(self, rgb, c_x, c_y, font, text):
        widget = font.render(text, True, rgb)
        rect = widget.get_rect()
        rect.center = (c_x, c_y)
        self.win.blit(widget, rect)

class Model:
    def __init__(self):
        self.x = 4
        self.y = 4
        self.board = [[0] * self.x for _ in range(self.y)]
        self.board[3][0] = 2
        self.board[3][3] = 2
        self.move_right()

    def move_left(self):
        for i in range(self.y):
            for j in range(self.x-1):
                if self.board[i][j+1] != 0:
                    done = False
                    temp = 1
                    while not done:
                        if j+temp == 0:
                            done = True
                        elif self.board[i][j+temp-1] == 0 or self.board[i][j+temp-1] == self.board[i][j+temp]:
                            if self.board[i][j+temp-1] == 0:
                                self.board[i][j+temp-1] = self.board[i][j+temp]
                            elif self.board[i][j+temp-1] == self.board[i][j+temp]:
                                self.board[i][j+temp-1] *= 2
                            self.board[i][j+temp] = 0
                            temp -= 1
                        else:
                            done = True

    def move_right(self):
        for i in range(self.y):
            for j in range(self.x-1):
                done = False
                while not done:
                    if self.board[i][self.x-1-j] == 0 or self.board[i][self.x-j] == self.board[i][self.x-1-j]:
                        if self.board[i][self.x-1-j] == 0:
                            self.board[i][self.x-1-j]

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

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.model.move_left()

            self.view.draw()

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    c = Controller()
    c.run()