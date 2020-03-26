# Edit: This is NOT COMPLETE, just messing around with pygame seeing what I can do.
#       It will be completed eventually if I get back into pygame


import pygame
import random

pygame.init()

display_width = 497
display_height = 499

black = (0, 0, 0)
white = (255, 255, 255)

block_width = 108
block_height = 106

places = [[(13, 14), (133, 14), (255, 14), (375, 15)],
            [(13, 135), (133, 134), (255, 137), (375, 139)],
            [(13, 257), (133, 254), (255, 254), (375, 254)],
            [(13, 377), (133, 374), (255, 374), (375, 374)]]

# maybe accomplish in a loop eventually
board = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]



gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('2048 game')

clock = pygame.time.Clock()

def draw_rectangle(color, number, placex, placey):
    font = pygame.font.SysFont(None, 20)
    text = font.render(number, True, white)
    pygame.draw.rect(gameDisplay, color, [placex, placey, 106, 106])
    gameDisplay.blit(text, ((placex + (block_width / 2)), (placey + (block_height / 2))))

def draw_board():
    grid = pygame.image.load('grid.png')
    gameDisplay.blit(grid, (0, 0))

def start_game():
    # Starting block to make 2
    placey = random.randint(0, 3)
    placex = random.randint(0, 3)

    # Starting block to make 2
    placey2 = random.randint(0, 3)
    placex2 = random.randint(0, 3)

    if placey2 != placey or placex2 != placex:
        board[placex][placey] = 2
        board[placex2][placey2] = 2
    else:
        start_game()

def go_left():
    change = False

    for y in range(0, 4):
        for x in range(3, 0, -1):
            if board[y][x] != 0:
                if board[y][x - 1] == 0:
                    board[y][x - 1] = board[y][x]
                    change = True
                elif board[y][x - 1] == board[y][x]:
                    board[y][x - 1] = board[y][x] ** 2
                    change = True
                    break
                else:
                    continue
                board[y][x] = 0
    # if change:
    #     make_random()

def go_right():
    change = False

    for y in range(0, 4):
        for x in range(2, 0, -1):
            if board[y][x] != 0:
                if board[y][x + 1] == 0:
                    board[y][x + 1] = board[y][x]
                    change = True
                elif board[y][x + 1] == board[y][x]:
                    board[y][x + 1] = board[y][x] ** 2
                    change = True
                    break
                else:
                    continue
                board[y][x] = 0

    if change:
        make_random()

def go_up():
    change = False

    for y in range(3, 0, -1):
        for x in range(0, 4):
            if board[y][x] != 0:
                if board[y - 1][x] == 0:
                    board[y - 1][x] = board[y][x]
                    change = True
                elif board[y - 1][x] == board[y][x]:
                    change = True
                    board[y - 1][x] = board[y][x] ** 2
                    break
                else:
                    continue
                board[y][x] = 0
    # if change:
    #     make_random()

def go_down():
    change = False

    for y in range(0, 3):
        for x in range(0, 4):
            if board[y][x] != 0:
                if board[y + 1][x] == 0:
                    board[y + 1][x] = board[y][x]
                    change = True
                elif board[y + 1][x] == board[y][x]:
                    change = True
                    board[y + 1][x] = board[y][x] ** 2
                    break
                else:
                    continue
                board[y][x] = 0

    # if change:
    #     make_random()

def make_random():


    placey = random.randint(0, 3)
    placex = random.randint(0, 3)

    if board[placey][placex] == 0:
        board[placey][placex] = 2
    else:
        make_random()

def game_loop():
    gameExit = False

    start_game()
    # print(board)
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # Logic to see if we can go left
                    go_left()
                elif event.key == pygame.K_RIGHT:
                    go_right()
                    # print(board)
                elif event.key == pygame.K_UP:
                    go_up()
                elif event.key == pygame.K_DOWN:
                    go_down()


        draw_board()

        for y in range(0, 4):
            for x in range(0, 4):
                if board[y][x] != 0:
                    draw_rectangle(black, str(board[y][x]), places[y][x][0], places[y][x][1])
                    # print(board)
        # draw_rectangle(black, str(12), places[placey][placex][0], places[placey][placex][1])

        # print(board)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
