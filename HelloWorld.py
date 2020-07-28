import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 12345))
s.listen(1)

while True:
    conn, addr = s.accept()
    print("New connection from " + str(addr) + ".")
     
    data = conn.recv(1024)
    print("Received:", data)
    response = bytes("HTTP/1.1 200 OK\n"
     +"Content-Type: text/html\n"
     +"\n" # Important!
     +"<html><body>Hello World!</body></html>\n")
    
    conn.send(response)
            

    conn.close()
    print("Closed.")
