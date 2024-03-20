import pygame
import sys

pygame.init()

#Display
width, height = 800, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("CAT")

# Background Music
pygame.mixer.music.load("CATT.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)


#Load image
cat_image = pygame.image.load("CAT2.jpg")

cat_rect = cat_image.get_rect()

#Position and speed
cat_rect.x = 100
cat_rect.y = 100
speed = [5, 5] #[X speed, Y speed]

#Trail
trail_color = (255, 0, 0)
trail_positions = []



#Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #update cat position
    cat_rect.x += speed[0]
    cat_rect.y += speed[1]
   
    #Bounce screen edges
    if cat_rect.left < 0 or cat_rect.right > width:
        speed[0] = -speed[0]
    if cat_rect.top < 0 or cat_rect.bottom > height:
        speed[1] = -speed[1]
       
    #Record cat position for list
    trail_positions.append((cat_rect.x, cat_rect.y))
   
    #Draw trail
    for pos in trail_positions:
        pygame.draw.circle(screen, trail_color, (pos[0], pos[1]), 5)
     
    screen.fill((230, 230, 250))
   
    #Draw cat
    screen.blit(cat_image, cat_rect)
   
    #Update display
    pygame.display.flip()
   
    #Fram rate
    pygame.time.Clock().tick(30)
