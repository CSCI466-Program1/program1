import socket

class Server:
    
    def __init__(self, name):
        self.name = name        

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(name)

    def talk_to_self():
        #message to own client
        pass

    def talk_to_opponent():
        #message to opponent's client
        pass
