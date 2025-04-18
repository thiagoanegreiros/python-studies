import abc


class Vehicle(abc.ABC):
    """
    Abstract class for Vehicles

    Attributes:
        name (str): Name of the vehicle
        max_speed (int): Max Speed it can achieve
    """
    __current_speed: int = 0
    name: str
    max_speed:int = 0
    acceleration_speed = 0

    def __init__(self, name: str, max_speed: int = 100, acceleration_speed: int = 1):
        self.name = name
        self.max_speed = max_speed
        self.acceleration_speed = acceleration_speed
    
    def __str__(self):
        return f'My {self.__class__.__name__} name is "{self.name}" and it\'s at {self.__current_speed} khm per hour ant its max speed is {self.max_speed}'
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', max_speed='{self.max_speed}')"

    def __eq__(self, value):
        return isinstance(value, Vehicle) and self.name == value.name

    def deaccelerate(self):
        self.__current_speed -= self.acceleration_speed
        if (self.__current_speed < 0):
            self.__current_speed = 0

    def accelerate(self):
        self.__current_speed += self.acceleration_speed
        if (self.__current_speed > self.max_speed):
            self.__current_speed = self.max_speed

    @property
    def current_speed(self) -> int:
        return self.__current_speed
    
    @abc.abstractmethod
    def honk(self):
        return 'Super Honk'


class Car(Vehicle):
    brand: str
    def __init__(self, name: str, max_speed: int = 10, acceleration_speed = 5, brand: str='Honda'):
        super().__init__(name, max_speed, acceleration_speed)
        self.brand = brand

    def __str__(self):
        return f'{super().__str__()} and my brand is {self.brand}'
    
    def honk(self):
        return super().honk() + ' -> Car Honk'

    @classmethod
    def defaultModel(cls):
        return cls('Fit', 180, 2)

    @staticmethod
    def khm_to_miles(khm: float):
        return khm * .62

class Bike(Vehicle):
    brand: str
    def __init__(self, name: str, max_speed: int = 10, acceleration_speed = 5, brand: str='Suzuki'):
        super().__init__(name, max_speed, acceleration_speed)
        self.brand = brand

    def __str__(self):
        return f'{super().__str__()} and my brand is {self.brand}'
    
    def honk(self):
        return super().honk() + ' -> Bike Honk'

c1 = Car('Civic', 200, 5)
c2 = Car('Civic', 200, 5)
c1.accelerate()
c1.accelerate()
print(c1)
print(c1.current_speed)

print('----')
print('----')

print(c1 == c2)

print(c1.honk())

fit = Car.defaultModel()
print(fit)

b1 = Bike('bike 01', 240, 10)
b2 = Bike('bike 02', 240, 10)

vehicles = [b1, b2, c1, c2]

for v in vehicles:
    print(v.honk())