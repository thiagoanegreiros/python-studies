class AccountException(Exception):
    pass

class BankAccount:
    def __init__(self, account: str, balance: int):
        self.__account = account
        self.__balance = balance
    def withdraw(self, val: int):
        if val > 100000:
            print(f'Big value changing the balance')
        self.balance -= val
    def deposit(self, val: int):
        if val > 100000:
            print(f'Big value changing the balance')
        self.balance += val
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, val):
        print(f'Setting balance to: {val}')
        if val < 0:
            raise AccountException('Negative value not allowed')
        self.__balance = val
    
    @property
    def account(self):
        return self.__account
    
    @account.deleter
    def account(self):
        if self.__balance == 0:
            raise AccountException('Not allowed delete the account if balance is 0')
            
a1 = BankAccount('abc', 10000000)
a1.withdraw(1)
print(a1.account)
print()
a1.deposit(10000000)

a1.account = 'aa'
a1.balance = -100
