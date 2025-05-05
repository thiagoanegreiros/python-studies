class Countdown():
    __value: int
    def __init__(self, value: int):
        self.__value = value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__value -= 1
        if (self.__value < 0):
            raise StopIteration
        else:
            return self.__value

for number in Countdown(5):
    print(number)
