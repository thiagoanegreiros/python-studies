class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value
    
    def __repr__(self):
        return f'Value: {self.value}'
    
    def __add__(self, other):
        return str(self.value) + other
    
    def __str__(self):
        return str(self.value)

items = [Node(1), Node(2), Node(3), Node(44), Node(4), Node(0), Node(55)]

sortedItems = sorted(items, reverse=True)

newItems = list(map(lambda x: x.value * 3, sortedItems))
print(newItems)

print(list(filter(lambda x: x % 2 == 0, newItems)))

for i, obj in enumerate(sortedItems):
    print("i -- " + str(i))
    print("obj -- " + str(obj))
    print("-------")