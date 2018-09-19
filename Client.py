import socket

class Client:

    def setup(self):
        self.my_server = ('127.0.0.1', 8000)
    
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
    
    def speak(self):
        self.s.connect((self.my_server))

        self.s.send('fire x=0&y=1'.encode('utf-8'))

        data = self.s.recv(64)

        print("Received data: " + data.decode('utf-8'))

        self.s.close()

C = Client()
C.setup()
C.speak()
