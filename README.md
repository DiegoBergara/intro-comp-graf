# Proyecto Introducción Computación Gráfica 

### Descripción

Implementacion de un juego donde se utilizan los conceptos adquieridos en el curso de Introducción a la Computación Gráfica.

### Instalación

Para la instalación es necesario tener instaladas las librerias que se encuentran en `requirements.txt`. Para esto re recomienda utilizar `Virtualenv` u otro entorno virtual, también es necesario `python` verion 3.8+ con su correspondiente versión de `pip`.

Los pasos a seguir son:

- Abrir la consola
- Entrar en el entorno virtual (opcional)
- navegar hacia la carpeta `Proyecto`
- Introducir el siguiente comando: `pip install -r requirements.txt`
 
 ### Iniciar juego
 
 Una vez terminada la instalación en la misma consola introducir: `python main.py`. 
 
 El resultado de esto debería ser:
 
![image](https://github.com/DiegoBergara/intro-comp-graf/blob/master/assets/game.png)


### Controles

- Movimiento: A,S,W,D
- Saltar: SPACE
- Atacar: Click izquierdo
- Segundo Ataque: Click derecho
- Regular cámara: scroll wheel
- Animación 1: 1
- Animación 2: 2
- Cambiar Cielo: 3
- Salir: Esc

### Features

- Se agregaron sonidos para las acciones
- Se utiliza un archivo de configuración para las texturas, objetos y sonidos
- Se utiliza glShadeModel(GL_SMOOTH)
- Movimientos de camara libre con foco en el knight
