import requests 
import socket
import json
import os
import platform
import os_release

SIM_SERVER_URL = "https://192.168.1.134:7039/api/simulator/register"

def Register():
    
    CONTENT = { 'Content-Type': 'application/json' , 'accept': 'text/plain' }
    data = {  "name": "Python Output Test",  "outputs": [ "FUEL TOTAL QUANTITY" ] }

    try:
        data[ "linux_name" ] = os_release.current_release().pretty_name 
    except FileNotFoundError:
        pass

    data[ "os_system" ] = platform.system()
    data[ "os_version" ] = platform.version()
    
    print( "DATA =" , json.dumps(data) )
    r = requests.request( "POST" , SIM_SERVER_URL, headers=CONTENT, data=json.dumps(data),  verify=False ) 
    print( "RESPONSE = " , r.text );
    return( json.loads(r.text) )


def Connect( ip , port ):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(( ip, port ))
        return client_socket

def Listen( skt ):
    data = skt.recv(512) ;
    return data


j = Register()
skt = Connect( j['ip_address'] , int( j['port'] ) )
while( True ):
    print("RECEIVED: %s" % Listen( skt ) )


