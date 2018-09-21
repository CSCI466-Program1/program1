import socket

class Client:

    def setup(self):
        self.my_server = ('127.0.0.1', 8000)        
				
    
    def speak(self, x, y):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
        self.s.connect((self.my_server))
        
        message = ('fire x=%s&y=%s' % (x, y))
		
        self.s.send(message.encode('utf-8'))

        data = self.s.recv(64)

        print("Received data: " + data.decode('utf-8'))

        self.s.close()


C = Client()
C.setup()
C.speak(0, 1)
C.speak(1, 1)
