import socket

class Client:

    def __init__(self, my_server, opp_server):        
        self.my_server = my_server
        self.opp_server = opp_server 
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.talk_to_opponent()
        
    def talk_to_self(self):
        #message to own server
        self.s.connect(my_server)

    def talk_to_opponent(self):
        #message to opponent's server
        self.s.connect(self.opp_server)
        self.s.send('Pew Pew'.encode('utf-8'))
        data = self.s.recv(64)
        print("Received data: " + data.decode('utf-8'))
        #s.close()
        
    def run(self):
        self.talk_to_opponent()
    
