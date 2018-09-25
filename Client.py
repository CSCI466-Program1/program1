import threading
import socket
import time
import os

class Client(threading.Thread):

    def __init__(self, my_turn, my_server, opp_server):
        threading.Thread.__init__(self)
        
        self.my_turn = my_turn
        
        self.my_server = my_server
        self.opp_server = opp_server

        self.shots = [
        0, 1,
        1, 1,
        2, 1,
        3, 1,
        4, 1,
        5, 1,
        0, 6,
        1, 6,
        2, 6,
        5, 5,
        5, 6,
        7, 2,
        7, 3,
        7, 4,
        7, 5,
        9, 0,
        9, 1,
        9, 2]
        
        self.count = 0
           
    def update_opponent(self, data, x, y):

        response = data.decode('utf-8')
        replace = 'X'
        
        print("C: Received data: " + response)
        if (response == 'hit=1'):
            print('C: Hit')
        elif (response == 'hit=0'):
            print('C: Miss')
            replace = 'O'
        elif (response == 'sunk=C'):
            print('C: You sunk their Carrier')
        elif (response == 'sunk=B'):
            print('C: You sunk their Battleship')
        elif (response == 'sunk=R'):
            print('C: You sunk their Cruiser')
        elif (response == 'sunk=S'):
            print('C: You sunk their Submarine')
        elif (response == 'sunk=D'):
            print('C: You sunk their Destroyer')
        else:
            print('C: Invalid response')

        filepath = os.path.join('C:\Users\ian\Downloads\program1-ian', 'opponent_board.txt')
        opp_board_r = open(filepath, 'r')
        lines = opp_board_r.readlines()

        target_row = list(lines[x])       
        target_row[y] = replace
        lines[x] = ''.join(target_row)
        opp_board_r.close()

        filepath = os.path.join('C:\Users\ian\Downloads\program1-ian', 'opponent_board.txt')
        opp_board_w = open(filepath, 'w')
        opp_board_w.write(''.join(lines))
        opp_board_w.close()
          
        print('Opponent Board')
        for i in range(10):
            print(lines[i])
    
    def shoot(self):
    
        x = self.shots[self.count]
        self.count += 1
        y = self.shots[self.count]
        self.count += 1
    
        print('C: Firing at x=%s & y=%s' % (x, y))
        message = ('fire x=%s&y=%s' % (x, y))
        
        self.s.send(message.encode('utf-8'))
        
        self.lastshot = [x, y]            

    
    def connect_opp_server(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        
        while True:
            
            time.sleep(0.01)
            print('C: Trying to connect to ' + str(self.opp_server))
            try:
                self.s.connect((self.opp_server))
                break
            except Exception as e:
                print 'C: Waiting for Server: ', e
                
    
    def connect_my_server(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        
        while True:
            
            time.sleep(0.01)
            print('C: Trying to connect to ' + str(self.my_server))
            try:
                self.s.connect((self.my_server))
                break
            except Exception as e:
                print 'C: Waiting for Server: ', e
        
    
    def run(self):
        
        while True:
            #TEMPORARY---------
            if(self.count >= 36):
                print('C: Game Over, You Win!')
                break
            #TEMPORARY---------
            if(self.my_turn == True):
                #print('C: 1')
                self.connect_opp_server()
                #print('C: 2')
                self.shoot()                                          
                
                data = self.s.recv(64)  
                
                self.update_opponent(data, self.lastshot[0], self.lastshot[1])
                self.s.close()
                
                time.sleep(0.01)
                
            else:
                time.sleep(0.01)
                