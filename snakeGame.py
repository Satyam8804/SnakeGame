import pygame,sys
from playsound import playsound
import random
pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
yellow=(255,255,0)

init_velocity=3

screen_width=900
screen_height=560
gamewindow = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("Snake Game")

image = pygame.image.load('snake.png')
image2 = pygame.image.load('bg.png').convert()

#defining prey dimension
prey_x=random.randint(20,screen_width-20)
prey_y= random.randint(40,screen_height-20)
prey_size=10


clock=pygame.time.Clock()

font=pygame.font.SysFont('Helvetica',30)
font1=pygame.font.SysFont('Helvetica',55)

def display(text,color,x,y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])
def display1(text,color,x,y):
    screen_text = font1.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow ,color,snake_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,yellow,[x ,y ,snake_size,snake_size])
snk_list = []
#Game Loop
def gameloop():
    exit_game = False
    game_over = False

    # defining snake dimension
    snake_x = 45
    snake_y = 55
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    score = 0
    fps = 60
    snk_length = 1
    with open('hiscore.txt','r') as f:
         Hiscore=f.read()

    # defining prey dimension
    prey_x = random.randint(20, screen_width - 20)
    prey_y = random.randint(40, screen_height - 20)
    prey_size = 10
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(image2, (0, 0))

        if game_over:
            with open('hiscore.txt', 'w') as f:
                f.write(str(Hiscore))


            gamewindow.blit(image, (400, 100))
            display1("Game Over ! Press Enter To Continue",red,100,300)
            playsound('gameover.wav')

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                if event.type == pygame.QUIT:
                    exit_game = True


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:

                        velocity_x=velocity_x+init_velocity
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=velocity_x-init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y=velocity_y-init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y=velocity_y+init_velocity
                        velocity_x = 0

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(snake_x-prey_x)<6 and abs(snake_y-prey_y)<6:
                score+=10

                playsound('snake.wav')

                prey_x = random.randint(20, screen_width-20)
                prey_y = random.randint(20, screen_height-20)
                snk_length+=5
                if score>int(Hiscore):
                    Hiscore=score


            pygame.draw.rect(gamewindow,yellow,[snake_x , snake_y ,snake_size,snake_size])
            display(" Score :  "+str(score), red, 5, 5)
            display(" HiScore :  " + str(Hiscore), red, screen_width-200, 5)
            #creating prey
            pygame.draw.rect(gamewindow,red,[prey_x,prey_y,prey_size,prey_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True

            if snake_x>screen_width or snake_x<0 or snake_y<0 or snake_y>screen_height:
                game_over=True


            plot_snake(gamewindow,yellow,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

gameloop()

