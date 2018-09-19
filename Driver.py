import socket
from Client import Client
from Server import Server


class Driver():

    def run(self):

        p1server = ('localhost', 10000)
        p2server = ('localhost', 10005)

        c1 = Client(p1server, p2server)
        c2 = Client(p2server, p1server)

        s1 = Server(p1server)
        s2 = Server(p2server)

m = Driver()
m.run()
