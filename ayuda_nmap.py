import sys
from colorama import Fore, Style, init
# Diccionario con los comandos y sus descripciones
COMANDOS = {
    "1": ("Escanear IP o rango de IPs", "nmap <IP o rango>"),
    "2": ("Escaneo rápido de host y servicios (-T4)", "nmap -T4 <IP>"),
    "3": ("Escaneo de puertos más utilizados (--top-ports 100)", "nmap --top-ports 100 <IP>"),
    "4": ("Escaneo completo de todos los puertos (-p-)", "nmap -p- <IP>"),
    "5": ("Escaneo sigiloso SYN (-sS)", "nmap -sS <IP>"),
    "6": ("Escaneo con detección de SO y servicios (-A)", "nmap -A <IP>"),
    "7": ("Escaneo UDP (-sU)", "nmap -sU <IP>"),
    "8": ("Detección de firewall (--packet-trace)", "nmap --packet-trace <IP>"),
    "9": ("Evasión con checksums incorrectos (--badsum)", "nmap --badsum <IP>"),
    "10": ("Escaneo sin revelar IP de origen (-D RND:10)", "nmap -D RND:10 <IP>"),
    "11": ("Escaneo rápido en red local (-sn)", "nmap -sn <IP>"),
    "12": ("Descubrir hosts activos con ARP (-PR)", "nmap -PR <IP>"),
    "13": ("Escaneo con detección de vulnerabilidades (--script=vuln)", "nmap --script=vuln <IP>"),
    "14": ("Escaneo con fuerza bruta de credenciales (--script=brute)", "nmap --script=brute <IP>"),
    "15": ("Escaneo sigiloso extremo (-sS -T0)", "nmap -sS -T0 <IP>"),
    "16": ("Escaneo con fragmentación de paquetes (-f)", "nmap -f <IP>"),
    "17": ("Escaneo con spoofing de MAC (--spoof-mac 0)", "nmap --spoof-mac 0 <IP>"),
    "18": ("Escaneo con bypass de firewalls (--source-port 53)", "nmap --source-port 53 <IP>"),
    "19": ("Escaneo con scripts específicos (-sC --script=<script>)", "nmap -sC --script=<script> <IP>"),
    "20": ("Salir", "Finaliza el programa.")
}

def mostrar_help():
    """Muestra la ayuda del programa con la descripción de los comandos"""
    print(Fore.CYAN + "\nUso: python script.py [opción]\n")
    print(Fore.YELLOW + "Opciones disponibles:")
    for key, (descripcion, ejemplo) in COMANDOS.items():
        print(Fore.GREEN + f"{key}. {descripcion}")
        print(Fore.LIGHTBLACK_EX + f"   Ejemplo: {ejemplo}\n")
    print(Fore.CYAN + "También puedes ejecutar el programa sin argumentos para interactuar con el menú.")
