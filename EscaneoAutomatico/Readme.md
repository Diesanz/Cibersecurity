# fsociety – Menú de Escaneo Automático (EscaneoAutomatico)

Menú interactivo en Python que orquesta escaneos de seguridad con Nmap y ataques de fuerza bruta con Hydra, a través de dos utilidades incluidas en este proyecto:
- nmap/nmap2.py: automatiza múltiples perfiles de escaneo con Nmap.
- hydra/hydra.py: facilita ataques de autenticación con Hydra en distintos servicios.

El lanzador principal es shell.py, que muestra un menú “fsociety” para ejecutar cada herramienta.

## Características
- Interfaz interactiva con menú de opciones.
- Permite modificar el comando antes de ejecutarlo (pre-relleno en la línea de comandos).
- Colores en consola mediante colorama y banner con pyfiglet.
- Manejo de errores y control de interrupciones (Ctrl+C).

## Estructura
```
EscaneoAutomatico/
├─ shell.py                 # Lanzador fsociety (menú)
├─ nmap/
│  ├─ nmap2.py             # Automatización de Nmap
│  └─ ayuda_nmap.py        # Ayuda de comandos Nmap
└─ hydra/
   ├─ hydra.py             # Automatización de Hydra
   └─ ayuda_hydra.py       # Ayuda de comandos Hydra
```

## Requisitos
- Python 3.8+
- Paquetes Python:
  - colorama
  - pyfiglet
  - readline (UNIX). En Windows usar pyreadline3
- Herramientas del sistema instaladas y en PATH:
  - nmap
  - hydra

Instalación rápida (Python):
```bash
pip install colorama pyfiglet
# Windows (solución a readline)
pip install pyreadline3
```
Instalación de herramientas del sistema:
- Linux (Debian/Ubuntu):
```bash
sudo apt update && sudo apt install nmap hydra
```
- macOS (Homebrew):
```bash
brew install nmap hydra
```
- Windows: se recomienda usar WSL. Nmap tiene instalador nativo; Hydra suele requerir WSL/Cygwin.

## Uso
Desde la carpeta EscaneoAutomatico:
```bash
python shell.py
```
El menú permite:
1) Ejecutar Nmap (nmap/nmap2.py)
2) Ejecutar Hydra (hydra/hydra.py)
Escriba "exit" para salir y "main" para limpiar pantalla y volver al menú.

También puede ejecutar directamente cada módulo:
```bash
python nmap/nmap2.py
python hydra/hydra.py
```

Nota sobre rutas/Windows: el menú interno usa comandos "python3 /EscaneoAutomatico/..." pensados para UNIX. Si en su entorno no se lanzan los subprogramas desde el menú, ejecute los módulos directamente como se muestra arriba o edite el diccionario programs en shell.py para que use:
- "python nmap/nmap2.py"
- "python hydra/hydra.py"

## Ejemplos
- Nmap: selección de escaneos como -A, -sS, --top-ports, --script=vuln, etc. Con posibilidad de editar el comando antes de ejecutarlo.
- Hydra: ataques predefinidos para SSH, FTP, HTTP Basic, RDP, MySQL, VNC, SMB, Telnet o un comando personalizado.

## Solución de problemas
- ModuleNotFoundError: readline (Windows)
  - Instale pyreadline3: `pip install pyreadline3`
- "nmap: command not found" / "hydra: command not found"
  - Instale las herramientas del sistema y verifique que están en PATH.
- Permisos requeridos
  - Algunos escaneos pueden requerir privilegios elevados (sudo en Linux/macOS).

## Advertencia legal
Este proyecto es únicamente para fines educativos y pruebas en entornos controlados. No ejecute estas herramientas sobre sistemas sin autorización expresa. El uso indebido puede ser ilegal.
