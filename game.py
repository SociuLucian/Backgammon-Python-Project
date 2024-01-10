import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Backgammon")

# Load the backgammon board image
board_image = pygame.image.load("backgammon_board.jpg")  # Replace with your image file
board_image = pygame.transform.scale(board_image, (width, height))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Button properties
button_width, button_height = 250, 50 
button_margin = 20

# Font and text properties
font = pygame.font.Font(None, 36)
text_color = BLACK


def draw_board():
    screen.blit(board_image, (0, 0))

def draw_initial_pieces(board):
    piece_radius = 15
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                while board[i][j] !=0 :
                 pygame.draw.circle(screen, (255, 255, 255), (j * 40 + 20, i * 40 + 20), piece_radius)
                 board[i][j] -= 1
            elif board[i][j] < 0:
                while board[i][j] !=0 :
                 pygame.draw.circle(screen, (0, 0, 0), (j * 40 + 20, i * 40 + 20), piece_radius)
                 board[i][j] += 1


# Function to draw buttons
def draw_button(x, y, text, action, selected_button):
    button_rect = pygame.Rect(x, y, button_width, button_height)

    # Define colors
    button_color = (200, 200, 200)
    border_color = (0, 0, 0)
    text_color = (0, 0, 0)

    # Adjust colors based on hover or selected state
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        button_color = (220, 220, 220)
        border_color = (50, 50, 50)
        text_color = (50, 50, 50)

    if action == selected_button:
        button_color = (150, 150, 150)
        border_color = (0, 0, 0)
        text_color = (0, 0, 0)

    pygame.draw.rect(screen, button_color, button_rect)
    pygame.draw.rect(screen, border_color, button_rect, 2)

    # Add text to the button
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect

# Main menu loop
def main_menu():
    selected_option = None
    player_vs_computer_button = None
    player_vs_player_button = None

    while True:
        screen.fill(WHITE)

        player_vs_computer_button = draw_button((width - button_width) / 2, height / 2 - button_height - button_margin, "Player vs Computer", "player_vs_computer", selected_option)
        player_vs_player_button = draw_button((width - button_width) / 2, height / 2 + button_margin, "Player vs Player", "player_vs_player", selected_option)
        quit_button = draw_button((width - button_width) / 2, height / 2 + 2 * (button_height + button_margin), "Quit", "quit", selected_option)
        rules_button = draw_button((width - button_width) / 2, height / 2 + 3 * (button_height + button_margin), "Rules", "rules", selected_option)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if player_vs_computer_button.collidepoint(event.pos):
                    selected_option = "player_vs_computer"
                elif player_vs_player_button.collidepoint(event.pos):
                    selected_option = "player_vs_player"
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif rules_button.collidepoint(event.pos):
                    print("Show Rules")  # Add logic to show rules

        pygame.display.flip()
        pygame.time.Clock().tick(60)

        if selected_option:
            return selected_option
 
def handle_click(pos, board, board_image):
    # Get the dimensions of the board image
    board_width, board_height = board_image.get_size()

    # Define horizontal and vertical paddings
    horizontal_padding = 100  
    vertical_padding = 150 

    # Calculate the size of each point on the board
    point_width = (board_width - horizontal_padding) / len(board[0])
    point_height = (board_height - vertical_padding) / len(board)


    # Calculate the row and column based on the mouse position
    col = int((pos[0] -  horizontal_padding) / point_width)
    row = int((pos[1] -  vertical_padding) / point_height)

    # Check if the click is within the bounds of the board
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        # Implement your logic for handling the click on the board
        print(f"Clicked on row {row}, column {col}")
    else:
          print("Clicked outside of the board")

# Player vs Computer game loop
def player_vs_computer_game():
    print("Player vs Computer game")
    board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
    # Set up initial pieces
    board[0][5] = 2  # 2 white pieces on point 6 (0-based index)
    board[0][7] = 5  # 5 white pieces on point 8
    board[1][5] = -5  # 5 black pieces on point 6 (12th row is the bottom for black)
    board[1][7] = -2  # 2 black pieces on point 8

    while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(pygame.mouse.get_pos(),board,board_image)

     screen.fill((255, 255, 255))  
     draw_board()
     draw_initial_pieces(board)

     pygame.display.flip()
     pygame.time.Clock().tick(60)

    
# Player vs Player game loop
def player_vs_player_game():
    print("Player vs Player game")
    # Add your game logic here

# Main program loop
while True:
    selected_option = main_menu()

    if selected_option == "player_vs_computer":
        player_vs_computer_game()
    elif selected_option == "player_vs_player":
        player_vs_player_game()
