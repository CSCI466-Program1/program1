import socket
from Client import Client
from Server import Server


class Driver():

    def run(self):

        #p1server = ('127.0.0.1', 8080)
        #p2server = ('localhost', 10005)

            
        

        print('Creating player 1\'s server')
        s1 = Server()
        #s2 = Server(p2server)

        print('Creating player 1\'s client')    
        c1 = Client()
        #c2 = Client(p2server, p1server)

m = Driver()
m.run()
