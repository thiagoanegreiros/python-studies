class Countdown():
    value: int
    def __init__(self, value: int):
        self.value = value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.value -= 1
        if (self.value < 0):
            raise StopIteration
        else:
            return self.value

for number in Countdown(5):
    print(number)