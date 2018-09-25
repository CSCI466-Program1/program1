import threading
import socket
import time

class Client2(threading.Thread):

    def __init__(self, my_name, my_ip, my_s_address, opp_s_address, my_turn):
        threading.Thread.__init__(self)
        
        print(my_name + " my server:" + str(my_s_address))
        print(my_name + " opp server:" + str(opp_s_address))
        
        self.my_name = my_name
        self.my_ip = my_ip
        self.my_s_address = my_s_address
        self.opp_s_address = opp_s_address
        self.my_turn = my_turn
        
    #-----------------------------------------------
    '''
    def talk_my_server(self):
    
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        while True:
            time.sleep(1)
            print(self.my_name + 'Trying to connect to my server ' + str(self.my_s_address))
            
            try:
                self.s.connect((self.my_s_address))
                break
            except Exception as e:
                print (self.my_name + 'Waiting for Server: '), e
                '''
                
                
    
    def talk_opp_server(self):
    
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        while True:
            time.sleep(1)
            print(self.my_name + 'Trying to connect to opp server ' + str(self.opp_s_address))
            
            try:
                self.s.connect((self.opp_s_address))
                break
            except Exception as e:
                print (self.my_name + 'Waiting for Server: '), e
                
    
    #----------------------------------------------
    
    def shoot(self):
        message = 'hi opp server'
        self.s.send(message.encode('utf-8'))
    
    def ask_my_turn(self):
        message = 'hi my server?'
        self.s.send(message.encode('utf-8'))
    
    
    #-----------------------------------------------
    
    #!!!!!
    def listen_my_server(self):
        #Listen for my server asking to connect
        #Accept connection
        #Use data to change self.my_turn variable
        my_server_conn, address = self.s.accept()
        print(self.my_name + " accepted connection from my server")
        data_my_server = my_server_conn.recv(64)
        my_server_conn.close()
        
        print(self.my_name +" received "+ data_my_server.decode('utf-8') + "from my server")
        
        self.my_turn = True
            
    
    def listen_opp_server(self):
        data_opp_server = self.s.recv(64)
        print(self.my_name + " received " + data_opp_server + "from opp server")
        
    
    #-----------------------------------------------
    
    def run(self):        
        
        while True:
        
            if (self.my_turn == True):
                self.talk_opp_server()
                self.shoot()
                self.listen_opp_server()                
                self.s.close()
                
                self.my_turn = False
                
            else:
                #NEW code
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.bind(self.my_ip)
                self.s.listen(1)
                self.listen_my_server()
                self.s.close()
            
                
                
            
    
    