import pygame
import random
import time
from pygame import mixer

# Initialization
pygame.init()

# Create a screen
screen = pygame.display.set_mode((700,700))

# Title and Icon
pygame.display.set_caption("Snake_&_Ladder")
icon = pygame.image.load("apple.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("Game.jpeg")
# Background music 
mixer.music.load('Background_music.mp3')
mixer.music.play(-1)

# Map Snakes and ladders 
ladder = {
    1 : 38 ,
    4 : 14 ,
    9 : 31 ,
    21 : 42 ,
    28 : 84 ,
    51 : 67 ,
    72 : 91 ,
    80 : 99 ,
}
ladder_keys=[1,4,9,21,28,51,72,80]
snake = {
    17 : 7 ,
    54 : 34 ,
    62 : 19 ,
    64 : 60 ,
    87 : 36 ,
    93 : 73 ,
    95 : 75 ,
    98 : 79 ,
}

# Map
map =  {
    1: [0, 576], 2: [64, 576], 3: [128, 576], 4: [192, 576], 5: [256, 576], 6: [320, 576], 7: [384, 576], 8: [448, 576], 9: [512, 576], 10: [576, 576],
    11: [576, 512], 12: [512, 512], 13: [448, 512], 14: [384, 512], 15: [320, 512], 16: [256, 512], 17: [192, 512], 18: [128, 512], 19: [64, 512], 20: [0, 512], 
    21: [0, 448], 22: [64, 448], 23: [128, 448], 24: [192, 448], 25: [256, 448], 26: [320, 448], 27: [384, 448], 28: [448, 448], 29: [512, 448], 30: [576, 448], 
    31: [576, 384], 32: [512, 384], 33: [448, 384], 34: [384, 384], 35: [320, 384], 36: [256, 384], 37: [192, 384], 38: [128, 384], 39: [64, 384], 40: [0, 384], 
    41: [0, 320], 42: [64, 320], 43: [128, 320], 44: [192, 320], 45: [256, 320], 46: [320, 320], 47: [384, 320], 48: [448, 320], 49: [512, 320], 50: [576, 320], 
    51: [576, 256], 52: [512, 256], 53: [448, 256], 54: [384, 256], 55: [320, 256], 56: [256, 256], 57: [192, 256], 58: [128, 256], 59: [64, 256], 60: [0, 256],
    61: [0, 192], 62: [64, 192], 63: [128, 192], 64: [192, 192], 65: [256, 192], 66: [320, 192], 67: [384, 192], 68: [448, 192], 69: [512, 192], 70: [576, 192], 
    71: [576, 128], 72: [512, 128], 73: [448, 128], 74: [384, 128], 75: [320, 128], 76: [256, 128], 77: [192, 128], 78: [128, 128], 79: [64, 128], 80: [0, 128], 
    81: [0, 64], 82: [64, 64], 83: [128, 64], 84: [192, 64], 85: [256, 64], 86: [320, 64], 87: [384, 64], 88: [448, 64], 89: [512, 64], 90: [576, 64], 
    91: [576, 0], 92: [512, 0], 93: [448, 0], 94: [384, 0], 95: [320, 0], 96: [256, 0], 97: [192, 0], 98: [128, 0], 99: [64, 0], 100: [0, 0]
}



# Players 
p1 = pygame.image.load("p1.png")
p2 = pygame.image.load("p2.png")
p3 = pygame.image.load("p3.png")
player = {
    1 : [ 0 , 3-30-20 , 610-30-6 , p1 ] ,
    2 : [ 0 , 3-30-6, 642-30-34 , p2 ] ,
    3 : [ 0 , 3-30-34 , 673-30-34 , p3 ] ,
}

# Player turn
i = 1
i_ = 1
dice = 0

'''
Image Blitting
'''
def player_blit():
    # Background Blitting
    screen.fill((0,0,0))
    screen.blit(background,(30,30))
    # Player Blitting
    screen.blit(player[1][3],(player[1][1]+30+20,player[1][2]+30+6))
    screen.blit(player[2][3],(player[2][1]+30+6,player[2][2]+30+34))
    screen.blit(player[3][3],(player[3][1]+30+34,player[3][2]+30+34))
    # Text Blitting
    dice_text = dice_font.render( str(dice) , True , (224,224,224) )
    player_text = player_font.render("Player : " + str(i_) , True , (204,204,255) )
    screen.blit( dice_text , (340,5))
    screen.blit( player_text , (5,5))
    # time.sleep(0.01)
    pygame.display.update()
    
    

def transition():
    global final_Xpos , final_Ypos
    initial_Xpos = player[i][1]
    initial_Ypos = player[i][2]
    final_Xpos = map[player[i][0]][0]
    final_Ypos = map[player[i][0]][1]
    playerX_change = ( final_Xpos - initial_Xpos ) / 400
    playerY_change = ( final_Ypos - initial_Ypos ) / 400
    trans = True
    while trans :
        if distance() > 20 :
            player[i][1] += playerX_change
            player[i][2] += playerY_change
            player_blit()
        else :
            player[i][1] = final_Xpos
            player[i][2] = final_Ypos
            player_blit()
            trans = False

def distance():
    global final_Xpos , final_Ypos
    return (( final_Xpos - player[i][1])**2 + ( final_Ypos - player[i][2])**2)**0.5

def won(j):
    global running
    run = True
    wins_text = wins_font.render("Player "+ str(j)+" Won!!!" , True , (19,0,142) )
    # screen.blit( wins_text , (100,200))
    # pygame.display.update()
    while run :
        screen.blit( wins_text , (100,200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
                run = False



# Text data
dice_font = pygame.font.Font('freesansbold.ttf',22)
player_font = pygame.font.Font('freesansbold.ttf',22)
wins_font = pygame.font.Font('freesansbold.ttf',64)



# Game Loop
running = True
while running:
    screen.fill((0,0,0))
    player_blit()

    # str_hell = input()
    # dice = random.randint(1,6)


    need = True
    while need :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
                need = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    dice = random.randint(1,6)
                    need = False
            


    if player[i][0] + dice < 100 :
        player[i][0] += dice 
        transition()
        # player[i][1] = map[player[i][0]][0]
        # player[i][2] = map[player[i][0]][1]
        player_blit()
    elif player[i][0] + dice == 100 or player[i][0] == 100:
        player[i][0] += dice 
        transition()
        won(i)
    else:
        dice = 0
    

     
    # player should blit 
    # player_blit()

    if player[i][0] in ladder:
        player[i][0] = ladder[player[i][0]]
        transition()
        ladder_ = True 
    else :
        ladder_ = False


    if player[i][0] in snake:
        player[i][0] = snake[player[i][0]]
        transition()


    i_ =  i

    if i==1:
        i=2
    elif i==2:
        i=3
    else:
        i=1

    if dice == 6 or ladder_ :
        if i==1:
            i=3
        elif i==2:
            i=1
        else:
            i=2


    player_blit()   
    pygame.display.update()

