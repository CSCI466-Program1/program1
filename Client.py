import socket

class Client:

    my_server = ('127.0.0.1', 8080)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        

    #s.connect(('127.0.0.1', 8080))
    s.connect((my_server))

    s.send('Pew Pew'.encode('utf-8'))

    data = s.recv(64)

    print("Received data: " + data.decode('utf-8'))

    s.close()
  
