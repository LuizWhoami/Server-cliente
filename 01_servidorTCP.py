import socket

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('', 80) #IP e porta 
skt.bind(server) #Pega o IP e Porta
skt.listen(10) #limite de listagem
while True:
    cliente, endereco = skt.accept() #cria uma variavel de aceitamento
    print(f"Cliente: {cliente} se conectou") 
    recebido = cliente.recv(1024).decode() #cria uma variavel que decodifica o que o Cliente vai receber
    print(f"Recebido: {recebido}")
    if recebido == 'Oi servidor\n':
        cliente.send(b'Oi de volta\n') #mostra o que o cliente recebeu 
    cliente.close()