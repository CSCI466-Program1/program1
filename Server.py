import threading
import socket
import re
import os

class Server(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        
        self.my_address = ('127.0.0.1', 8000)
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        self.carrier = 0 #5 lives
        self.battleship = 0 #4 lives
        self.crusier = 0 #3 lives
        self.submarine = 0 #3 lives
        self.destroyer = 0 #2 lives       
        

    def check_for_hit(self, coordinates):        
        filepath = os.path.join('c:/Users/ian/Documents/Courses/CSCI 466/Program1', 'own_board.txt')        
        own_board = open(filepath, 'r')        
        
        lines = own_board.readlines()        
        own_board.close()
        
        x = coordinates[0]
        y = coordinates[1]

        response = self.check_coords(lines[x][y])

        return response
    

    def check_coords(self, coord):

        if coord == '_':
            response = 'hit=0'            
            
        elif coord == 'C':            
            self.carrier += 1            
            response = self.check_sunk('C')
            
        elif coord == 'B':
            self.battleship += 1
            response = self.check_sunk('B') 
            
        elif coord == 'R':            
            self.cruiser += 1
            response = self.check_sunk('R')
            
        elif coord == 'S':            
            self.submarine += 1
            response = self.check_sunk('S')
            
        elif coord == 'D':  
            print('Destroyer hit!')
            self.destroyer += 1
            print('Destroyer adding taking damage, at %s damage' % self.destroyer)
            response = self.check_sunk('D')
        
        else:
            response = 'hit=0'
        
        return response
        
        
    def check_sunk(self, ship):
       
        if ship == 'C':
            if self.carrier < 5:
                response = 'hit=1'
            elif self.carrier >= 5:
                response = 'sunk=C'            
            
        elif ship == 'B':
            if self.battleship < 4:
                response = 'hit=1'
            elif self.battleship >= 4:
                response = 'sunk=B'            
        
        elif ship == 'R':
            if self.cruiser < 3:
                response = 'hit=1'
            elif self.cruiser >= 3:
                response = 'sunk=R'                    
            
        elif ship == 'S':
            if self.submarine < 3:
                response = 'hit=1'
            elif self.submarine >= 3:
                response = 'sunk=S'            
                              
        elif ship == 'D':
            if self.destroyer < 2:
                print('Destroyer has %s damage' % self.destroyer)
                response = 'hit=1'
            elif self.destroyer >= 2:
                print('Destroyer has been sunk, %s damage' % self.destroyer)
                response = 'sunk=D'          
        
        else:
            response = 'hit=0'
        
        return response
        

    def update_board(self):
        pass
    

    def respond(self, message):
        print('Returning response ' + str(message))        
        self.conn.send(str(message).encode('utf-8'))
        

    def parse_shot(self, shot):
        coordinates = re.findall(r'\d+', shot)
        coordinates = map(int, coordinates)
        print(coordinates)
        return coordinates

    
    def run(self):
        print("Beginning to listen...")
        self.s.bind(self.my_address)
        
        self.s.listen(1)
        self.conn, self.address = self.s.accept()
        
        for i in range(2):
        

            shot = self.conn.recv(64)
            print("Received data of " + shot.decode('utf-8'))
            
            coordinates = self.parse_shot(shot)
                #Parse string into integer array {x, y}
            
            response = self.check_for_hit(coordinates)
                #Check own_board.txt for hit or miss
                #Create string response of hit=0, hit=1, or sink
            
            self.respond(response)
                #Send message to client

        self.conn.close()
        
