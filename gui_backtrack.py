import pygame
from gui import white, black, text, textRect, text1, textRect1, clock, size, queen

gameDisplay = pygame.display.set_mode((716, 716), 0, 0)
queen_red = pygame.image.load('red_queen.png')
queen_gre = pygame.image.load('green_queen.png')
delay = 150


def update(board, queenIcon):
    gameDisplay = pygame.display.set_mode((716, 716), 0, 0)
    gameDisplay.fill(white)

    cnt = 0
    for i in range(0, boardLength):
        for z in range(0, boardLength):
            # check if current loop value is even
            if cnt % 2 == 0:
                pygame.draw.rect(gameDisplay, white, [10 + size * z, 10 + size * i, size, size])
            else:
                pygame.draw.rect(gameDisplay, black, [10 + size * z, 10 + size * i, size, size])
            cnt += 1
        # since theres an even number of squares go back one value
        cnt -= 1
    # Add a nice boarder
    pygame.draw.rect(gameDisplay, black, [10, 10, boardLength * size, boardLength * size], 1)

    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                gameDisplay.blit(queenIcon, (i * size + 10, j * size + 10))
    gameDisplay.blit(text, textRect)
    gameDisplay.blit(text1, textRect1)
    # gameDisplay = gameDisplay
    pygame.display.update()


gameExit = False

# board length, must be even
boardLength = 8
gameDisplay.fill(white)

cnt = 0
for i in range(0, boardLength):
    for z in range(0, boardLength):
        # check if current loop value is even
        if cnt % 2 == 0:
            pygame.draw.rect(gameDisplay, white, [10 + size * z, 10 + size * i, size, size])
        else:
            pygame.draw.rect(gameDisplay, black, [10 + size * z, 10 + size * i, size, size])
        cnt += 1
    # since theres an even number of squares go back one value
    cnt -= 1
# Add a nice boarder
next = pygame.Rect(97, 736, 174, 50)
prev = pygame.Rect(445, 736, 174, 50)
pygame.draw.rect(gameDisplay, black, [10, 10, boardLength * size, boardLength * size], 1)
gameDisplay.blit(text, textRect)
gameDisplay.blit(text1, textRect1)
pygame.display.update()


class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x):
        self.x = x

    def unset(self):
        self.x = -1

    def show(self):
        print(self.x, self.y)

    def conflicts(self, queen2):
        x = self.x
        y = self.y
        p = queen2.x
        q = queen2.y

        if x == -1 or p == -1:
            return False
        elif x == p or y == q or (x - y) == (p - q) or (x + y) == (p + q):  # check if the queens threatens each other
            return True
        else:
            return False


class Board:
    count = 0
    queens = []
    boards = []
    board1 = []

    def __init__(self):
        for i in range(8):
            q = Queen(-1, i)
            self.queens.append(q)

    def is_safe(self):
        for i in range(8):
            for j in range(8):
                if i != j:
                    if self.queens[i].conflicts(self.queens[j]):
                        return False

        return True

    def print_board(self):
        queens = []
        for queen in self.queens:
            queens.append(queen.x)
        self.boards.append(self.board1)

    def place_queen(self, y):
        if y >= 8:
            self.count += 1
            self.get_board()
            self.print_board()
            update(self.board1, queen_gre)
            pygame.time.delay(5000)
            return False

        for i in range(8):
            self.queens[y].set(i)
            self.get_board()
            update(self.board1, queen)
            pygame.time.delay(delay)
            if self.is_safe() and self.place_queen(y + 1):
                gameDisplay.blit(queen_gre, (self.queens[y].x * size + 10, self.queens[y].y * size + 10))
                pygame.display.update()
                pygame.time.delay(750)
                gameDisplay.blit(queen, (self.queens[y].x * size + 10, self.queens[y].y * size + 10))
                pygame.display.update()
                return True
            else:
                self.queens[y].unset()
                self.get_board()
                update(self.board1, queen)
                pygame.time.delay(delay)

        return False

    def get_board(self):
        self.board1 = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]]
        for queen in self.queens:
            self.board1[queen.x][queen.y] = 1


if __name__ == '__main__':
    board = Board()
    while not gameExit:
        board.place_queen(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            pygame.display.update()
        clock.tick(60)
