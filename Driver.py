import thread
from Client import Client
from Server import Server


class Driver:

    if __name__ == '__main__':

        thread1 = Server()
        thread2 = Client()

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

