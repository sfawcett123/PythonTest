""" Module to Test Sim Listener """
import json
import socket
import requests
import socket
import time


host = socket.gethostname() # Get local machine name
#host = "192.204.3.21"


SIM_SERVER_URL = f"https://{host}:27464/api/v1/API/register"

def register():
    """Register with Sim Listener"""
    content = { 'Content-Type': 'application/json' , 'accept': 'text/plain' }
    data = {  "name": "Python Output Test" }


    print( "DATA =" , json.dumps(data) )
    req = requests.request( "POST" , SIM_SERVER_URL,
                                   timeout=10,
                                   headers=content,
                                   data=json.dumps(data),
                                   verify=False )
    print( "RESPONSE = " , req.text )
    return json.loads(req.text)


#j = register()
#port = int(j['port'])
port = 9000

print( f"Connecting on {host}:{port}")

s = socket.socket()         # Create a socket object

# Initialize a TCP client socket using SOCK_STREAM
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
json_data = {  "BUTTON POSITION": "OFF" }
data = json.dumps(json_data)

try:
    # Establish connection to TCP server and exchange data
    tcp_client.connect((host, port))
    while True:
        tcp_client.sendall(data.encode())
        received = tcp_client.recv(1024)
        print ("Bytes Sent:     {}".format(data))
        print ("Bytes Received: {}".format(received.decode()))    
finally:
    tcp_client.close()

               # Close the socket when done
