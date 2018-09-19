import socket

class Server:

    my_address = ('127.0.0.1', 8080)
        
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #s.bind(('127.0.0.1', 8080))
    s.bind(my_address)

    print("Beginning to listen...")

    s.listen(1)

    conn, address = s.accept()

    data = conn.recv(64)

    print("Received data of " + data.decode('utf-8'))

    conn.send('Hey babe ;)'.encode('utf-8'))

    conn.close()

