import sys
from colorama import Fore, Style, init

# Diccionario con los comandos y sus descripciones para Hydra
COMANDOS = {
    "1": ("Ataque SSH con diccionario de contraseñas", "hydra -l <usuario> -P <diccionario.txt> ssh://<IP>"),
    "2": ("Ataque FTP con diccionario de usuarios y contraseñas", "hydra -L <usuarios.txt> -P <contraseñas.txt> ftp://<IP>"),
    "3": ("Ataque HTTP Basic Authentication", "hydra -L <usuarios.txt> -P <contraseñas.txt> http://<IP> -m <ruta_protegida>"),
    "4": ("Ataque RDP (Escritorio remoto)", "hydra -L <usuarios.txt> -P <contraseñas.txt> rdp://<IP>"),
    "5": ("Ataque MySQL con diccionario", "hydra -L <usuarios.txt> -P <contraseñas.txt> mysql://<IP>"),
    "6": ("Ataque a formulario web (POST)", "hydra -L <usuarios.txt> -P <contraseñas.txt> <IP> http-post-form /ruta_login:user=^USER^&pass=^PASS^:F=incorrecto"),
    "7": ("Ataque contra VNC", "hydra -P <contraseñas.txt> vnc://<IP>"),
    "8": ("Ataque contra SMB (Windows File Sharing)", "hydra -L <usuarios.txt> -P <contraseñas.txt> smb://<IP>"),
    "9": ("Ataque contra Telnet", "hydra -L <usuarios.txt> -P <contraseñas.txt> telnet://<IP>"),
    "10": ("Salir", "Finaliza el programa.")
}

def mostrar_help():
    """Muestra la ayuda del programa con la descripción de los comandos de Hydra"""
    print(Fore.CYAN + "\nUso: python script.py [opción]\n")
    print(Fore.YELLOW + "Opciones disponibles:")
    for key, (descripcion, ejemplo) in COMANDOS.items():
        print(Fore.GREEN + f"{key}. {descripcion}")
        print(Fore.LIGHTBLACK_EX + f"   Ejemplo: {ejemplo}\n")
    print(Fore.CYAN + "También puedes ejecutar el programa sin argumentos para interactuar con el menú.")

# Si ejecutamos el script con el argumento '-h' o '--help'
if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
    mostrar_help()
