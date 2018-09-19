import socket

class Server:
    
    def __init__(self, name):
        self.name = name        

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(name)
        
        self.run()
        
    def run(self):
        self.listen_to_self()

    def talk_to_self(self):
        #message to own client
        pass

    def talk_to_opponent(self):
        #message to opponent's client
        pass

    def listen_to_self(self):
        print("Beginning to listen...")
        self.s.listen(1)
        conn, address = self.s.accept()
        data = conn.recv(64)
        print("Received data of " + data.decode('utf-8'))
        conn.send('Hey babe ;)'.encode('utf-8'))
        #conn.close()
        
        #TEMPORARY FOR DEBUGGING
        #s.close()
    
