import abc

class BluePrint(abc.ABC): 
    @abc.abstractmethod
    def hello(self):
        pass

class WhitePool(BluePrint):
    def hello(self):
        print('Welcome to the White Pool!')

wp = WhitePool()
wp.hello()  # Saída: "Welcome to the White Pool!"
