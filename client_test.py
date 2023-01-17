""" Module to Test Sim Listener """
import json
import socket
import sys
import requests

SIM_SERVER_URL = "https://localhost:27464/api/v1/API/register"

def register():
    """Register with Sim Listener"""
    content = { 'Content-Type': 'application/json' , 'accept': 'text/plain' }
    rdata = {  "name": "Python Output Test" }

    print( "Registration data =" , json.dumps(rdata) )
    try:
        req = requests.request( "POST" , SIM_SERVER_URL,
                                         timeout=10,
                                         headers=content,
                                         data=json.dumps(rdata),
                                         verify=False )
    except requests.exceptions.ConnectionError as e :
        print( "Server not ready")
        sys.exit(1)

    print( "RESPONSE = " , req.text )
    return json.loads(req.text)

# Set up some data to send
json_data = {  "BUTTON POSITION": "ON" }
data = json.dumps(json_data)

# Currently this is running on same server as tcp server.
host = socket.gethostname() # Get local machine name
#j = register()
#port = int(j['Port'])
port=9000
print( f"Connecting on {host}:{port}")

# Initialize a TCP client socket using SOCK_STREAM
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect((host, port))
tcp_client.setblocking( True )

while True:
    try:
        tcp_client.sendall(data.encode() )
        received = tcp_client.recv(1024)
        print (f"Bytes Received: {received.decode()}" )
        print (f"Bytes Sent: {data}")
    except ConnectionResetError as e :
        print( f"Socket Closed with {e}" )
        sys.exit(1)
    except BlockingIOError as e :
        pass
