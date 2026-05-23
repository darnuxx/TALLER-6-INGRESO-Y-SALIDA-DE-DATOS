import socket
import ssl
import gzip

HOST = "www.python.org"
PORT = 443
PATH = "/"

class HTTPClient:

    def fetch(self, path):

        # Crear socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # HTTPS
        context = ssl.create_default_context()
        client = context.wrap_socket(sock, server_hostname=HOST)

        print("Conectando con:", HOST)

        client.connect((HOST, PORT))

        # Petición HTTP
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {HOST}\r\n"
            f"Connection: close\r\n\r\n"
        )

        client.send(request.encode())

        print("Petición enviada...")

        response = b""

        while True:

            data = client.recv(4096)

            if not data:
                break

            response += data

        client.close()

        # Separar headers y body
        headers, body = response.split(b"\r\n\r\n", 1)

        print(headers.decode(errors="ignore"))

        # Descomprimir gzip
        body = gzip.decompress(body)

        # Convertir a texto
        html = body.decode("utf-8", errors="ignore")

        return html


# Ejecutar cliente
client = HTTPClient()

html = client.fetch(PATH)

print("\n===== HTML =====\n")

print(html[:5000])
