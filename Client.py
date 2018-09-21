import socket
import os

class Client:

    def setup(self):
        self.my_server = ('127.0.0.1', 8000)        
			

    def update_opponent(self, data, x, y):

        response = data.decode('utf-8')
        replace = 'X'
        
        print("Received data: " + response)
        if (response == 'hit=1'):
            print('Hit')
        elif (response == 'hit=0'):
            print('Miss')
            replace = 'O'
        elif (response == 'sink=C'):
            print('You sunk their Carrier')
        elif (response == 'sink=B'):
            print('You sunk their Battleship')
        elif (response == 'sink=R'):
            print('You sunk their Cruiser')
        elif (response == 'sink=S'):
            print('You sunk their Submarine')
        elif (response == 'sink=D'):
            print('You sunk their Destroyer')
        else:
            print('Invalid response')

        filepath = os.path.join('c:/Users/ian/Documents/Courses/CSCI 466/Program1', 'opponent_board.txt')
        opp_board_r = open(filepath, 'r')
        lines = opp_board_r.readlines()
        print(lines)

        target_row = list(lines[x])
        target_row[y] = replace
        lines[x] = ''.join(target_row)
        print(lines)
        opp_board_r.close()

        filepath = os.path.join('c:/Users/ian/Documents/Courses/CSCI 466/Program1', 'opponent_board.txt')
        opp_board_w = open(filepath, 'w')
        opp_board_w.write(''.join(lines))
        opp_board_w.close()
        
    
    def speak(self, x, y):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
        self.s.connect((self.my_server))
        
        message = ('fire x=%s&y=%s' % (x, y))
		
        self.s.send(message.encode('utf-8'))

        data = self.s.recv(64)
        print("Received data: " + data.decode('utf-8'))
        
        self.update_opponent(data, x, y)

        self.s.close()


C = Client()
C.setup()
C.speak(0, 1)
C.speak(1, 1)
