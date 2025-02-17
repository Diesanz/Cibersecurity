# fsociety - Menú de Escaneo Automático

Este proyecto es un menú interactivo en Python que permite ejecutar herramientas de escaneo de seguridad de forma automatizada. Utiliza `nmap` y `hydra` como herramientas principales para la auditoría de redes y pruebas de fuerza bruta.

## Características

- **Interfaz interactiva** con opciones de selección de comandos.
- **Ejecución automática** de scripts de `nmap` y `hydra`.
- **Historial de comandos** con soporte para Linux/Mac.
- **Formato visual mejorado** gracias a `pyfiglet` y `colorama`.
- **Manejo de errores** y salida en colores para facilitar la lectura.

## Instalación y Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install pyfiglet colorama
```

Además, asegúrate de que `nmap` y `hydra` estén correctamente instalados en tu sistema.

## Uso

Para ejecutar el script, simplemente corre el siguiente comando:

```bash
python3 fsociety.py
```

### Opciones disponibles:

1. **Ejecutar `nmap_fsociety`**
2. **Ejecutar `hydra_fsociety`**
3. **Escribir `exit` para salir**
4. **Escribir `main` para limpiar la pantalla y volver al menú**

### Ejemplo de Uso

```bash
set> 1
Ejecutando python3 /home/diego/Escritorio/Programas/EscaneoAutomatico/nmap/nmap2.py...
```

```bash
set> 2
Ejecutando python3 /home/diego/Escritorio/Programas/EscaneoAutomatico/hydra/hydra.py...
```

## Notas Adicionales

- Si el usuario interrumpe el programa (`Ctrl + C`), el script manejará la interrupción y saldrá de manera controlada.
- Si se introduce un comando inválido, se mostrará un mensaje de error en rojo.

## Licencia

Este proyecto está desarrollado con fines educativos y de práctica. Úsalo bajo tu propia responsabilidad.
