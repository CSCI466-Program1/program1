import threading
import thread
import time
from Client2 import Client2
from Server2 import Server2


class Driver2:

    if __name__ == '__main__':
        
        s1_ip = (('127.0.0.1', 8000))
        
        s2_ip = (('127.0.0.2', 9000))
        
        c1_ip = (('127.0.1.1', 8001))
        
        c2_ip = (('127.0.2.2', 9002))
        
        #--------------------        
        
        thr_s1 = Server2('Server1', s1_ip, c1_ip,  True)
        thr_s2 = Server2('Server2', s2_ip, c2_ip, False)
        thr_c1 = Client2('Client1', c1_ip, s1_ip, s2_ip, False)
        thr_c2 = Client2('Client2', c2_ip, s2_ip, s1_ip, True)        
        #----------------------------------------------        
        
        thr_s1.start()
        thr_s2.start()
        thr_c1.start()
        thr_c2.start()
        #-------------                
        
        thr_s1.join()
        thr_s2.join()
        thr_c1.join()
        thr_c2.join()
        #------------ 
        
        thr_s1.exit()
        thr_s2.exit()
        thr_c1.exit()
        thr_c2.exit()
            
        

