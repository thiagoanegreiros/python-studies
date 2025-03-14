class TankError(Exception):
    pass

class Tank:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.__level = 0

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, amount):
        if amount > 0:
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError('Fuelling more than capacity level')
        elif amount < 0:
            raise TankError('Fuelling negative value is not allowed')

    @level.deleter
    def level(self):
        if self.__level > 0 :
            print('Cleaning the tank')
        self.__level = 0

our_tank = Tank(20)
our_tank.level = 10
print('Current liquid level:', our_tank.level)
del our_tank.level
