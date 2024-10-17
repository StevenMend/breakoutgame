# Breakout Game

## Descripción
El juego Breakout es un clásico juego de arcade en el que el objetivo es destruir todos los bloques en la pantalla utilizando una pelota que rebota. El jugador controla una paleta que se mueve de izquierda a derecha para evitar que la pelota caiga. Al golpear los bloques, se eliminan y el jugador gana puntos.

## Características
- Jugabilidad intuitiva y adictiva.
- Gráficos simples y atractivos.
- Puntuaciones más altas para incentivar la competencia.

## Requisitos
- Python 3.x
- Pygame

## El código del juego Breakout está diseñado utilizando la biblioteca Pygame y se organiza en secciones que gestionan la inicialización, la configuración de la pantalla, el movimiento de la barra y la pelota, las colisiones, y la lógica del juego. Al inicio, se importan las bibliotecas necesarias y se inicializa Pygame, configurando una ventana de 600x400 píxeles y definiendo una paleta de colores. Se establece la velocidad del juego y se inicializan variables para la barra (paddle), la pelota y los bloques, incluyendo sus dimensiones y posiciones. Las funciones move_paddle() y move_ball() controlan el movimiento de la barra y la pelota, manejando colisiones con los bordes de la pantalla y la barra, así como el rebote de la pelota. La función check_collisions() verifica si la pelota colisiona con los bloques, eliminándolos de la pantalla al ser golpeados. La función reset_ball() reinicia la posición de la pelota en el centro de la pantalla cuando cae. La lógica principal del juego se encuentra en un bucle que actualiza la pantalla, dibuja todos los elementos, y gestiona las entradas del usuario, incluyendo el control de vidas y la visualización de una pantalla de "Game Over" cuando se pierden todas las vidas.
