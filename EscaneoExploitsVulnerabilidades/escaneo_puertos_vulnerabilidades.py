import socket
import requests
import nmap
import subprocess

def search_nvd(product: str, versionOrig: str):
    """Busca vulnerabilidades en la base de datos de NVD (National Vulnerability Database)."""
    if not product or not versionOrig:
        print("[!] No se pudo determinar el producto o la versión.")
        return
    
    versiones = versionOrig.split('-')
   
    for version in versiones:
        print(f"[*] Buscando vulnerabilidades para {product} {version} en NVD...")
        if '.' in version and '-' in versionOrig: 
            version = ".".join(version.split(".")[:-1])
        try:
            # Llamamos a searchsploit pasando el producto y versión como argumentos separados
            result = subprocess.run(["searchsploit", product, version],
                                    capture_output=True, text=True)

            if result.returncode == 0:
                # Imprimimos la salida de searchsploit
                print(result.stdout)
            else:
                print(f"[!] Error ejecutando searchsploit: {result.stderr}")
        except Exception as e:
            print(f"[!] Error al ejecutar searchsploit: {e}")

def get_vulns_nmap(scripts):
    """Extrae y formatea las vulnerabilidades detectadas en los scripts de Nmap."""
    vulns = []
    for script_name, output in scripts.items():
        if "VULNERABLE" in output or "CVE" in output or "EXPLOIT" in output:
            vulns.append(f"[*] {script_name}: {output.strip()}\n")
    return vulns

def scan_port(target: str, port: int):
    """Escanea un puerto en busca de servicios y versiones."""
    nm = nmap.PortScanner()
    print(f"[*] Escaneando {target}:{port} con Nmap...")
    nm.scan(target, arguments=f'-p {port} -sV --script vuln')

    results = []

    if target in nm.all_hosts():
       # print(nm[target])
        for p in nm[target]['tcp']:
            service = nm[target]['tcp'][p].get('name', 'unknown')
            product = nm[target]['tcp'][p].get('product', '')
            version = nm[target]['tcp'][p].get('version', '')

            scripts = nm[target]['tcp'][p].get('script', {})
            vulns = get_vulns_nmap(scripts)
            
            results.append((p, service, product, version, vulns))
    else:
        print(f"[!] No se pudo escanear {target}. Verifica la conexión.")

    return results

def is_open(target: str, port: int):
    """Verifica si un puerto está abierto con una conexión de socket."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        s.close()
        return result == 0
    except socket.error:
        print(f"[!] Error conectando a {target}:{port}")
        return False

if __name__ == "__main__":
    target = str(input("Taget ip address: "))
    t_ports = input("Port or list of ports (separated by commas): ")  # Solicita los puertos como string
    t_ports = [int(port.strip()) for port in t_ports.split(",") if port.strip().isdigit()]

    for port in t_ports:
        if is_open(target, port):
            print(f"[+] El puerto {port} está abierto.")
            results = scan_port(target, port)

        if results:
            for (p, service, product, version, vulnerabilities) in results:
                print(f"[+] {p}/tcp -> {service} ({product} {version})")
                search_nvd(product, version)
                if vulnerabilities:
                        print("[🔴]Más Vulnerabilidades detectadas: ")
                        for vuln in vulnerabilities:
                            print(vuln)
        else:
            print(f"[-] El puerto {port} está cerrado.")

