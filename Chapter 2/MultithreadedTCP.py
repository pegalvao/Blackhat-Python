import socket
import threading

IP = "0.0.0.0"
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Criação do socket
    server.bind((IP,PORT)) # Associação entre a estrutura socket e o IP/porta
    server.listen(5) #Quantidade de solitações até o servidor realizar o próximo passo
    print(f'[*] Listening on {IP}: {PORT}')

    while True:
        client, adress = server.accept()
        print(f'[*] Accepted connection from {adress[0]}:{adress[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
        with client_socket as sock:
            request = sock.recv(1024)
            print(f'[*] Received: {request.decode("utf-8")}')
            sock.send(b'ACK')

# if __name__ == '__main__':
     #main()