# Proyecto HCI: Control Bluetooth para Carrito y Juego de Laberinto

Este proyecto abarca dos módulos principales:

1. **Control remoto por Bluetooth para un carrito con ESP32**  
   Sistema para controlar un carrito mediante comandos Bluetooth enviados desde una app móvil desarrollada con MIT App Inventor.

2. **Juego de laberinto en MIT App Inventor**  
   Un juego móvil con interfaz gráfica donde el jugador controla un sprite dentro de un laberinto evitando paredes y obstáculos.

---

## Funcionalidades

### Control Bluetooth para carrito
- Comunicación Bluetooth con ESP32 para enviar comandos.  
- Movimientos: avanzar, retroceder, girar izquierda/derecha, detenerse.  
- App móvil con botones para control remoto.

### Juego de laberinto
- Canvas con ImageSprite que representa al jugador.  
- Colisiones para evitar atravesar paredes.  
- Múltiples niveles con transición entre pantallas.  
- Control táctil para mover el sprite.

---

## Tecnologías usadas

- ESP32 (Arduino IDE)  
- Bluetooth Serial  
- MIT App Inventor (app móvil y juego)  
- Diseño de interfaces en MIT App Inventor  

---

## Instalación y uso

### Carrito Bluetooth
1. Programar el ESP32 con el código fuente usando Arduino IDE.  
2. Instalar la app móvil desde MIT App Inventor o APK.  
3. Emparejar Bluetooth y usar los controles para mover el carrito.

### Juego de laberinto
1. Abrir el proyecto en MIT App Inventor.  
2. Ejecutar en un emulador o dispositivo móvil.  
3. Navegar por el laberinto usando controles táctiles.

---

## Estructura del proyecto

- `carrito/` — Código del ESP32 para control Bluetooth.  
- `app/` — Proyecto de MIT App Inventor para controlar el carrito.  
- `juego_laberinto/` — Proyecto MIT App Inventor con el juego de laberinto.  

---

## Notas y consideraciones

- Se está trabajando en mejorar la estabilidad de la conexión Bluetooth para evitar desconexiones inesperadas.  
- El juego puede ampliarse con más niveles y funcionalidades.  

---

## Licencia

MIT License
