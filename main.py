import pygame


WIDTH = 1920
HEIGHT = 1080

SPRITE_WIDTH = 128
SPRITE_HEIGHT = 128
halfscale=2
pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Renderizar Spritesheet")

spritesheet = pygame.image.load("./Spritesheets/spritesheet_tiles.png").convert()
scaledSpriteSheet = pygame.transform.scale(spritesheet,((spritesheet.get_width()/halfscale),(spritesheet.get_height()/halfscale)))

sprite_rect = pygame.Rect(0, 0, SPRITE_WIDTH/halfscale, SPRITE_HEIGHT/halfscale)
sprite_rectt = pygame.Rect(0, 0, SPRITE_WIDTH, SPRITE_HEIGHT)
# Variable para controlar el bucle principal
running = True

# Bucle principal
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la ventana
    window.fill((0, 0, 0))

    # Renderizar la sección de la spritesheet en la ventana
    window.blit(scaledSpriteSheet, (0, 0), sprite_rect)
    window.blit(spritesheet, (64, 0), sprite_rectt)
    # Actualizar la ventana
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
