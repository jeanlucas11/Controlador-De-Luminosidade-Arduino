import socket

host = '10.1.25.173'
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

try:
    while True:
        print("\nDigite o número da luz que deseja acender:")
        print("1 - Quarto")
        print("2 - Cozinha")
        print("3 - Sala")
        valor = input("Comando: ")
        sock.sendall(valor.encode())
except KeyboardInterrupt:
    print("Saindo...")
finally:
    sock.close()