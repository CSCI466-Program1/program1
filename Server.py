import threading
import socket
import re
import os

class Server(threading.Thread):

    def __init__(self, my_ip, opp_ip):
        threading.Thread.__init__(self)
                
        self.my_ip = my_ip
        self.opp_ip = opp_ip
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(self.my_ip)
    
        self.carrier = 0 #5 lives
        self.battleship = 0 #4 lives
        self.cruiser = 0 #3 lives
        self.submarine = 0 #3 lives
        self.destroyer = 0 #2 lives       
        

    def check_for_hit(self, coordinates):        
        filepath = os.path.join('C:\Users\ian\Downloads\program1-ian', 'own_board.txt')        
        own_board = open(filepath, 'r')        
        
        lines = own_board.readlines()        
        own_board.close()
        
        print('Own Board')
        for i in range(10):
            print(lines[i])
        
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
            print('S: Destroyer hit!')
            self.destroyer += 1
            print('S: Destroyer adding taking damage, at %s damage' % self.destroyer)
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
                print('S: Destroyer has %s damage' % self.destroyer)
                response = 'hit=1'
            elif self.destroyer >= 2:
                print('S: Destroyer has been sunk, %s damage' % self.destroyer)
                response = 'sunk=D'          
        
        else:
            response = 'hit=0'
        
        return response
        

    def update_board(self):
        pass
    

    def respond(self, message):
        print('S: Returning response ' + str(message))        
        self.conn.send(str(message).encode('utf-8'))
        

    def parse_shot(self, shot):
        coordinates = re.findall(r'\d+', shot)
        coordinates = map(int, coordinates)        
        return coordinates

    
    def run(self):
                
        while True:
            print("S: Beginning to listen...")
                          
            self.s.listen(1)
            self.conn, self.address = self.s.accept()
            print('S: Connected to ' + str(self.address))

            shot = self.conn.recv(64)
            print("S: Received data of " + shot.decode('utf-8'))
            
            coordinates = self.parse_shot(shot)
                #Parse string into integer array {x, y}
            
            response = self.check_for_hit(coordinates)
                #Check own_board.txt for hit or miss
                #Create string response of hit=0, hit=1, or sink
            
            self.respond(response)
                #Send message to client

            self.conn.close()
        
