import threading
import socket
import time
import os

class Client(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.my_server = ('127.0.0.1', 8000)

        self.shots = [0, 1, 1, 1]
           
    def update_opponent(self, data, x, y):

        response = data.decode('utf-8')
        replace = 'X'
        
        print("Received data: " + response)
        if (response == 'hit=1'):
            print('Hit')
        elif (response == 'hit=0'):
            print('Miss')
            replace = 'O'
        elif (response == 'sunk=C'):
            print('You sunk their Carrier')
        elif (response == 'sunk=B'):
            print('You sunk their Battleship')
        elif (response == 'sunk=R'):
            print('You sunk their Cruiser')
        elif (response == 'sunk=S'):
            print('You sunk their Submarine')
        elif (response == 'sunk=D'):
            print('You sunk their Destroyer')
        else:
            print('Invalid response')

        filepath = os.path.join('c:/Users/ian/Documents/Courses/CSCI 466/Program1', 'opponent_board.txt')
        opp_board_r = open(filepath, 'r')
        lines = opp_board_r.readlines()

        target_row = list(lines[x])
        target_row[y] = replace
        lines[x] = ''.join(target_row)
        opp_board_r.close()

        filepath = os.path.join('c:/Users/ian/Documents/Courses/CSCI 466/Program1', 'opponent_board.txt')
        opp_board_w = open(filepath, 'w')
        opp_board_w.write(''.join(lines))
        opp_board_w.close()
        
    
    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        
        while True:
            
            time.sleep(1)
            print('Trying to connect to ' + str(self.my_server))
            try:
                self.s.connect((self.my_server))
                break
            except Exception as e:
                print 'Waiting for Server: ', e
        
        
        
        count = 0
        for i in range(2):
            x = self.shots[count]
            count += 1
            y = self.shots[count]
            count += 1
        
            print('Firing at x=%s & y=%s' % (x, y))
            message = ('fire x=%s&y=%s' % (x, y))
            
            self.s.send(message.encode('utf-8'))

            data = self.s.recv(64)
                    
            self.update_opponent(data, x, y)
            
            time.sleep(1)

        self.s.close()