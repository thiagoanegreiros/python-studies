class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self) -> int:
        return self.size

    def append(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            head = self.head
            while head.next:
                head = head.next
            head.next = Node(val)
            self.size += 1

    def __getitem__(self, i):
        if self.size < i-1 or i < 0:
            raise ValueError('Invalid index')

        curr = self.head
        for _ in range(i):
            curr = curr.next

        return curr.value

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

print(len(ll))       # 3
print(ll[0])         # 10
print(ll[1])         # 20
print(ll[2])         # 30
