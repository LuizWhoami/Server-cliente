import socket

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('192.168.9.159', 80)
skt.connect(server)
skt.send(b"Oi Servidor\n")
cliente = skt.recv(1024).decode()
print(f"Recebido {cliente}")
skt.close()