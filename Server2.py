import threading
import socket
import time

class Server2(threading.Thread):

    def __init__(self, my_name, my_address, my_client,  am_listening):
        threading.Thread.__init__(self)
        
        self.my_name = my_name
        self.my_address = my_address
        self.my_client = my_client
        
        self.listening = am_listening
       
#-----------------------------------------------------   
        
    def listen_opp_client(self):        
        self.opp_client_conn, opp_client_address = self.s.accept()        
        data_opp_client = self.opp_client_conn.recv(64)
        
        print(self.my_name + " recieved " + data_opp_client + "from opp client")
        
        
    
#-----------------------------------------------------
    
    #!!!!!
    def talk_own_client(self):
        #open connection with my client's ip
        #send message
        #Close connection
        while True:
            try:
                self.s.connect(self.my_client)
                break
            except Exception as e:
                print self.my_name, e
                
        print(self.my_name + " connected to own client")
        message = 'your turn=True'
        self.s.send(message.encode('utf-8'))
        print(self.my_name + " sent your turn message to own client")
                           
        
    def talk_opp_client(self):
    
        message = 'hi opponent'
        self.opp_client_conn.send(str(message).encode('utf-8'))
        print(self.my_name + " sent message to opp client")
            
        
#-----------------------------------------------------  
    
    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        self.s.bind(self.my_address)
        
        while True:
        
            if(self.listening == True):
                
                print(self.my_name + ' Listening for connection')                
                self.s.listen(1)                                
                print(self.my_name + ' Waiting for packet')                
                self.listen_opp_client()                                               
                self.talk_opp_client()                
                print(self.my_name + ' Closing connection')                
                self.opp_client_conn.close()                                              
                                
                self.listening = False
                
            else:                
                self.s = self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                self.talk_own_client()
                self.s.close()
                
                self.listening = True
                
            #--------------------------------    
            time.sleep(1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        