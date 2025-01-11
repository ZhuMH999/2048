import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

class View:
    def __init__(self, model, win):
        self.model = model
        self.win = win

    def draw(self):
        self.win.fill((100, 100, 100))

class Model:
    def __init__(self):
        self.x = 4
        self.y = 4
        self.board = [[0] * self.x for _ in range(self.y)]

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

            self.view.draw()

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    c = Controller()
    c.run()