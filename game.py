import random
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Backgammon")

# Load the backgammon board image
board_image = pygame.image.load("Images/backgammon_board.jpg")  
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

dice_buff =0

def draw_board():
    screen.blit(board_image, (0, 0))
def draw_initial_dice():
    piece_x = 50 + 10 * 54 # identation + row * board cell size 
    piece_y = 10 
    dice_image = pygame.image.load("Images/you_dice_6.png")
    screen.blit(dice_image, (piece_x, piece_y))
    piece_x += dice_image.get_height()
    screen.blit(dice_image, (piece_x, piece_y))  

def draw_initial_pieces(board):
    cell_size = 54
    for i in range(len(board)):
        for j in range(len(board[i])):
            piece_image1 = None
            # Calculate the position based on the board size and cell size
            if board[i][j] != 0:
             if i==0 :
              piece_x = 45 + j * cell_size
              piece_y = 75 + i * cell_size
              buff = board[i][j]
              while buff!=0:
               if buff < 0 :
                piece_image1 = pygame.image.load("Images/black_piece.png")
                piece_image1 = pygame.transform.scale(piece_image1, (cell_size, cell_size))
                screen.blit(piece_image1, (piece_x, piece_y))
                piece_y += cell_size
                buff+=1
               else: 
                 piece_image1 = pygame.image.load("Images/white_piece.png")
                 piece_image1 = pygame.transform.scale(piece_image1, (cell_size, cell_size))
                 screen.blit(piece_image1, (piece_x, piece_y))
                 piece_y += cell_size
                 buff-=1
             elif i==1:
                 piece_x = 45 + j * cell_size
                 piece_y = 610 + i * cell_size
                 buff = board[i][j]
                 while buff!=0:
                  if buff < 0 :
                   piece_image1 = pygame.image.load("Images/black_piece.png")
                   piece_image1 = pygame.transform.scale(piece_image1, (cell_size, cell_size))
                   screen.blit(piece_image1, (piece_x, piece_y))
                   piece_y -= cell_size
                   buff+=1
                  else: 
                   piece_image1 = pygame.image.load("Images/white_piece.png")
                   piece_image1 = pygame.transform.scale(piece_image1, (cell_size, cell_size))
                   screen.blit(piece_image1, (piece_x, piece_y))
                   piece_y -= cell_size
                   buff-=1
                          
# Function to draw buttons
def draw_button(x, y, text, action, selected_button):
    button_rect = pygame.Rect(x, y, button_width, button_height)

    # Defining colors
    button_color = (200, 200, 200)
    border_color = (0, 0, 0)
    text_color = (0, 0, 0)

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

def get_board_pos(pos,board,screen_width,screen_height):
    # Define horizontal padding (adjust as needed)
    padding_downside = 80
    padding_rightside = 50

    # Calculate the cell size dynamically based on the size of the board
    cell_width = (screen_width - padding_downside * 2) / len(board)
    cell_height = (screen_height - padding_rightside * 2) / len(board[0])

    # Calculate the row and column based on the mouse position
    col = int((pos[1] - 75) / cell_width)
    row = int((pos[0] - 45) / cell_height)

    return col,row,cell_width,cell_height
   
def handle_click(pos, board, board_image,turn,switch,dice_roll,on_table):
    # Get the dimensions of the board image
    screen_height, screen_width = board_image.get_size()

    col,row,cell_width,cell_height = get_board_pos(pos,board,screen_width,screen_height)
  
    if 600<=pos[0]<=680 and 10<=pos[1]<=70 and switch[0] == 1:
        dice_roll[0],dice_roll[1] = roll_dice()
        switch[0] = 0
        on_table[0] = False
        print(f" rolled: {dice_roll}")
        piece_x = 50 + row * 54
        piece_y = 10 + col * 54
        dice_image1 = pygame.image.load(f"Images/you_dice_{dice_roll[0]}.png")
        dice_image2 = pygame.image.load(f"Images/you_dice_{dice_roll[1]}.png")
        screen.blit(dice_image1, (piece_x, piece_y))
        piece_x += dice_image1.get_height()
        screen.blit(dice_image2, (piece_x, piece_y)) 
    # Check if the click is within the bounds of the board
    if (0 <= row < len(board[0]) and 0 <= col < len(board) and
            len(board)>=(pos[1] - 75) / cell_width >= 0 and (pos[0] - 45) / cell_height >= 0) :
        print(f"Clicked on row {row}, column {col}")
        on_table[0] = True
        if board[col][row] != 0 :
           print(f"{abs(board[col][row])} pieces on the row")
    else:
        on_table[0] = False
        print("Clicked outside of the board")
   
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def random_move(board,board_image,turn,switch,dice_roll,on_table,screen_width,screen_height):
   move_pos = []
   pos_buffer2 = (0,0)
   while(len(move_pos)<2):
      pos_buffer = (random.randint(0,800),random.randint(0,800))
      if(pos_buffer!=pos_buffer2):
        handle_click(pos_buffer,board,board_image,turn,switch,dice_roll,on_table)
        if(on_table[0]==True):
          move_pos.append(pos_buffer)
      pos_buffer2 = pos_buffer
   return move_pos
 
def move_piece(move, board, screen_width, screen_height, dice):
    col1, row1, cell_width1, cell_height1 = get_board_pos(move[0], board, screen_width, screen_height)
    col2, row2, cell_width1, cell_height1 = get_board_pos(move[1], board, screen_width, screen_height)

    if board[col1][row1] > 0 and board[col2][row2] >= 0 :
        board[col2][row2] += 1
        board[col1][row1] -= 1
    elif board[col1][row1] > 0 and board[col2][row2] == -1:
        board[col2][row2] += 2
        board[col1][row1] -= 1
        board[1][6] -= 1
    elif board[col1][row1] < 0 and board[col2][row2] <= -1:
        board[col1][row1] += 1
        board[col2][row2] -= 1
    elif board[col1][row1] < 0 and board[col2][row2] == 1:
        board[col1][row1] += 1
        board[col2][row2] -= 2
        board[0][6] += 1
    elif board[col1][row1] < 0 and board[col2][row2] == 0:
        board[col1][row1] += 1
        board[col2][row2] -= 1
    elif board[0][6] > 0 and (board[col2][row2] == board[1][dice[1]] or board[col2][row2]==board[1][dice[0]]) and board[col1][row1] == board[0][6] :
        if(board[col2][row2]>=0):
         board[0][6] -= 1
         board[col2][row2] += 1
        elif board[col2][row2]==-1:
         board[0][6] -= 1
         board[col2][row2] += 2
         board[1][6] -=1
    elif board [1][6] < 0 and (board[col2][row2] == board[0][dice[1]] or board[col2][row2]==board[0][dice[0]]) and board[col1][row1] == board[0][6]:
        if(board[col2][row2]==0):
         board[1][6] += 1
         board[col2][row2] -= 1
        elif board[col2][row2]==1:
         board[1][6] += 1
         board[col2][row2] -= 2

    return board

def pull(pos, board, screen_width, screen_height,dice,turn):
    col1, row1, cell_width1, cell_height1 = get_board_pos(pos, board, screen_width, screen_height)
    check = False
    if turn[0] == 1:
       if board[col1][row1] >0:
                if board[col1][row1] == dice[0] -1 :
                      board[col1][row1] -=1
                elif board[col1][row1] == dice[1] -1 :
                      board[col1][row1] -=1  
    elif turn[0] == 2:
       if board[col1][row1] <0 :
             if board[col1][row1] == dice[0] -1:
                      board[col1][row1] +=1
             elif board[col1][row1] == dice[1] -1 :
                      board[col1][row1] +=1 

def helper(row1,row2,dice):
       for i in range(row1,row1 + dice[0]+1):
         if i==6 and row1 < 6 and row2>6:
            return 1
       for i in range(row1,row1 + dice[1]+1):
         if i==6 and row1<6 and row2>6:
           return 1
       for i in range(row1-dice[0]-1,row1):
         if i==6 and row1>6 and row2<6:
           return 1
       for i in range(row1-dice[1]-1,row1):
         if i==6 and row1>6 and row2<6:
           return 1
       return 0       

def check_move(move,board,screen_width,screen_height,dice,turn):
   
   col1,row1,cell_width1,cell_height1 = get_board_pos(move[0],board,screen_width,screen_height)
   col2,row2,cell_width1,cell_height1 = get_board_pos(move[1],board,screen_width,screen_height)
   check = False
   dice_buff=0
    
   if turn[0]==1 : 
     if board[0][6] > 0 :
       if row1 == 6 and col2 == 1 and row2 == dice[0]-1 :
          if board[col2][row2] >=0:
              check = True
              dice_buff=dice[0]
          elif board[col2][row2] ==-1:
              check = True
              dice_buff=dice[0]

       elif row1 == 6 and col2 == 1 and row2 == dice[1]-1:
          if board[col2][row2] >=0:
              check = True
              dice_buff=dice[1]
          elif board[col2][row2] ==-1:
              check = True
              dice_buff=dice[1]

       elif row1 == 6 and col2 == 1 and row2 == dice[1]-1:
          if board[col2][row2] <-1:
              check = False
              dice_buff=dice[1]

       elif row1 == 6 and col2 == 1 and row2 == dice[0]-1:
          if board[col2][row2] <-1:
              check = False
              dice_buff=dice[1]
     else:
              if board[col1][row1]>0:
                if row1 == 6 and col2 == 1 and row2 == dice[0]-1 :
                  if board[col2][row2] >=0:
                      check = True
                      dice_buff=dice[0]
                  elif board[col2][row2] ==-1:
                      check = True
                      dice_buff=dice[0]

                elif row1 == 6 and col2 == 1 and row2 == dice[1]-1:
                  if board[col2][row2] >=0:
                      check = True
                      dice_buff=dice[1]
                  elif board[col2][row2] ==-1:
                      check = True
                      dice_buff=dice[1]

                elif row1 == 6 and col2 == 1 and row2 == dice[1]-1:
                  if board[col2][row2] <-1:
                      check = False
                      dice_buff=dice[1]

                elif row1 == 6 and col2 == 1 and row2 == dice[0]-1:
                  if board[col2][row2] <-1:
                      check = False
                      dice_buff=dice[1]
                      
                elif 12-(row1+dice[0]-13) == row2 and col1==1 and col2==0 :
                  if board[col2][row2] >=0 :
                    check = True
                    dice_buff=dice[0]
                  elif board[col2][row2] ==-1:
                    check = True 
                    dice_buff=dice[0]

                elif 12-(row1+dice[1]-13) == row2 and col1==1 and col2==0 :
                  if board[col2][row2] >=0 :
                    check = True
                    dice_buff=dice[1]
                  elif board[col2][row2] ==-1:
                    check = True 
                    dice_buff=dice[1]

                elif row1<6 and row1+dice[0]+1==row2 and 6<=row1+dice[0]<12 and col1==col2==1 and row1<row2 and row2!=6 and row1!=6:
                  if helper(row1,row2,dice)==1:
                    if board[col2][row2] >=0 :
                      check = True
                      dice_buff=dice[0]
                    elif board[col2][row2] ==-1:
                      check = True
                      dice_buff=dice[0]

                elif row1>6 and row1-dice[0]-1==row2 and row1-dice[0]-1<=6 and col1==col2==0 and row1>row2 and row2!=6 and row1!=6:
                  if helper(row1,row2,dice)==1: 
                    if board[col2][row2] >=0 :
                      check = True
                      dice_buff=dice[0]
                    elif board[col2][row2] ==-1:
                      check = True 
                      dice_buff=dice[0]

                elif row1<6 and row1+dice[1]+1==row2 and 6<=row1+dice[1]+1<12 and col1==col2==1 and row1<row2 and row2!=6 and row1!=6:
                  if helper(row1,row2,dice)==1:  
                    if board[col2][row2] >=0 :
                      check = True
                      dice_buff=dice[1]
                    elif board[col2][row2] ==-1:
                      check = True
                      dice_buff=dice[1]

                elif row1>6 and row1-dice[1]-1==row2 and row1-dice[1]-1<=6 and col1==col2==0 and row1>row2 and row2!=6 and row1!=6:
                  if helper(row1,row2,dice)==1:
                    if board[col2][row2] >=0 :
                      check = True
                      dice_buff=dice[1]
                    elif board[col2][row2] ==-1:
                      check = True 
                      dice_buff=dice[1]  
                        
                elif row1+dice[0] == row2 and col1==col2==1 and row1<row2 and row2!=6 and row1!=6:
                  if helper(row1,row2,dice)==0:
                    if board[col2][row2] >=0 :
                      check = True
                      dice_buff=dice[0]
                    elif board[col2][row2] ==-1:
                      check = True
                      dice_buff=dice[0]
                    
                elif row1+dice[1]==row2 and col1==col2==1 and row1<row2 and row2!=6 and row1!=6:
                  if helper(row1,row2,dice)==0:
                    if board[col2][row2] >=0 :
                      check = True
                      dice_buff=dice[1]
                    elif board[col2][row2] ==-1:
                      check = True
                      dice_buff=dice[1]

                elif row1-dice[0]==row2 and col1==col2==0 and row1>row2 and row2!=6 and row1!=6:
                  if helper(row1,row2,dice)==0:
                    if board[col2][row2] >=0 :
                      check = True
                      dice_buff=dice[0]
                    elif board[col2][row2] ==-1:
                      check = True
                      dice_buff=dice[0]

                elif row1-dice[1]==row2 and col1==col2==0 and row1>row2 and row2!=6 and row1!=6:
                  if helper(row1,row2,dice)==0:
                    if board[col2][row2] >=0 :
                      check = True
                      dice_buff=dice[1]
                    elif board[col2][row2] ==-1:
                      check = True
                      dice_buff=dice[1]

   elif turn[0]==2: 
     if board[1][6] <0:
        if row1 == 6 and col2 == 0 and row2 == dice[0]-1 :
              if board[col2][row2] <=0:
                  check = True
                  dice_buff=dice[0]
              elif board[col2][row2] ==1:
                  check = True 
                  dice_buff=dice[0]

        elif row1 == 6 and col2 == 0 and row2 == dice[1]-1:
              if board[col2][row2] <=0:
                  check = True
                  dice_buff=dice[1]
              elif board[col2][row2] ==1:
                  check = True 
                  dice_buff=dice[1]

        elif row1 == 6 and col2 == 0 and row2 == dice[0]-1:
              if board[col2][row2] >0:
                  check = False
                  dice_buff=dice[1]

        elif row1 == 6 and col2 == 0 and row2 == dice[1]-1:
              if board[col2][row2] >0:
                  check = False
                  dice_buff=dice[0] 
     else:    
          if board[col1][row1]<0:
            if row1 == 6 and col2 == 0 and row2 == dice[0]-1 :
              if board[col2][row2] <=0:
                  check = True
                  dice_buff=dice[0]
              elif board[col2][row2] ==1:
                  check = True 
                  dice_buff=dice[0]

            elif row1 == 6 and col2 == 0 and row2 == dice[1]-1:
              if board[col2][row2] <=0:
                  check = True
                  dice_buff=dice[1]
              elif board[col2][row2] ==1:
                  check = True 
                  dice_buff=dice[1]

            elif row1 == 6 and col2 == 0 and row2 == dice[0]-1:
              if board[col2][row2] >0:
                  check = False
                  dice_buff=dice[1]

            elif row1 == 6 and col2 == 0 and row2 == dice[1]-1:
              if board[col2][row2] >0:
                  check = False
                  dice_buff=dice[0]
                  
            elif 12-(row1+dice[0]-13) == row2 and col1==0 and col2==1 :
              if board[col2][row2] <=0 :
                check = True
                dice_buff=dice[0]
              elif board[col2][row2] ==1:
                check = True 
                dice_buff=dice[0]

            elif 12-(row1+dice[1]-13) == row2 and col1==0 and col2==1:
              if board[col2][row2] <=0 :
                check = True
                dice_buff=dice[1]
              elif board[col2][row2] ==1:
                check = True 
                dice_buff=dice[1]

            elif row1<6 and row1+dice[0]+1==row2  and col1==col2==0 and row1<row2 and row2!=6 and row1!=6:
              if helper(row1,row2,dice)==1:  
                if board[col2][row2] <=0 :
                  check = True
                  dice_buff=dice[0]
                elif board[col2][row2] ==1:
                  check = True
                  dice_buff=dice[0]

            elif row1<6 and row1+dice[1]+1==row2  and col1==col2==0 and row1<row2 and row2!=6 and row1!=6:
              if helper(row1,row2,dice)==1: 
                if board[col2][row2] <=0 :
                  check = True
                  dice_buff=dice[1]
                elif board[col2][row2] ==1:
                  check = True
                  dice_buff=dice[1]

            elif row1>6 and row1-dice[0]-1==row2 and row1-dice[0]-1<=6 and col1==col2==1 and row1>row2 and row2!=6 and row1!=6:
              if helper(row1,row2,dice)==1:  
                if board[col2][row2] <=0 :
                  check = True
                  dice_buff=dice[0]
                elif board[col2][row2] ==1:
                  check = True
                  dice_buff=dice[0]

            elif row1>6 and row1-dice[1]-1==row2 and row1-dice[1]-1<=6 and col1==col2==1 and row1>row2 and row2!=6 and row1!=6:
              if helper(row1,row2,dice)==1:  
                if board[col2][row2] <=0 :
                  check = True
                  dice_buff=dice[1]
                elif board[col2][row2] ==1:
                  check = True
                  dice_buff=dice[1]
                      
            elif row1+dice[0] == row2 and col1==col2==0 and row1<row2 and row2!=6 and row1!=6:
              if helper(row1,row2,dice)==0:
                if board[col2][row2] <=0 :
                  check = True
                  dice_buff=dice[0]
                elif board[col2][row2] ==1:
                  check = True
                  dice_buff=dice[0]

            elif row1+dice[1]==row2  and col1==col2==0 and row1<row2 and row2!=6 and row1!=6:
              if helper(row1,row2,dice)==0:
                if board[col2][row2] <=0 :
                  check = True
                  dice_buff=dice[1]
                elif board[col2][row2] ==1:
                  check = True
                  dice_buff=dice[1]

            elif row1-dice[0]==row2 and col1==col2==1 and row1>row2 and row2!=6 and row1!=6:
              if helper(row1,row2,dice)==0:
                if board[col2][row2] <=0 :
                  check = True
                  dice_buff=dice[0]
                elif board[col2][row2] ==1:
                  check = True
                  dice_buff=dice[0]

            elif row1-dice[1]==row2 and col1==col2==1 and row1>row2 and row2!=6 and row1!=6:
              if helper(row1,row2,dice)==0:
                if board[col2][row2] <=0 :
                  check = True
                  dice_buff=dice[1]
                elif board[col2][row2] ==1:
                  check = True
                  dice_buff=dice[1]
      
   return check,dice_buff

def check_winner(board):
  winner1 = 0
  winner2 = 0
  player =0
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] >0:
        winner1 = 1
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] <0:
        winner2 = 2   
  if(winner1 == 0):
    player = 1
  elif(winner2 == 0):
    player = 2
  return player

def check_dice(board,dice):
  
   if board[0][6] >0 :
      j=1
      for i in range(len(board[0])//2):
          if i==dice-1 :
            if board[j][i] <-1:
              return False
   elif board[1][6]<0:
      j=0
      for i in range(len(board[1])//2):      
          if i==dice-1 :
            if board[j][i] >1:
              return False
      
   return True

def check_base(board):
      j=0
      for i in range(len(board)):
        if i==0:
          j==7
          for j in range(len(board[0])) :
            if board[i][j] > 0:
              return False
      for i in range(len(board)) :
        if i==1:
          j==7
          for j in range(len(board[0])):
            if board[i][j] < 0:
              return False
      return True
# Player vs Computer game loop
def player_vs_computer_game():
    print("Player vs Computer game")
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    # Set up initial pieces
    board[0][0] = -2
    board[0][5] = 5
    board[0][8] = 3
    board[0][12] = -5
    board[1][5] = -5
    board[1][8] = -3
    board[1][0] = 2
    board[1][12] = 5

    font = pygame.font.SysFont('Arial', 20)

    screen.fill((255, 255, 255))
    draw_board()
    draw_initial_pieces(board)
    draw_initial_dice()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

    turn = [1]  # White turn
    text = font.render(f"Turn: Player {turn[0]}", True, (0, 0, 0))
    pygame.draw.rect(screen, WHITE, (10, 10, 130, 30))
    screen.blit(text, (10, 10))

    message_font = pygame.font.SysFont('Arial', 20)
    message_rect = pygame.Rect(150, 10, 380, 30)

    switch = [1]
    dice_roll = [0, 0]
    move_pos = []
    moves1=2
    moves2=4
    while True:
     if check_winner(board) == 1:
      pygame.draw.rect(screen, WHITE, message_rect)
      text = message_font.render("Player 1 wins", True, BLACK)
      screen.blit(text, message_rect.topleft)
     elif check_winner(board) == 2:
      pygame.draw.rect(screen, WHITE, message_rect)
      text = message_font.render("Player 2 wins", True, BLACK)
      screen.blit(text, message_rect.topleft) 
     on_table = [False]
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          pos_buff = pygame.mouse.get_pos()
          handle_click(pos_buff,board,board_image,turn,switch,dice_roll,on_table)
          if dice_roll[0]!=0 and dice_roll[1]!=0 :
            save_dice = dice_roll[:]
          if turn[0]==1:
            if dice_roll[0]!=dice_roll[1]: 
              if check_dice(board,save_dice[0])==False and check_dice(board,save_dice[1])==False:
                 moves1=0
                 moves2=0
              elif (check_dice(board,save_dice[0])==False and check_dice(board,save_dice[1])==True) or (check_dice(board,save_dice[0])==True and check_dice(board,save_dice[1])==False):
                   moves1-=1
              if on_table[0] == True:
                print(check_base(board))
                if check_base(board):
                    pull(pos_buff,board,width,height,dice_roll,turn)
                    moves1-=1
                move_pos.append(pos_buff)
                print(move_pos)
              if(len(move_pos)==2):
                check,dice_buff = check_move(move_pos,board,width,height,dice_roll,turn)
                if check==True:
                  board = move_piece(move_pos,board,width,height,dice_roll)
                  if(dice_buff==dice_roll[0]):
                        dice_roll[0] =0
                  elif dice_buff==dice_roll[1]:
                        dice_roll[1] =0
                  draw_board()
                  draw_initial_pieces(board)
                  piece_x = 50 + 10 * 54 # identation + row * board cell size 
                  piece_y = 10
                  dice_image1 = pygame.image.load(f"Images/you_dice_{save_dice[0]}.png")
                  dice_image2 = pygame.image.load(f"Images/you_dice_{save_dice[1]}.png")
                  screen.blit(dice_image1, (piece_x, piece_y))
                  piece_x += dice_image1.get_height()
                  screen.blit(dice_image2, (piece_x, piece_y))
                  text = font.render(f"Turn: Player {turn[0]}", True, (0, 0, 0))
                  pygame.draw.rect(screen, WHITE, (10, 10, 130, 30))
                  screen.blit(text, (10, 10))
                  print(check_move(move_pos,board,width,height,dice_roll,turn),moves1)
                  moves1 -= 1
                else:  
                    pygame.draw.rect(screen, WHITE, message_rect)
                    text = message_font.render("Invalid Move! Try Again!", True, BLACK)
                    screen.blit(text, message_rect.topleft)
                move_pos = []
            elif dice_roll[0]==dice_roll[1]:
              if check_dice(board,save_dice[0])==False and check_dice(board,save_dice[1])==False:
                     moves1=0
                     moves2=0
              elif (check_dice(board,save_dice[0])==False and check_dice(board,save_dice[1])==True) or (check_dice(board,save_dice[0])==True and check_dice(board,save_dice[1])==False):
                     moves2-=1
              if on_table[0] == True:
                if check_base(board):
                    pull(pos_buff,board,width,height,dice_roll,turn)
                    moves2-=1
                move_pos.append(pos_buff)
                print(move_pos)
              if(len(move_pos)==2):
                  check,dice_buff = check_move(move_pos,board,width,height,dice_roll,turn)
                  if check==True:
                    board = move_piece(move_pos,board,width,height,dice_roll)
                    draw_board()
                    draw_initial_pieces(board)
                    piece_x = 50 + 10 * 54 # identation + row * board cell size 
                    piece_y = 10
                    dice_image1 = pygame.image.load(f"Images/you_dice_{save_dice[0]}.png")
                    dice_image2 = pygame.image.load(f"Images/you_dice_{save_dice[1]}.png")
                    screen.blit(dice_image1, (piece_x, piece_y))
                    piece_x += dice_image1.get_height()
                    screen.blit(dice_image2, (piece_x, piece_y))
                    text = font.render(f"Turn: Player {turn[0]}", True, (0, 0, 0))
                    pygame.draw.rect(screen, WHITE, (10, 10, 130, 30))
                    screen.blit(text, (10, 10))
                    moves2 -= 1
                  else:  
                    pygame.draw.rect(screen, WHITE, message_rect)
                    text = message_font.render("Invalid Move! Try Again!", True, BLACK)
                    screen.blit(text, message_rect.topleft)
                  move_pos = []
          elif(turn[0] ==2):
            while(turn[0] ==2):
                 move_pos = random_move(board,board_image,turn,switch,dice_roll,on_table,width,height)
                 check,dice_buff=check_move(move_pos,board,width,height,dice_roll,turn)
                 if dice_roll[0]!=dice_roll[1]: 
                      if check_dice(board,save_dice[0])==False and check_dice(board,save_dice[1])==False:
                        moves1=0
                      elif (check_dice(board,save_dice[0])==False and check_dice(board,save_dice[1])==True) or (check_dice(board,save_dice[0])==True and check_dice(board,save_dice[1])==False):
                        moves2-=1
                      if on_table[0] == True:
                        if check_base(board):
                         pull(pos_buff,board,width,height,dice_roll,turn)
                         moves1-=1
                        print(move_pos)
                      if(len(move_pos)==2):
                        if check==True:
                          board = move_piece(move_pos,board,width,height,dice_roll)
                          if(dice_buff==dice_roll[0]):
                                dice_roll[0] =0
                          elif dice_buff==dice_roll[1]:
                                dice_roll[1] =0
                          draw_board()
                          draw_initial_pieces(board)
                          piece_x = 50 + 10 * 54 # identation + row * board cell size 
                          piece_y = 10
                          dice_image1 = pygame.image.load(f"Images/you_dice_{save_dice[0]}.png")
                          dice_image2 = pygame.image.load(f"Images/you_dice_{save_dice[1]}.png")
                          screen.blit(dice_image1, (piece_x, piece_y))
                          piece_x += dice_image1.get_height()
                          screen.blit(dice_image2, (piece_x, piece_y))
                          text = font.render(f"Turn: Player {turn[0]}", True, (0, 0, 0))
                          pygame.draw.rect(screen, WHITE, (10, 10, 130, 30))
                          screen.blit(text, (10, 10))
                          print(check_move(move_pos,board,width,height,dice_roll,turn),moves1)
                          moves1 -= 1
                        else:  
                            pygame.draw.rect(screen, WHITE, message_rect)
                            text = message_font.render("Invalid Move! Try Again!", True, BLACK)
                            screen.blit(text, message_rect.topleft)
                        move_pos = []
                 elif dice_roll[0]==dice_roll[1]:
                    if check_dice(board,save_dice[0])==False and check_dice(board,save_dice[1])==False:
                            moves2=0
                    elif (check_dice(board,save_dice[0])==False and check_dice(board,save_dice[1])==True) or (check_dice(board,save_dice[0])==True and check_dice(board,save_dice[1])==False):
                            moves2-=1
                    if on_table[0] == True:
                      if check_base(board):
                         pull(pos_buff,board,width,height,dice_roll,turn)
                         moves2-=1
                      print(move_pos)
                    if(len(move_pos)==2):
                        check,dice_buff = check_move(move_pos,board,width,height,dice_roll,turn)
                        if check==True:
                          board = move_piece(move_pos,board,width,height,dice_roll)
                          draw_board()
                          draw_initial_pieces(board)
                          piece_x = 50 + 10 * 54 # identation + row * board cell size 
                          piece_y = 10
                          dice_image1 = pygame.image.load(f"Images/you_dice_{save_dice[0]}.png")
                          dice_image2 = pygame.image.load(f"Images/you_dice_{save_dice[1]}.png")
                          screen.blit(dice_image1, (piece_x, piece_y))
                          piece_x += dice_image1.get_height()
                          screen.blit(dice_image2, (piece_x, piece_y))
                          text = font.render(f"Turn: Player {turn[0]}", True, (0, 0, 0))
                          pygame.draw.rect(screen, WHITE, (10, 10, 130, 30))
                          screen.blit(text, (10, 10))
                          moves2 -= 1
                        else:  
                          pygame.draw.rect(screen, WHITE, message_rect)
                          text = message_font.render("Invalid Move! Try Again!", True, BLACK)
                          screen.blit(text, message_rect.topleft)
                        move_pos = []
                    if moves1 == 0 or moves2 == 0:
                        moves1=2
                        moves2=4
                        turn[0] = 2 if turn[0] == 1 else 1
                        switch[0]=1
                        text = font.render(f"Turn: Player {turn[0]}", True, (0, 0, 0))
                        pygame.draw.rect(screen, WHITE, (10, 10, 130, 30))
                        screen.blit(text, (10, 10))
          if moves1 == 0 or moves2 == 0:
               moves1=2
               moves2=4
               turn[0] = 2 if turn[0] == 1 else 1
               switch[0]=1
               text = font.render(f"Turn: Player {turn[0]}", True, (0, 0, 0))
               pygame.draw.rect(screen, WHITE, (10, 10, 130, 30))
               screen.blit(text, (10, 10))

     pygame.display.flip()
     pygame.time.Clock().tick(60) 

# Player vs Player game loop
def player_vs_player_game():
    print("Player vs Player game")
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    # Set up initial pieces
    
    board[0][0] = -2
    board[0][5] = 5
    board[0][8] = 3
    board[0][12] = -5
    board[1][5] = -5
    board[1][8] = -3
    board[1][0] = 2
    board[1][12] = 5

    font = pygame.font.SysFont('Arial', 20)

    screen.fill((255, 255, 255))
    draw_board()
    draw_initial_pieces(board)
    draw_initial_dice()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

    turn = [1]  # White turn
    text = font.render(f"Turn: Player {turn[0]}", True, (0, 0, 0))
    pygame.draw.rect(screen, WHITE, (10, 10, 130, 30))
    screen.blit(text, (10, 10))

    message_font = pygame.font.SysFont('Arial', 20)
    message_rect = pygame.Rect(150, 10, 380, 30)

    switch = [1]
    dice_roll = [0, 0]
    move_pos = []
    moves1=2
    moves2=4
    while True:
     if check_winner(board) == 1:
        pygame.draw.rect(screen, WHITE, message_rect)
        text = message_font.render("Player 1 wins", True, BLACK)
        screen.blit(text, message_rect.topleft)
     elif check_winner(board) == 2:
         pygame.draw.rect(screen, WHITE, message_rect)
         text = message_font.render("Player 2 wins", True, BLACK)
         screen.blit(text, message_rect.topleft) 
     on_table = [False]
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos_buff = pygame.mouse.get_pos()
            handle_click(pos_buff,board,board_image,turn,switch,dice_roll,on_table)
            if dice_roll[0]!=0 and dice_roll[1]!=0 :
              save_dice = dice_roll[:]
            if dice_roll[0]!=dice_roll[1]:
              if check_dice(board,save_dice[0])==False and check_dice(board,save_dice[1])==False:
                 moves1=0
                 moves2=0
              elif (check_dice(board,save_dice[0])==False and check_dice(board,save_dice[1])==True) or (check_dice(board,save_dice[0])==True and check_dice(board,save_dice[1])==False):
                   moves1-=1 
              if on_table[0] == True:
                if check_base(board):
                    pull(pos_buff,board,width,height,dice_roll,turn)
                    moves1-=1
                move_pos.append(pos_buff)
                print(move_pos)
              if(len(move_pos)==2):
                check,dice_buff = check_move(move_pos,board,width,height,dice_roll,turn)
                print(check)
                if check==True:
                  if(dice_buff==dice_roll[0]):
                        dice_roll[0] =0
                  elif dice_buff==dice_roll[1]:
                        dice_roll[1] =0
                  board = move_piece(move_pos,board,width,height,dice_roll)
                  draw_board()
                  draw_initial_pieces(board)
                  piece_x = 50 + 10 * 54 # identation + row * board cell size 
                  piece_y = 10
                  dice_image1 = pygame.image.load(f"Images/you_dice_{save_dice[0]}.png")
                  dice_image2 = pygame.image.load(f"Images/you_dice_{save_dice[1]}.png")
                  screen.blit(dice_image1, (piece_x, piece_y))
                  piece_x += dice_image1.get_height()
                  screen.blit(dice_image2, (piece_x, piece_y))
                  text = font.render(f"Turn: Player {turn[0]}", True, (0, 0, 0))
                  pygame.draw.rect(screen, WHITE, (10, 10, 130, 30))
                  screen.blit(text, (10, 10))
                  moves1 -= 1
                else:  
                    pygame.draw.rect(screen, WHITE, message_rect)
                    text = message_font.render("Invalid Move! Try Again!", True, BLACK)
                    screen.blit(text, message_rect.topleft)
                move_pos = []
            elif dice_roll[0]==dice_roll[1]:
              if check_dice(board,save_dice[0])==False and check_dice(board,save_dice[1])==False:
                 moves1=0
                 moves2=0
              elif (check_dice(board,save_dice[0])==False and check_dice(board,save_dice[1])==True) or (check_dice(board,save_dice[0])==True and check_dice(board,save_dice[1])==False):
                   moves1-=1
              if on_table[0] == True:
                if check_base(board):
                    pull(pos_buff,board,width,height,dice_roll,turn)
                    moves2-=1
                move_pos.append(pos_buff)
                print(move_pos)
              if(len(move_pos)==2):
                  check,dice_buff = check_move(move_pos,board,width,height,dice_roll,turn)
                  print(check)
                  if check==True:
                    board = move_piece(move_pos,board,width,height,dice_roll)
                    draw_board()
                    draw_initial_pieces(board)
                    piece_x = 50 + 10 * 54 # identation + row * board cell size 
                    piece_y = 10
                    dice_image1 = pygame.image.load(f"Images/you_dice_{save_dice[0]}.png")
                    dice_image2 = pygame.image.load(f"Images/you_dice_{save_dice[1]}.png")
                    screen.blit(dice_image1, (piece_x, piece_y))
                    piece_x += dice_image1.get_height()
                    screen.blit(dice_image2, (piece_x, piece_y))
                    text = font.render(f"Turn: Player {turn[0]}", True, (0, 0, 0))
                    pygame.draw.rect(screen, WHITE, (10, 10, 130, 30))
                    screen.blit(text, (10, 10))
                    moves2 -= 1
                  else:  
                    pygame.draw.rect(screen, WHITE, message_rect)
                    text = message_font.render("Invalid Move! Try Again!", True, BLACK)
                    screen.blit(text, message_rect.topleft)
                  move_pos = []
            if moves1 == 0 or moves2 == 0:
               moves1=2
               moves2=4
               turn[0] = 2 if turn[0] == 1 else 1
               switch[0]=1
               text = font.render(f"Turn: Player {turn[0]}", True, (0, 0, 0))
               pygame.draw.rect(screen, WHITE, (10, 10, 130, 30))
               screen.blit(text, (10, 10))   
     pygame.display.flip()
     pygame.time.Clock().tick(60) 

# Main program loop
while True:
    selected_option = main_menu()
    if selected_option == "player_vs_computer":
        player_vs_computer_game()
    elif selected_option == "player_vs_player":
        player_vs_player_game()