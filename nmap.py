import subprocess
import ayuda_nmap
import readline
from colorama import Fore, Style, init

opciones = {
    1: "Escanear IP o rango de IPs",
    2: "Escaneo rápido de host y servicios (-T4)",
    3: "Escaneo de puertos más utilizados (--top-ports)",
    4: "Escaneo completo de todos los puertos (-p-)",
    5: "Escaneo sigiloso SYN (-sS)",
    6: "Escaneo con detección de SO y servicios (-A)",
    7: "Escaneo UDP (-sU)",
    8: "Detección de firewall (--packet-trace)",
    9: "Evasión con checksums incorrectos (--badsum)",
    10: "Escaneo sin revelar IP de origen (-D RND:10)",
    11: "Escaneo rápido en red local (-sn)",
    12: "Descubrir hosts activos con ARP (-PR)",
    13: "Escaneo con detección de vulnerabilidades (--script=vuln)",
    14: "Escaneo con fuerza bruta de credenciales (--script=brute)",
    15: "Escaneo sigiloso extremo (-sS -T0)",
    16: "Escaneo con fragmentación de paquetes (-f)",
    17: "Escaneo con spoofing de MAC (--spoof-mac)",
    18: "Escaneo con bypass de firewalls (--source-port 53)",
    19: "Escaneo con scripts específicos (-sC --script=<script>)",
    20: "Help", 
    21: "Mostrar opciones", 
    22: "Salir",
    23: "Nmap propio"
}

def run_nmap(command: list | str):
    """Ejecuta un comando de Nmap de manera segura."""
    try:
        print(Fore.BLUE + f"\nEjecutando: {' '.join(command)}\n")

        if(input("Deseas modificar el comando? (s/n): ") == "s"):
            command = modificar_comando(' '.join(command)).split()

        output = subprocess.run(command, capture_output=True, text=True)
        print(output.stdout)

        if output.stderr:
            print(Fore.RED + f"Error durante el escaneo: {output.stderr}")
            return

        print(Fore.GREEN + "✅ Nmap ejecutado correctamente.")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"❌ Error ejecutando nmap: {e}")

def mostrar_opt():
    print(Fore.YELLOW + "Opciones disponibles:")
    for key, value in opciones.items():
       print(Fore.WHITE + f"{key}. {value}")

def modificar_comando(comand: str):
    """Modifica un comando Nmap según la opción elegida. (Prerrellena)"""
    readline.set_startup_hook(lambda: readline.insert_text(comand)) #se ejecuta antes de de que se muestre el input

    try:
        return input(Fore.WHITE + "Modificando comando Nmap: ")
    finally:
        readline.set_startup_hook() #Limpia el hock para evitar errores

def main():
    
    print( Fore.WHITE + "\n🔍 Automatización de Nmap\n")
    mostrar_opt()
 
    while(True):
        try:
            opt = int(input(Fore.CYAN + "\nSelecciona una opción, teclea 21 para ver de nuevo las opciones: "))
        except ValueError:
            print(Fore.RED + "⚠️ Opción inválida. Intente de nuevo.")
            return
    
        if opt not in opciones:
            print(Fore.RED + "⚠️ Opción inválida. Intente de nuevo.")
            return

        if opt == 20:
            ayuda_nmap.mostrar_help()
            continue

        if opt == 21:
            mostrar_opt()
            continue

        if opt == 22:
            print(Fore.GREEN + "👋 Saliendo...")
            return

        # Diccionario de comandos Nmap según la opción elegida
        comandos = {
            1: lambda: ["nmap", input("Introduce IP o rango de IPs: ")],
            2: lambda: ["nmap", "-T4", input("Introduce IP o rango de IPs: ")],
            3: lambda: ["nmap", "--top-ports", "100", input("Introduce IP o rango de IPs: ")],
            4: lambda: ["nmap", "-p-", input("Introduce IP o rango de IPs: ")],
            5: lambda: ["nmap", "-sS", input("Introduce IP o rango de IPs: ")],
            6: lambda: ["nmap", "-A", input("Introduce IP o rango de IPs: ")],
            7: lambda: ["nmap", "-sU", input("Introduce IP o rango de IPs: ")],
            8: lambda: ["nmap", "--packet-trace", input("Introduce IP o rango de IPs: ")],
            9: lambda: ["nmap", "--badsum", input("Introduce IP o rango de IPs: ")],
            10: lambda: ["nmap", "-D", "RND:10", input("Introduce IP o rango de IPs: ")],
            11: lambda: ["nmap", "-sn", input("Introduce IP o rango de IPs: ")],
            12: lambda: ["nmap", "-PR", input("Introduce IP o rango de IPs: ")],
            13: lambda: ["nmap", "--script=vuln", input("Introduce IP o rango de IPs: ")],
            14: lambda: ["nmap", "--script=brute", input("Introduce IP o rango de IPs: ")],
            15: lambda: ["nmap", "-sS", "-T0", input("Introduce IP o rango de IPs: ")],
            16: lambda: ["nmap", "-f", input("Introduce IP o rango de IPs: ")],
            17: lambda: ["nmap", "--spoof-mac", "0", input("Introduce IP o rango de IPs: ")],
            18: lambda: ["nmap", "--source-port", "53", input("Introduce IP o rango de IPs: ")],
            19: lambda: ["nmap", "-sC", "--script=" + input("Introduce nombre del script: "), input("Introduce IP o rango de IPs: ")],
            23: lambda: input("Introduce el comando Nmap personalizado: ").split()
        }

        # Ejecuta el comando correspondiente a la opción elegida
        command = comandos[opt]()
        run_nmap(command)
    

if __name__ == '__main__':
    main()
