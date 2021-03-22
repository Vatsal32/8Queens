import pygame
from main import Board

pygame.init()
white, black, button = (255, 255, 255), (0, 0, 0), (47, 17, 32)
queen = pygame.image.load('white_queen.png')
size = 87
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 28)
text = font.render('Next', True, white)
textRect = text.get_rect()
textRect.center = (184, 762)
text1 = font.render('Previous', True, white)
textRect1 = text1.get_rect()
textRect1.center = (532, 762)


def update(board, queenIcon):
    gameDisplay = pygame.display.set_mode((716, 816), 0, 0)
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

    next = pygame.Rect(97, 736, 174, 50)
    prev = pygame.Rect(445, 736, 174, 50)
    pygame.draw.rect(gameDisplay, button, next)
    pygame.draw.rect(gameDisplay, button, prev)

    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                gameDisplay.blit(queenIcon, (i * size + 10, j * size + 10))
    gameDisplay.blit(text, textRect)
    gameDisplay.blit(text1, textRect1)
    # gameDisplay = gameDisplay
    pygame.display.update()


gameDisplay = pygame.display.set_mode((716, 816), 0, 0)

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
pygame.draw.rect(gameDisplay, button, next)
pygame.draw.rect(gameDisplay, button, prev)
gameDisplay.blit(text, textRect)
gameDisplay.blit(text1, textRect1)
pygame.display.update()

if __name__ == '__main__':
    board = Board()
    board.place_queen(0)
    solutions = board.boards
    solution = 0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if next.collidepoint(pos):
                    if solution < 91:
                        solution += 1
                if prev.collidepoint(pos):
                    if solution > -1:
                        solution -= 1
            if event.type == pygame.QUIT:
                gameExit = True
            update(solutions[solution])
            pygame.display.update()
        clock.tick(60)
