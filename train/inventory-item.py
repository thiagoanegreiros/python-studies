class InventoryItem():
    name: str
    _qtd: int

    @property
    def qtd(self):
        return self._qtd
    
    @qtd.setter
    def qtd(self, val):
        if (val < 0):
            raise ValueError('Invalid negative value')
        self._qtd = val

    def __init__(self, name: str, qtd: int):
        self.name = name
        self._qtd = qtd
    
    def __str__(self):
        return f'Inventory for {self.name} = {self.qtd} items'
    
    def __repr__(self):
        return f'{self.name} - {self.qtd}'
    
    def __eq__(self, value):
        return isinstance(value, InventoryItem) and value.name == self.name
    
    def __hash__(self):
        return hash(self.name)

    def __add__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return InventoryItem(self.name, self.qtd + other.qtd)
        elif isinstance(other, (int, float)):
            return InventoryItem(self.name, self.qtd + other)
        else:
            raise ValueError('Invalid value')
    
    def __sub__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            if self.qtd - other.qtd < 0:
                raise ValueError('Not enough items')
            return InventoryItem(self.name, self.qtd - other.qtd)
        elif isinstance(other, (int, float)):
            if self.qtd - other < 0:
                raise ValueError('Not enough items')
            return InventoryItem(self.name, self.qtd - other)
        else:
            raise ValueError('Invalid value')

    def __len__(self):
        return self.qtd

    def __bool__(self):
        return self.qtd > 0

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return InventoryItem(self.name, self.qtd * factor)
        else:
            raise ValueError('Invalid value')
        
    def __lt__(self, other):
        if isinstance(other, InventoryItem):
            return self.qtd < other.qtd
        elif isinstance(other, (int, float)):
            return self.qtd < other
        else:
            raise ValueError('Not valid value')
        
    def __gt__(self, other):
        if isinstance(other, InventoryItem):
            return self.qtd > other.qtd
        elif isinstance(other, (int, float)):
            return self.qtd > other
        else:
            raise ValueError('Not valid value')

    @staticmethod
    def sum_items(items: list):
        return sum(x.qtd for x in items if isinstance(x, InventoryItem))

i1 = InventoryItem('Shampoo', 1)
i1 += 5
i1 -= 1

i2 = InventoryItem('Shampoo', 2)
i3 = i2 + i1

print(i1)
print(i3)

print(i3 < i1)
print(i1 < i3)
print(i1 < 20)


items = [i3, 80, i1, i2, 99, 60]

newItems =  sorted(items)
print(newItems)

print(InventoryItem.sum_items(newItems))

test = [x.name for x in newItems if isinstance(x, InventoryItem)]

print(test)