""" Module to Test Sim Listener """
import socketserver
import socket


class HandlerTCPServer(socketserver.BaseRequestHandler):
    """ Create a TCP Server """

    def handle(self):
        # self.request - TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print( f"{self.client_address[0]} sent" )
        print(self.data)
        # just send back ACK for data arrival confirmation
        self.request.sendall("ACK from TCP Server".encode())

if __name__ == "__main__":
    PORT =  9000
    HOST = socket.gethostname()

    # Init the TCP server object, bind it to the localhost on 9999 port
    tcp_server = socketserver.TCPServer((HOST, PORT), HandlerTCPServer)

    # Activate the TCP server.
    # To abort the TCP server, press Ctrl-C.
    tcp_server.serve_forever()
