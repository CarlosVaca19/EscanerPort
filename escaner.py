import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        # Crear el socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Timeout reducido para mayor rapidez
            result = sock.connect_ex((ip, port))
            
            if result == 0:
                # Obtener nombre del servicio si es posible
                try:
                    service_name = socket.getservbyport(port)
                except OSError:
                    service_name = "Desconocido"
                
                print(f"Puerto abierto: {port} ({service_name})")
    except Exception as e:
        # Manejar errores generales, si los hubiera
        pass

if __name__ == "__main__":
    ip = input("Ingrese la dirección IP a escanear: ")

    print("Escaneando puertos...")
    with ThreadPoolExecutor(max_workers=100) as executor:
        # Escaneo en paralelo para mayor velocidad
        executor.map(lambda p: scan_port(ip, p), range(1, 1200))

    print("Escaneo finalizado.")
