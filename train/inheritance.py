from abc import abstractmethod, ABC

class Account(ABC):
    def __init__(self, balance: int):
        self._balance = balance

    @abstractmethod
    def deposit(self, value: int) -> int:
        pass
    
    @abstractmethod
    def withdraw(self, value: int) -> int:
        pass

    def __str__(self):
        return f'{self.__class__.__name__} - {self._balance}'

class CheckingAccount(Account):
    def __init__(self, value: int):
        super().__init__(value)
    
    def deposit(self, value: int) -> int:
        self._balance = self._balance + value
        return self._balance
    
    def withdraw(self, value: int) -> int:
        if self._balance < value:
            raise ValueError('Account Balance not available')
        self._balance = self._balance - value
        return self._balance
    
class DepositAccount(Account):
    def __init__(self, value: int):
        super().__init__(value)
    
    def deposit(self, value: int) -> int:
        self._balance = self._balance + value
        return self._balance
    
    def withdraw(self, value: int) -> int:
        if self._balance < value:
            raise ValueError('Account Balance not available')
        self._balance = self._balance - value
        return self._balance


ac1 = CheckingAccount(300)
ac1.deposit(200)
print(ac1.withdraw(200))

mylist = [ac1, CheckingAccount(2), DepositAccount(22)]

for i  in mylist:
    print(i)