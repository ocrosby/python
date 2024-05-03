import socket
import threading

IP = '0.0.0.0'
PORT = 9998


"""
This example creates a standard multi-threaded TCP server that listens on port 9998.

1. pass in the IP address and port we want the server to listen on
2. with a maximum backlog of connections set to 5 we put the server into its main loop where it waits for an incoming connection.
3. When a client connects, we print out the IP address and port of the client.
4. We then create a new thread object that points to the handle_client function, passing in the client socket object as an argument.
5. We start the new thread, and the main server loop goes back to waiting for incoming connections.
6. The handle_client function is where we receive the client data and send a simple response back to the client.

You can use the tcp_client.py script to connect to this server and test it out.
"""


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, addr = server.accept()
        print(f'[*] Accepted connection from: {addr[0]}:{addr[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')


if __name__ == '__main__':
    main()
