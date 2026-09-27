import pygame
import math

# =========================
# CONFIGURACIÓN
# =========================

pygame.init()

ANCHO = 900
ALTO = 700

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Figura geométrica animada")

reloj = pygame.time.Clock()

# Colores
FONDO = (15, 18, 25)
BLANCO = (240, 240, 240)

# Centro y tamaño
CENTRO = (ANCHO // 2, ALTO // 2)
RADIO = 220

# Velocidad de cambio de lados
VELOCIDAD_CAMBIO = 1.5

# Velocidad de rotación
VELOCIDAD_ROTACION = 0.8


# =========================
# FUNCIÓN PARA CREAR FIGURA
# =========================

def crear_poligono(lados, centro, radio, rotacion):
    puntos = []

    for i in range(lados):

        angulo = (
            2 * math.pi * i / lados
            + rotacion
            - math.pi / 2
        )

        x = centro[0] + math.cos(angulo) * radio
        y = centro[1] + math.sin(angulo) * radio

        puntos.append((x, y))

    return puntos


# =========================
# VARIABLES DE ANIMACIÓN
# =========================

# Comenzamos con 9 lados
lados_actuales = 9.0

# Dirección:
# -1 = disminuyendo
#  1 = aumentando
direccion = -1

rotacion = 0


# =========================
# BUCLE PRINCIPAL
# =========================

ejecutando = True

while ejecutando:

    # -------------------------
    # EVENTOS
    # -------------------------

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:
                ejecutando = False


    # -------------------------
    # ACTUALIZAR ANIMACIÓN
    # -------------------------

    lados_actuales += (
        direccion
        * VELOCIDAD_CAMBIO
        * (1 / 60)
    )

    # Llegamos al triángulo
    if lados_actuales <= 3:
        lados_actuales = 3
        direccion = 1

    # Llegamos nuevamente al eneágono
    elif lados_actuales >= 9:
        lados_actuales = 9
        direccion = -1


    # Rotación
    rotacion += (
        math.radians(VELOCIDAD_ROTACION)
    )


    # -------------------------
    # DIBUJAR
    # -------------------------

    pantalla.fill(FONDO)

    # Convertimos a entero para
    # dibujar una cantidad válida de lados
    lados = round(lados_actuales)

    puntos = crear_poligono(
        lados,
        CENTRO,
        RADIO,
        rotacion
    )

    # Dibujar polígono
    pygame.draw.polygon(
        pantalla,
        BLANCO,
        puntos,
        width=5
    )

    # Dibujar vértices
    for punto in puntos:

        pygame.draw.circle(
            pantalla,
            BLANCO,
            (int(punto[0]), int(punto[1])),
            7
        )


    # -------------------------
    # TEXTO
    # -------------------------

    fuente = pygame.font.Font(None, 42)

    texto = fuente.render(
        f"{lados} lados",
        True,
        BLANCO
    )

    rectangulo = texto.get_rect(
        center=(ANCHO // 2, 80)
    )

    pantalla.blit(
        texto,
        rectangulo
    )


    # -------------------------
    # ACTUALIZAR PANTALLA
    # -------------------------

    pygame.display.flip()

    reloj.tick(60)


pygame.quit()