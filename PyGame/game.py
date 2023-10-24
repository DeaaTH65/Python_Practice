import pygame

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('PyGame')
clock = pygame.time.Clock()
running = True


dt = 0
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Screen color
    screen.fill('grey')
    
    # Draw line
    pygame.draw.line(screen, 'black', (0, 500), (800, 50), 2)
    
    pygame.draw.circle(screen, 'blue', player_pos, 40)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
        
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
        
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
        
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
        
    
    # Use mouse
    if pygame.mouse.get_pressed()[0]:
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            player_pos.x = pos[0]
            player_pos.y = pos[1]
        
        
        
    # # Use mouse
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     pos = pygame.mouse.get_pos()
    #     player_pos.x = pos[0]
    #     player_pos.y = pos[1]
        
    # if event.type == pygame.MOUSEBUTTONUP:
    #     pos = pygame.mouse.get_pos()
    #     pygame.draw.circle(screen, "red", player_pos, 40)
        
    # # Motion
    # if event.type == pygame.MOUSEMOTION:
    #     pos = pygame.mouse.get_pos()
    #     player_pos.x = pos[0]
    #     player_pos.y = pos[1]
        
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    


pygame.quit()