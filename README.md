# 🌸 Flor Animada — Python + Pygame

Una pequeña animación desarrollada con **Python y Pygame** en la que una flor se va formando progresivamente desde el tallo hasta los pétalos. Al finalizar la animación aparece el mensaje **"Te amo"**.

El proyecto está pensado como un ejemplo sencillo de **animación 2D, geometría, dibujo de figuras y manejo de eventos con Pygame**.

---

## ✨ Características

* 🌱 Crecimiento animado del tallo.
* 🍃 Aparición progresiva de las hojas.
* 🌸 Creación de los pétalos uno por uno.
* 🌼 Animación del centro de la flor.
* ❤️ Aparición progresiva del mensaje **"Te amo"**.
* 🔄 Posibilidad de reiniciar la animación.
* ⌨️ Control mediante teclado.
* 🖥️ Ventana gráfica creada con Pygame.
* 🧮 Uso de trigonometría para construir los pétalos.

---

## 🛠️ Tecnologías utilizadas

* **Python 3**
* **Pygame**
* `math`

No se utilizan imágenes externas; la flor se genera mediante código utilizando figuras geométricas.

---

## 📂 Estructura del proyecto

```text
flor-te-amo/
│
├── flor_te_amo.py
└── README.md
```

---

## ⚙️ Requisitos

Necesitas tener instalado:

* Python 3
* Pygame

Puedes comprobar tu versión de Python con:

```bash
python3 --version
```

---

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/flor-te-amo.git
```

Entrar al proyecto:

```bash
cd flor-te-amo
```

### 2. Instalar Pygame

```bash
pip3 install pygame
```

Si utilizas un entorno virtual, es recomendable instalarlo dentro del entorno:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pygame
```

---

## ▶️ Ejecutar el programa

Ejecuta:

```bash
python3 flor_te_amo.py
```

Se abrirá una ventana donde comenzará la animación.

---

## 🎮 Controles

| Tecla          | Acción                 |
| -------------- | ---------------------- |
| `R`            | Reiniciar la animación |
| `ESC`          | Salir del programa     |
| Cerrar ventana | Salir                  |

---

## 🧠 ¿Cómo funciona?

La animación está construida utilizando coordenadas, trigonometría y primitivas gráficas de Pygame.

### 🌱 Tallo

El tallo se dibuja progresivamente desde la parte inferior de la pantalla hasta llegar a la flor.

```python
pygame.draw.line(
    pantalla,
    TALLO,
    (CX, y_base),
    (CX, y_actual),
    12
)
```

### 🌸 Pétalos

Los pétalos se construyen utilizando puntos calculados mediante `sin()` y `cos()`.

```python
x = math.sin(t) * ancho
y = -math.cos(t) * longitud
```

Posteriormente los puntos son rotados alrededor del centro de la flor.

Esto permite crear los diferentes pétalos sin necesidad de utilizar imágenes.

### 🌼 Centro

El centro de la flor utiliza círculos y pequeños puntos decorativos:

```python
pygame.draw.circle(
    pantalla,
    CENTRO,
    (CX, CY),
    radio
)
```

### ❤️ Mensaje

Cuando la flor está suficientemente desarrollada, aparece progresivamente:

```text
Te amo
```

La transparencia del texto aumenta gradualmente para crear un efecto de aparición suave.

---

## 🎨 Personalización

Puedes modificar fácilmente los colores desde la sección de configuración:

```python
FONDO = (18, 12, 24)
PETALO = (245, 105, 155)
PETALO_CLARO = (255, 145, 185)
CENTRO = (255, 205, 70)
TALLO = (70, 170, 90)
HOJA = (75, 185, 105)
BLANCO = (255, 255, 255)
```

También puedes cambiar el mensaje:

```python
texto = fuente_amor.render("Te amo", True, BLANCO)
```

Por ejemplo:

```python
texto = fuente_amor.render("Te quiero ❤️", True, BLANCO)
```

---

## 🚀 Posibles mejoras

Este proyecto puede ampliarse fácilmente con:

* 💕 Corazones flotando alrededor de la flor.
* ✨ Partículas y efectos de brillo.
* 🌙 Fondo nocturno animado.
* 🌧️ Efecto de lluvia.
* 🎵 Música de fondo.
* 🌹 Diferentes tipos de flores.
* 🌈 Cambio dinámico de colores.
* 🖱️ Interacción con el mouse.
* ⏱️ Diferentes velocidades de crecimiento.
* 💌 Mensajes personalizados.
* 🎆 Efectos de partículas al terminar la animación.

---

## 📚 Conceptos utilizados

Este proyecto permite practicar:

* Programación con Python.
* Pygame.
* Bucles de animación.
* Coordenadas `X/Y`.
* Trigonometría.
* `sin()` y `cos()`.
* Rotación de puntos.
* Figuras geométricas.
* Renderizado 2D.
* Transparencia.
* Manejo de eventos.
* Control de FPS.
* Funciones y modularización.

---

## 📸 Resultado

Al ejecutar el programa se observa una flor que comienza a crecer desde el tallo, desarrolla sus hojas y posteriormente crea sus pétalos.

Finalmente aparece:

```text
        🌸
       🌸🌸
      🌸🌼🌸
       🌸🌸
        🌿
        🌿

      Te amo
```

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica de **Python y animación 2D con Pygame**.

---

## 📄 Licencia

Este proyecto puede utilizarse libremente con fines educativos y personales.

Si utilizas o modificas el proyecto, puedes agregar tus propios cambios y atribuciones.
