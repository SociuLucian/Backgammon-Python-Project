import pygame
import sys

pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Backgammon")

# Load the backgammon board image
board_image = pygame.image.load("backgammon_board.jpg") 
board_image = pygame.transform.scale(board_image, (width, height))

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def draw_board():
    screen.blit(board_image, (0, 0))

def draw_pieces():

    pass

def handle_click(pos):
    # Convert mouse coordinates to board coordinates
    col = pos[0] * len(board[0]) // width
    row = pos[1] * len(board) // height

    # Check if the click is within the bounds of the board
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        #----------------------------------------------------------------
        print(f"Clicked on row {row}, column {col}")
    else:
        print("Clicked outside of the board")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(pygame.mouse.get_pos())

    screen.fill((255, 255, 255)) 
    draw_board()
    draw_pieces()

    pygame.display.flip()
    pygame.time.Clock().tick(60)