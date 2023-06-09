import pygame, cv2, random, os, mediapipe as mp
from pygame.locals import *

# Pygame initialization
pygame.init()
pygame.font.init()
pygame.mixer.init()
FPS = 60
screen_width = 1920
screen_height = 1080
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Balloon Pop")
pygame.display.set_icon(pygame.image.load(os.path.join('Icon', 'balloonpop.png')))
im = 'Images'
s = 'sound'
pop = pygame.mixer.Sound(os.path.join(s, 'pop.wav'))
gameoversfx = pygame.mixer.Sound(os.path.join(s, 'jumpscare2.wav'))
bgm = pygame.mixer.music.load(os.path.join(s, 'MainTheme.wav'))
color = (255,255,255)
black=(0,0,0) 
width = game_screen.get_width() 
height = game_screen.get_height() 
smallfont = pygame.font.SysFont('Arial',36)  
quitmenu = smallfont.render('Quit' , True , color) 
startmenu = smallfont.render('Start', True, color)
text = smallfont.render('Press Esc to quit', True, black)
bgmain = pygame.image.load('Images\\main-menu-notext.png')
startimg = pygame.image.load('Images\\startimg.png')
quitimg = pygame.image.load('Images\\quitimg.png')
gameoverimg = pygame.image.load('Images\\gameover.png')
startimgResized = pygame.image.load('Images\\startimg600x400.png')         
quitimgResized = pygame.image.load('Images\\quitimg500x350.png')
bg = pygame.image.load('Images\\bg.jpg')
bg2 = pygame.image.load('Images\\background2.png')
suspense = pygame.image.load('Images\\suspense.png')
suspense1 = pygame.image.load('Images\\suspense1.png')
suspense2 = pygame.image.load('Images\\suspense2.png')
credits = pygame.image.load('Images\\credits.png')
credits = pygame.transform.scale(credits,(screen_width,31))
backgroundimg = pygame.Surface((game_screen.get_size()))
backgroundimg.fill((100, 0, 0))
image = image2 = pygame.image.load('Images\\bg.jpg')
image = image.convert()
rect = image.get_rect()

image2 = image2.convert_alpha()
rect2 = image2.get_rect()

# Font initialization
font = pygame.font.SysFont("Arial", 42)
titlefont = pygame.font.Font((os.path.join('Text', 'BloodyText.ttf')), 36)

# Mediapipe initialization for hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
cap = cv2.VideoCapture(1)
cap.set(3, 1920)
cap.set(4, 1080)


# Balloon class
class Balloon:
    def __init__(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.skin_color = random.choice(['cyan', 'red', 'blue', 'black', 'white'])
        self.radius = random.randint(30, 50)
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = screen_height + self.radius
        self.speed = random.randint(6, 12)
        self.popped = False
        self.image = pygame.image.load(os.path.join(im, f'{self.skin_color}_balloon.png')).convert_alpha()
         
    def move(self):
        self.y -= self.speed
            
    def draw(self):
        if self.skin_color == 'black':
            pygame.draw.circle(game_screen, self.color, (self.x, self.y), self.radius)
            balloon_image_resized = pygame.transform.scale(self.image, ((self.radius * 2.15), self.radius * 3))
            game_screen.blit(balloon_image_resized, ((self.x - 1.5) - self.radius, (self.y - 3) - self.radius))
            
        elif self.skin_color == 'white':
            pygame.draw.circle(game_screen, self.color, (self.x, self.y), self.radius)
            balloon_image_resized = pygame.transform.scale(self.image, ((self.radius * 2.15), self.radius * 6))
            game_screen.blit(balloon_image_resized, ((self.x - 1.75) - self.radius, (self.y - 3) - self.radius))
            
        else:
            pygame.draw.circle(game_screen, self.color, (self.x, self.y), self.radius)
            balloon_image_resized = pygame.transform.scale(self.image, ((self.radius * 2.15), self.radius * 5))
            game_screen.blit(balloon_image_resized, ((self.x - 1.5) - self.radius, (self.y - 3) - self.radius))
            
    def time(self):
        if self.skin_color == 'white' and self.popped:
            return 3
        elif self.skin_color == 'black' and self.popped:
            return -5
        else:
            return 0 
    
            
def start():
    # main menu
    i = 0
    running = True
    while running:
        for event in pygame.event.get(): 
            # esc button setup
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.QUIT: 
                pygame.quit() 
            # if mouse is clicked...
            if event.type == pygame.MOUSEBUTTONDOWN: 
                #...on quit
                if width-740 <= mouse[0] <= width-600 and height/2+80 <= mouse[1] <= height/2+180: 
                    pygame.quit()
                #...on start
                if width-840 <= mouse[0] <= width-500 and height/2-170 <= mouse[1] <= height/2-60: 
                    main()
    
        # main menu display
        game_screen.blit(bgmain, (0, 0))
        game_screen.blit(startimg, (1000, 250))
        game_screen.blit(quitimg, (1100, 550))
        game_screen.blit(credits,(i,0))
        game_screen.blit(credits,(i,1047))
        game_screen.blit(credits,(screen_width+i,0))
        game_screen.blit(credits,(screen_width+i,1047))
        if (i==-screen_width):
            game_screen.blit(credits,(screen_width+i,0))
            game_screen.blit(credits,(screen_width+i,1047))
            i=0
        i-=1
        # gets cursor coordinates
        mouse = pygame.mouse.get_pos() 
        # if mouse is hovered.....
        if width-740 <= mouse[0] <= width-600 and height/2+80 <= mouse[1] <= height/2+180:          #...on quit
            game_screen.blit(bgmain, (0, 0))
            game_screen.blit(startimg, (1000, 250))
            game_screen.blit(quitimgResized, (1050, 525))
            game_screen.blit(credits,(i,0))
            game_screen.blit(credits,(i,1047))
            game_screen.blit(credits,(screen_width+i,0))
            game_screen.blit(credits,(screen_width+i,1047))
            if (i==-screen_width):
                game_screen.blit(credits,(screen_width+i,0))
                game_screen.blit(credits,(screen_width+i,1047))
                i=0
            i-=1
        elif width-840 <= mouse[0] <= width-500 and height/2-170 <= mouse[1] <= height/2-60:        #...on start
            game_screen.blit(bgmain, (0, 0))
            game_screen.blit(startimgResized, (950, 220))
            game_screen.blit(quitimg, (1100, 550))
            game_screen.blit(credits,(i,0))
            game_screen.blit(credits,(i,1047))
            game_screen.blit(credits,(screen_width+i,0))
            game_screen.blit(credits,(screen_width+i,1047))
            if (i==-screen_width):
                game_screen.blit(credits,(screen_width+i,0))
                game_screen.blit(credits,(screen_width+i,1047))
                i=0
            i-=1

        
        # update pygame display
        pygame.display.update()    
def main():

    #Player initialization
    player = pygame.transform.scale((pygame.image.load(os.path.join(im, 'pin1.png'))), (93/2, 139/2))
    x = 1
    y = 1
    
    # Initialize balloons list
    balloons = []

    # Initialize score and timer
    score = 0
    time_left = 60 # in seconds
    total_time = 60
    add_time = 0
    append_time = 0
    
    # bgm and sound setup
    pygame.mixer.music.play(-1)
    pop.set_volume(1)
    pygame.mixer.music.set_volume(0.2)

    # Game loop
    running = True
    start_time = pygame.time.get_ticks() // 1000
    
    i = 0
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    start()
            if event.type == pygame.QUIT:
                running = False
        
        # Pygame screen setup
        game_screen.blit(bg, (0, 0))

        # Capture video frame
        ret, frame = cap.read()

        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)

        # Convert the BGR frame to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands
        results = hands.process(rgb)

        # Draw balloons
        for balloon in balloons:
            balloon.move()
            if balloon.y < -balloon.radius:
                balloons.remove(balloon)
            if not balloon.popped:
                balloon.draw()

        # Pop balloons on finger inside
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                x, y = int(index_finger_tip.x * screen_width), int(index_finger_tip.y * screen_height)
                for balloon in balloons:
                    if not balloon.popped and (balloon.x - x)**2 + (balloon.y - y)**2 <= balloon.radius**2:
                        balloon.popped = True
                        pygame.mixer.Sound.play(pop)
                        score += 1
                        balloon.y = 0 - balloon.radius
                        
                #Display finger position
                pygame.draw.circle(game_screen, (255, 0, 0), (x, y), 2)
            
        image_rect = player.get_rect()
        image_rect.x = x - player.get_height()/2 - 2
        image_rect.y = y - player.get_width() - 11                
        game_screen.blit(player, image_rect)
        
        # Spawn new balloons
        if random.randint(0, 18) == 0:
            balloons.append(Balloon())

        # Display score
        score_text = titlefont.render("Score:" + str(score), True, (255, 0, 0))
        game_screen.blit(score_text, (10, 10))

        # Display timer
        timer = (pygame.time.get_ticks() // 1000)
        time_elapsed = timer - start_time
        # total_time = 60
                      
        time_left = total_time - time_elapsed + append_time
            
            # total_time -= time_elapsed
        for balloon in balloons:
            if balloon.popped == True and balloon.time() != 0:
                while add_time > -5 and add_time < 3:
                    add_time += balloon.time()
                    balloons.remove(balloon)
                    # print(f"Add time: {add_time}")
                    
            elif add_time!=0:
                append_time+=add_time   
                add_time = 0
                # print(f"Append time: {append_time}")
            
        if time_left <= 10:
            image.set_alpha(i)
            image2.set_alpha(i)

            game_screen.fill((150, 0, 0))
            game_screen.blit(backgroundimg, backgroundimg.get_rect())
            game_screen.blit(image, rect)
            game_screen.blit(image2, rect2)

            for balloon in balloons:
                if balloon.popped:
                    balloons.remove(balloon)
                else:
                    balloon.draw()
                    pygame.draw.circle(game_screen, (255, 0, 0), (x, y), 2)
                    game_screen.blit(player, image_rect)
                    game_screen.blit(score_text, (10, 10))
            
            if i == 255:
                i = 0
                pygame.time.delay(60)
            else:
                i += 5
        if time_left <= 0:
            game_screen.blit(pygame.image.load('Images\\jumpscare2.png'), (0, 0))
            game_screen.blit(pygame.image.load('Images\\gameover.png'), (0, 0))
            game_screen.blit(score_text, (800, 700))
            pygame.mixer.Sound.play(gameoversfx)
            pygame.display.update()
            pygame.time.delay(3000) # wait for 3 seconds before exiting the game
            running = False
        
        time_text = titlefont.render("Time: " + str(time_left), True, (255, 0, 0))
        game_screen.blit(time_text, (1280/2, 10))
        game_screen.blit(text, (width-255,height-700))
        # Update the Pygame display
        pygame.display.update()

start()
# Release the video capture
cap.release()

# Close Pygame
pygame.quit()
