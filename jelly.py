import pygame
import random
import math

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 450, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jelly Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)

STANDARD_FONT = pygame.font.SysFont('comicsans', 40)

FPS = 60


def draw_window(board, score):

    # clear screen    
    pygame.draw.rect(WIN, BLACK, BORDER)

    # Draw score
    score_text = STANDARD_FONT.render("Score: " + str(score), 1, WHITE)
    WIN.blit(score_text, (10, 760))
    
    # Draw game board with cubes

    draw_board(board)

    pygame.display.update()


def draw_board(board):
    game_block = pygame.Rect(0, 0, 50, 50)
    pygame.draw.rect(WIN, YELLOW, game_block)

    temp_height = 0
    temp_width = 0
    for row in board:
        temp_width = 0
        for block in row:

            game_block = pygame.Rect(temp_width, temp_height, 50, 50)
            
            if (block == 1):
                color = YELLOW
            elif (block == 2):
                color = BLUE
            elif (block == 3):
                color = RED
            elif (block == 4):
                color = GREEN
            else:
                color = BLACK
            pygame.draw.rect(WIN, color, game_block)

            temp_width = temp_width + 50
        temp_height = temp_height + 50
        #pygame.draw.rect(WIN, YELLOW, bullet)

def end_game(text):
    draw_text = STANDARD_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def generate_board():

    board = []
    for x in range(15):
        row = []
        for y in range(9):
            row.append(random.randint(1, 4))
        board.append(row)

    return board

    
def nearby_same_color(color_number, up_color, down_color, left_color, right_color):
    if color_number == up_color or color_number == down_color or color_number == left_color or color_number == right_color:
        return True 
    return False


def get_valid_moves(board):
    valid_moves = []
  
    row = 0

    for rows in board:
        column = 0
        for block in rows:
       
            if(block == 0):
                column = column + 1  
                continue

            up_color = 0
            if(row > 0):
                up_color = board[row - 1][column]

            down_color = 0
            if(row < 14):
                down_color = board[row + 1][column]
            
            left_color = 0
            if(column > 0):
                left_color = board[row][column-1]

            right_color = 0
            if(column < 8):
                right_color = board[row][column+1]
                
            if nearby_same_color(block, up_color, down_color, left_color, right_color):
                
                valid_moves.append([row, column])
            
            column = column + 1    

        row = row + 1   

    return valid_moves


def clear_all_nearby(deleting_color, row, column, board, number_of_clears):

    if(row == -1):
        return board, number_of_clears

    if(row == 15):
        return board, number_of_clears

    if(column == -1):
        return board, number_of_clears

    if(column == 9):
        return board, number_of_clears


    if deleting_color == board[row][column]:
        board[row][column] = 0
        number_of_clears = number_of_clears + 1
        board, number_of_clears = clear_all_nearby(deleting_color, row+1, column, board, number_of_clears)
        board, number_of_clears = clear_all_nearby(deleting_color, row-1, column, board, number_of_clears)
        board, number_of_clears = clear_all_nearby(deleting_color, row, column-1, board, number_of_clears)
        board, number_of_clears = clear_all_nearby(deleting_color, row, column+1, board, number_of_clears)
    return board, number_of_clears

def add_score(number_of_clears):
    if(number_of_clears==2):
        return 2
    elif(number_of_clears==3):
        return 5
    elif(number_of_clears==4):
        return 8
    elif(number_of_clears==5):
        return 13
    elif(number_of_clears==6):
        return 18   
    elif(number_of_clears==7):
        return 25
    elif(number_of_clears==8):
        return 32
    elif(number_of_clears==9):
        return 41
    elif(number_of_clears==10):
        return 50        # THIS IS FAKED
    elif(number_of_clears==11):
        return 61
    elif(number_of_clears==12):
        return 70        # THIS IS FAKED
    elif(number_of_clears==13):
        return 85
    elif(number_of_clears==14):
        return 90        # THIS IS FAKED
    elif(number_of_clears==15):
        return 100        # THIS IS FAKED
    elif(number_of_clears==16):
        return 110        # THIS IS FAKED
    else:
        return 999999     # THIS IS FAKED

def are_there_colors_above(colors, row, column, board):
    if(row == 0):
        return colors

    if (board[row][column] == 0):
        return colors
    
    if (board[row][column] != 0):
        colors.append([row, column])
        colors = are_there_colors_above(colors, row-1, column, board)
    return colors

def fill_board(board):

    row = 0
    for rows in board:
        column = 0
        for block in rows:
            if board[14][column] == 0:
                break

            if(block == 0):
                board[row][column] = random.randint(1, 4)

            column = column + 1
        row = row + 1
    return board

def remove_column(column, board):
    del board[0][column]
    del board[1][column]
    del board[2][column]
    del board[3][column]
    del board[4][column]
    del board[5][column]
    del board[6][column]
    del board[7][column]
    del board[8][column]
    del board[9][column]
    del board[10][column]
    del board[11][column]
    del board[12][column]
    del board[13][column]
    del board[14][column]
    return board

def add_column(board):
    board[0].append(0)
    board[1].append(0)
    board[2].append(0)
    board[3].append(0)
    board[4].append(0)
    board[5].append(0)
    board[6].append(0)
    board[7].append(0)
    board[8].append(0)
    board[9].append(0)
    board[10].append(0)
    board[11].append(0)
    board[12].append(0)
    board[13].append(0)
    board[14].append(0) 
    return board


def execute_column_break(board, active_columns):

    should_board_be_filled = False
    columns_to_remove = []
    for column in range(active_columns):
        if(board[14][column] == 0):
            columns_to_remove.append(column)
            active_columns = active_columns -1

    if(len(columns_to_remove)>0):
        should_board_be_filled = True
        reversed_list = columns_to_remove[::-1]
        for reversed in reversed_list:
            board = add_column(board)
            board = remove_column(reversed, board)

    return board, active_columns, should_board_be_filled

def execute_gravity(board):

    row = 0
    for rows in board:
        column = 0
        for block in rows:
       
            if(block == 0):
                column = column + 1
                continue

            if(row > 13):
                break            

            # Can block move down?
            if(board[row + 1][column] == 0):
                board[row + 1][column] = board[row][column]
                board[row][column] = 0
                # Run it again
                execute_gravity(board)
            
            column = column + 1    

        row = row + 1   

    return board

def main():

    score = 0
    
    board = generate_board()
    active_columns = 9
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
    
        valid_moves = get_valid_moves(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                
                
                print(len(valid_moves))
                
                x, y = pygame.mouse.get_pos()
                column = math.floor(x/50)
                row = math.floor(y/50)
                print(row,column, board[row][column])
                if ([row, column] in valid_moves and board[row][column] != 0):
                    board, number_of_clears = clear_all_nearby(board[row][column], row, column, board, 0)
                    score = score + add_score(number_of_clears)
                    board = execute_gravity(board)
                    board, active_columns, should_board_be_filled = execute_column_break(board, active_columns)
                    if (should_board_be_filled):
                        board = fill_board(board)
                


        if len(valid_moves) == 0:
            end_game('You lost')
            break

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_b]:
            print("\n\r")
            for row in board:
                print(row)

        if keys_pressed[pygame.K_c]:
            print(valid_moves)

        if keys_pressed[pygame.K_a]:
            score = score + 10
            print('A is pressed')

        draw_window(board, score)

    main()


if __name__ == "__main__":
    main()