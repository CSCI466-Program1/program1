import time
import socket
from Client import Client
from Server import Server


class Driver:

    def run(self):

        #p1server = ('127.0.0.1', 8080)
        #p2server = ('localhost', 10005)
        
        print('Creating player 2\'s server')
        s2 = Server(('127.0.0.1', 9000))        
                
        print('Creating player 1\'s client')    
        c1 = Client(('127.0.0.1', 8000), ('127.0.0.1', 9000))

        s2.listening()
        c1.shoot()        

m = Driver()
m.run()
