""" Module to Test Sim Listener """
import platform
import json
import socket
import requests


SIM_SERVER_URL = "https://192.168.1.134:7039/api/simulator/register"

def register():
    """Register with Sim Listener"""
    content = { 'Content-Type': 'application/json' , 'accept': 'text/plain' }
    data = {  "name": "Python Output Test",  "outputs": [ "FUEL TOTAL QUANTITY" ] }

    data[ "os_system" ] = platform.system()
    data[ "os_version" ] = platform.version()

    print( "DATA =" , json.dumps(data) )
    req = requests.request( "POST" , SIM_SERVER_URL,
                                   timeout=10,
                                   headers=content,
                                   data=json.dumps(data),
                                   verify=False )
    print( "RESPONSE = " , req.text )
    return json.loads(req.text)


def connect( ip_address , port ):
    """Connect to the TCP Port"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(( ip_address, port ))
    return client_socket

def listen( skt ):
    """ Listen for data"""
    data = skt.recv(512)
    return data


j = register()
server_socket = connect( j['ip_address'] , int( j['port'] ) )
while True :
    print(f"RECEIVED: {1}" % listen( server_socket ) )
