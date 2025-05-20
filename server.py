import socket
import serial
import time

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
time.sleep(2)  


host = '10.1.25.173'
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

print(f"Servidor escutando na porta {port}...")

conn, addr = sock.accept()
print(f"Conectado a {addr}")

try:
    while True:
        data = conn.recv(1024).decode().strip()
        if not data:
            break

        print("Recebido:", data)

        
        ser.write((data + '\n').encode())

        
        resposta = ser.readline().decode().strip()
        if resposta:
            print("Arduino disse:", resposta)
except KeyboardInterrupt:
    print("\nEncerrando servidor...")
finally:
    conn.close()
    sock.close()
    ser.close()
