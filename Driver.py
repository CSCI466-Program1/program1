import thread
from Client import Client
from Server import Server


class Driver:

    if __name__ == '__main__':
        
        s1_ip = ('127.0.0.1', 8000)
        s2_ip = ('127.0.0.1', 9000)
        
        c1_ip = ('127.0.0.1', 8005)
        c2_ip = ('127.0.0.1', 9005)
    
        thr_s1 = Server(s1_ip, s2_ip)
        #thr_s2 = Server(s2_ip, s1_ip)
        #thr_c1 = Client(False, s1_ip, s2_ip)
        thr_c2 = Client(True, s2_ip, s1_ip)
        

        thr_s1.start()
        #thr_s2.start()
        #thr_c1.start()
        thr_c2.start()

        thr_s1.join()
        #thr_s2.join()
        #thr_c1.join()
        thr_c2.join()

