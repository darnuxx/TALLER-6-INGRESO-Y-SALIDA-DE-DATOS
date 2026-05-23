import sys
import socket
import argparse

def main():

    # Argumentos
    parser = argparse.ArgumentParser(
        description='Socket Error Example'
    )

    parser.add_argument('--host', required=True)
    parser.add_argument('--port', type=int, required=True)
    parser.add_argument('--file', required=True)

    args = parser.parse_args()

    host = args.host
    port = args.port
    filename = args.file

    # Crear socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as e:
        print("Error creando socket:", e)
        sys.exit(1)

    # Conectar
    try:
        s.connect((host, port))

    except socket.gaierror as e:
        print("Error de dirección:", e)
        sys.exit(1)

    except socket.error as e:
        print("Error de conexión:", e)
        sys.exit(1)

    # Enviar datos
    try:

        request = f"GET /{filename} HTTP/1.0\r\nHost: {host}\r\n\r\n"

        s.sendall(request.encode())

    except socket.error as e:
        print("Error enviando datos:", e)
        sys.exit(1)

    # Recibir respuesta
    while True:

        try:
            buf = s.recv(2048)

        except socket.error as e:
            print("Error recibiendo datos:", e)
            sys.exit(1)

        if not buf:
            break

        print(buf.decode(errors="ignore"))

    s.close()


if __name__ == '__main__':
    main()
