import pygame
import math

pygame.init()

# =========================
# CONFIGURACIÓN
# =========================

ANCHO = 900
ALTO = 700

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Una flor para ti")

reloj = pygame.time.Clock()

# Colores
FONDO = (18, 20, 30)
PETALO = (255, 105, 180)
PETALO_CLARO = (255, 150, 205)
CENTRO = (255, 210, 60)
TALLO = (70, 180, 90)
HOJAS = (50, 150, 75)
BLANCO = (255, 255, 255)

# Centro de la flor
CX = ANCHO // 2
CY = 280

# Configuración de pétalos
NUM_PETALOS = 12
RADIO_PETALO = 115

# Animación
petalos_creados = 0
tiempo = 0

# Fuentes
fuente_grande = pygame.font.Font(None, 80)
fuente_pequena = pygame.font.Font(None, 35)


# =========================
# FUNCIÓN PARA DIBUJAR PÉTALO
# =========================

def dibujar_petalo(superficie, x, y, angulo, escala):
    ancho = 45 * escala
    alto = 120 * escala

    # Creamos el pétalo en una superficie independiente
    petalo = pygame.Surface(
        (ancho * 2 + 20, alto * 2 + 20),
        pygame.SRCALPHA
    )

    centro = (
        petalo.get_width() // 2,
        petalo.get_height() // 2
    )

    # Elipse del pétalo
    pygame.draw.ellipse(
        petalo,
        PETALO,
        (
            centro[0] - ancho / 2,
            centro[1] - alto / 2,
            ancho,
            alto
        )
    )

    # Pequeño brillo
    pygame.draw.ellipse(
        petalo,
        PETALO_CLARO,
        (
            centro[0] - ancho * 0.25,
            centro[1] - alto * 0.35,
            ancho * 0.25,
            alto * 0.25
        )
    )

    # Girar el pétalo
    petalo = pygame.transform.rotate(
        petalo,
        -math.degrees(angulo)
    )

    rect = petalo.get_rect(center=(x, y))

    superficie.blit(petalo, rect)


# =========================
# FUNCIÓN PARA DIBUJAR TALLO
# =========================

def dibujar_tallo():
    pygame.draw.line(
        pantalla,
        TALLO,
        (CX, CY + 80),
        (CX, 610),
        12
    )

    # Hoja izquierda
    pygame.draw.ellipse(
        pantalla,
        HOJAS,
        (CX - 130, 460, 140, 55)
    )

    # Hoja derecha
    pygame.draw.ellipse(
        pantalla,
        HOJAS,
        (CX - 10, 500, 140, 55)
    )


# =========================
# BUCLE PRINCIPAL
# =========================

ejecutando = True

while ejecutando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

    # Tiempo
    tiempo += 1

    pantalla.fill(FONDO)

    # =========================
    # TALLO
    # =========================

    dibujar_tallo()

    # =========================
    # CREAR PÉTALOS
    # =========================

    if petalos_creados < NUM_PETALOS:

        if tiempo % 15 == 0:
            petalos_creados += 1

    for i in range(petalos_creados):

        angulo = (
            2 * math.pi * i / NUM_PETALOS
            - math.pi / 2
        )

        # Animación de crecimiento
        if i == petalos_creados - 1:
            escala = min(
                1,
                (tiempo % 15) / 15
            )
        else:
            escala = 1

        x = CX + math.cos(angulo) * RADIO_PETALO
        y = CY + math.sin(angulo) * RADIO_PETALO

        dibujar_petalo(
            pantalla,
            x,
            y,
            angulo,
            escala
        )

    # =========================
    # CENTRO DE LA FLOR
    # =========================

    if petalos_creados >= NUM_PETALOS:

        pygame.draw.circle(
            pantalla,
            CENTRO,
            (CX, CY),
            65
        )

        # Semillas
        for i in range(18):

            angulo = i * 2.4

            distancia = 25 + (i % 3) * 10

            x = CX + math.cos(angulo) * distancia
            y = CY + math.sin(angulo) * distancia

            pygame.draw.circle(
                pantalla,
                (180, 130, 30),
                (int(x), int(y)),
                4
            )

    # =========================
    # MENSAJE
    # =========================

    if petalos_creados >= NUM_PETALOS:

        texto = fuente_grande.render(
            "Te amo ❤️",
            True,
            BLANCO
        )

        rect = texto.get_rect(
            center=(CX, 650)
        )

        pantalla.blit(
            texto,
            rect
        )

    else:

        texto = fuente_pequena.render(
            "Una flor para ti...",
            True,
            BLANCO
        )

        rect = texto.get_rect(
            center=(CX, 650)
        )

        pantalla.blit(
            texto,
            rect
        )

    pygame.display.flip()

    reloj.tick(60)


pygame.quit()