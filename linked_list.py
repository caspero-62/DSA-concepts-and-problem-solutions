class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, data):
        current = self.head
        previous = None
        while current.value != data and current.next:
            previous = current
            current = current.next
        if current.value == data:
            previous.next = current.next
        else:
            self.head = current.next

    def insert(self, data, position):
        new_node = Node(data)
        current = self.head
        count = 1
        
        if position > 1:
            while current and position > count:
                if count == position - 1:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
                count += 1
        elif position == 1:
            new_node.next = self.head
            self.head = new_node
              

    def displayList(self):
        current = self.head
        linked_list = []
        while current:
            linked_list.append(current.value)
            current = current.next
        return linked_list

    def getLength(self):
        current = self.head
        total = 0
        while current:
            total += 1
            current = current.next
        return total

    def getPosition(self, position):
        current = self.head
        count = 1
        if position < 1:
            return 'invalid position'
        while current:
            if count == position:
                return current.value         
            count += 1
            current = current.next
        return 'Position not found'

my_list = LinkedList(Node(1))
my_list.append(2)
my_list.append(4)
print(my_list.getLength())
print(my_list.displayList())
my_list.insert(3, 3)
print(my_list.getLength())
print(my_list.displayList())
print(my_list.getPosition(3))
my_list.delete(2)
print(my_list.getLength())
print(my_list.displayList())

        
