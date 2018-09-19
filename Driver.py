import socket

class Driver():

    def run(self):

        p1client = ('localhost', 10000)
        p2client = ('localhost', )

        p1server = ('localhost', )
        p2server = ('localhost', )


        c1 = Client(p1server, p2server)
        c2 = Client(p2server, p1server)

        s1 = Server(('localhost', 10000), p1client, p2client)
        s2 = Server(('localhost', 10005), p2client, p1client)

m = Driver()
m.run()
