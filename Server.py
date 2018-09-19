import socket
import sys
import re

class Server:

    def check_for_hit(self, coordinates):
        print('Checking for hit')
        own_board = open('own_board.txt', 'r')
        lines = own_board.readlines()
        x = coordinates[0]
        y = coordinates[1]

        response = 'hit=0'
    
        if (lines[x][y] != '_'):
            print('ARG, WE BE HIT CAP\'N')
            response = 'hit=1'
        '''
        for j in lines:
            for i in j:
                print(i),
        '''
        return response

    def parse_shot(self, shot):
        coordinates = re.findall(r'\d+', shot)
        coordinates = map(int, coordinates)
        print(coordinates)
        return coordinates
    
    def listening(self):
        print("Beginning to listen...")
        self.s.listen(1)
        conn, address = self.s.accept()

        shot = conn.recv(64)
        print("Received data of " + shot.decode('utf-8'))
        
        coordinates = self.parse_shot(shot)
        
        response = self.check_for_hit(coordinates)

        print('Returning response')
        conn.send(response.encode('utf-8'))

        conn.close()

    def setup(self):
        my_address = ('127.0.0.1', 8000)
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        self.s.bind(my_address)    

S = Server()
S.setup()
S.listening()
