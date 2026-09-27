import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
reloj = pygame.time.Clock()

x = 100
velocidad = 3

ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    x += velocidad

    if x >= 700 or x <= 100:
        velocidad *= -1

    pantalla.fill((30, 30, 30))

    pygame.draw.line(
        pantalla,
        (255, 255, 255),
        (x, 200),
        (x, 400),
        5
    )

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()