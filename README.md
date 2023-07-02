# boilerplate-pygame-sql

Plantilla base para crear juegos con persistencia.

## Sinopsis del juego

Es una version simplificada del juego asteroids.

- No hay disparos
- Se controla con el mouse
- Solo hay dos objetos (asteriode y nave)
- La nave debe esquivar los asteroides
- El puntaje se incrementa con el tiempo, hasta que la nave es impactada por un asteroide o se cierra el juego
- La base de datos consta solamente de una tabla (scores) y un campo "score"

## Instalacion

Deben instalar desde la consola la libreria Pygame (asegurense de tener actualizado PIP)

```bash
pip install -Ur .\requirements.txt 
```

- En el archivo 'requirements.txt' se encuentra la libreria listada

## Scaffolding (organizacion de carpetas)

```bash
.
├───db
│   ├────asteroids.db
│   └────init.sql
├───objects
│   ├────asteroid.py
│   └────ship.py
├───.gitignore
├───config.py
├───main.py
├───README.md
└───requirements.txt
```

## Uso

Como cualquier script o programa de python.

```bash
python "main.py"
```

*Para correrlo sin mencionar el directorio, la consola debe estar posicionada sobre la carpeta del proyecto.
