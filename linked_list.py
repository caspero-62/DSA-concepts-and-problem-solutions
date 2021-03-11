class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    #initialize linked list's head to be None
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        #create a new node from the data to be appended
        new_node = Node(data)
        current = self.head
        # satisfy the following condition if linked list has
        # a head already, otherwise make the new node the head
        if self.head:
            #loop through the linked list and append the new list to the end. 
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
        if previous and current.value == data:
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

    def getPositionValue(self, position):
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
print(my_list.getPositionValue(3))
my_list.delete(1)
print(my_list.getLength())
print(my_list.displayList())
print(my_list.getPositionValue(3))

        
