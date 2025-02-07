import subprocess
import pyfiglet
import readline  # Para historial de comandos en Linux/Mac
from colorama import Fore, Style, init

init(autoreset=True)  # Inicializa colorama para reiniciar colores automáticamente

# Menú de opciones
programs = {
    1: "python3 /home/diego/Escritorio/Programas/nmap.py",
    2: "python3 /home/diego/Escritorio/Programas/hydra.py"
}

def show_banner():
    banner = pyfiglet.figlet_format("fsociety")
    print(Fore.RED + "*" * 37)
    print(Fore.GREEN + banner)
    print(Fore.RED + "*" * 37)

def select_menu():
    print(Fore.CYAN + "\nSeleccione una opción:")
    print(Fore.YELLOW + "1) Ejecutar nmap_fsociety")
    print(Fore.YELLOW + "2) Ejecutar hydra_fsociety")
    print(Fore.YELLOW + "Escriba 'exit' para salir\n")

def shell():
    show_banner()
    select_menu()  # Mostrar el menú antes de iniciar el shell

    while True:
        try:
            command = input(Fore.CYAN + "set> " + Style.RESET_ALL)

            if command.isdigit():  # Verificar si es un número
                command = int(command)
                if command in programs:
                    print(Fore.YELLOW + f"\nEjecutando {programs[command]}...")
                    subprocess.run(programs[command], shell=True, check=True)
                    continue
                else:
                    print(Fore.RED + "[!] Opción inválida. Intente de nuevo.")
                    continue
            
            if command.lower() == "main":
                subprocess.run("clear" if subprocess.os.name == "posix" else "cls", shell=True)

                show_banner()
                select_menu()
                continue

            if command.lower() == "exit":
                print(Fore.YELLOW + "\nSaliendo...")
                break

            output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
            print(Fore.WHITE + output)

        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n[!] Interrumpido por el usuario. Saliendo...")
            break
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"Error en el comando: {e.output}")
        except Exception as e:
            print(Fore.RED + f"Error inesperado: {e}")

if __name__ == "__main__":
    shell()
