import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    # set up the server and tie to a IP and PORT to listen to
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    print("[*] Listening on {}:{}".format(IP, PORT))
    # start listening with a backlog of max connections set to 5
    server.listen(5)

    # put the server in a loop to wait for client connections
    while True:
        client, address = server.accept() # returns the client socket object and the remote connection details 
        print("[*] Accepted connection from {}:{}".format(address[0], address[1]))

        # create a new thread object that points to handle_client function and pass the socket object as parameter
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    # receive the request from client and send an acknowledgement
    with client_socket as sock:
        request = sock.recv(1024)
        print("[*] Received: {}".format(request.decode("utf-8")))
        sock.send(b'ACK')

if __name__ == '__main__':
    main()

