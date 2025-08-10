# Proyecto HCI: Control Bluetooth para Carrito con ESP32

Este proyecto implementa un sistema de control remoto por Bluetooth para un carrito usando un microcontrolador ESP32. La comunicación Bluetooth recibe comandos desde una app móvil (creada con MIT App Inventor) que controla el movimiento del carrito.

---

## Funcionalidades

- Conexión Bluetooth con ESP32.  
- Comandos para mover el carrito: avanzar, retroceder, izquierda, derecha, parar, etc.  
- App móvil con botones para controlar el carrito en tiempo real.  
- Manejo básico de desconexiones y reconexiones Bluetooth.  

---

## Tecnologías usadas

- Microcontrolador ESP32.  
- Bluetooth Serial (BLE o clásico).  
- MIT App Inventor para la app móvil.  
- Arduino IDE o PlatformIO para programación ESP32.  

---

## Instalación y uso

1. Cargar el código fuente al ESP32 usando Arduino IDE.  
2. Instalar la app móvil en un teléfono Android (archivo APK o a través de MIT App Inventor).  
3. Emparejar el teléfono con el ESP32 vía Bluetooth.  
4. Usar los botones en la app para controlar el carrito.  

---

## Estructura del código

- `main.ino` o archivo principal del ESP32 con la lógica Bluetooth y movimiento.  
- `app.aia` proyecto de MIT App Inventor (opcional para distribución).  

---

## Consideraciones

- La conexión Bluetooth puede desconectarse si se envían comandos específicos (por ejemplo, 'A' y 'B'), se está trabajando en la depuración.  
- El código puede ser ampliado para soporte de más comandos o sensores adicionales.  

---

## Licencia

MIT License (u otra si tienes preferencia)  

