import socket
import re

class Client:

    def update_opponent(self, data, x_shot, y_shot):

        response = data.decode('utf-8')
        replace = 'X'
        
        print("Received data: " + response)
        if (response == 'hit=1'):
            print('Hit')
        if (response == 'hit=0'):
            print('Miss')
            replace = 'O'
        if (response == 'sink=C'):
            print('You sunk my Carrier')
        if (response == 'sink=B'):
            print('You sunk my Battleship')
        if (response == 'sink=R'):
            print('You sunk my Cruiser')
        if (response == 'sink=S'):
            print('You sunk my Submarine')
        if (response == 'sink=D'):
            print('You sunk my Destroyer')

        opp_board_r = open('opponent_board.txt', 'r')
        lines = opp_board_r.readlines()
        print(lines)

        target_row = list(lines[x_shot])
        target_row[y_shot] = replace
        lines[x_shot] = ''.join(target_row)
        print(lines)
        opp_board_r.close()

        opp_board_w = open('opponent_board.txt', 'w')
        opp_board_w.write(''.join(lines))
        opp_board_w.close()                   

    def setup(self):
        self.my_server = ('127.0.0.1', 8000)
    
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
    
    def speak(self):
        self.s.connect((self.my_server))

        x_shot = 0
        y_shot = 1

        self.s.send(('fire x=' + str(x_shot) + '&y=' + str(y_shot)).encode('utf-8'))

        data = self.s.recv(64)
        self.update_opponent(data, x_shot, y_shot)

        self.s.close()

C = Client()
C.setup()
C.speak()
