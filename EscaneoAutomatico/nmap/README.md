# Automatización de Nmap

Este script permite ejecutar distintos tipos de escaneos con Nmap de forma automatizada, proporcionando una interfaz interactiva para seleccionar opciones de escaneo y modificar los comandos antes de su ejecución.

## Características
- Menú interactivo con múltiples opciones de escaneo.
- Modificación de comandos antes de ejecutarlos.
- Uso de `colorama` para mejorar la visualización en la terminal.
- Soporte para técnicas avanzadas de evasión y detección de firewalls.
- Integración con `ayuda_nmap` para mostrar información detallada.

## Requisitos
Este script requiere las siguientes dependencias:
- Python 3.x
- `colorama` (para colores en la terminal)
- `readline` (para edición de línea de comandos en UNIX)
- `nmap` instalado en el sistema

Para instalar las dependencias de Python:
```bash
pip install colorama
sudo apt install nmap
```

## Uso
```bash
python nmap_automation.py
```
Se mostrará un menú con diversas opciones de escaneo. SOlo tienes que seleccionar la opción deseada y proporcionar la IP o rango de IPs a escanear.

## Ejemplo de ejecución
```bash
🔍 Automatización de Nmap

Opciones disponibles:
1. Escanear IP o rango de IPs
2. Escaneo rápido de host y servicios (-T4)
3. Escaneo de puertos más utilizados (--top-ports)
...
Selecciona una opción, teclea 21 para ver de nuevo las opciones: 6
Introduce IP o rango de IPs: 192.168.1.1
Ejecutando: nmap -A 192.168.1.1
```

## Modificar comandos 
Antes de ejecutar un escaneo, el script te permite modificar el comando predefinido para personalizarlo según tus necesidades.

## Advertencia
Este script está diseñado para pruebas de seguridad en entornos controlados. No lo uses en sistemas sin permiso explícito. El uso indebido de este software puede ser ilegal.