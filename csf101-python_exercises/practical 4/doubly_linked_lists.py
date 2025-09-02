class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_front(self):
        if not self.is_empty():
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            raise IndexError("List is empty")

    def delete_end(self):
        if not self.is_empty():
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            raise IndexError("List is empty")

    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return ' <-> '.join(map(str, elements))

    def display_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
        return ' <-> '.join(map(str, elements))

# Usage example
dll = DoublyLinkedList()
dll.insert_end(1)
dll.insert_end(2)
dll.insert_front(0)
print(dll.display_forward())   # Output: 0 <-> 1 <-> 2
print(dll.display_backward())  # Output: 2 <-> 1 <-> 0
dll.delete_front()
dll.delete_end()
print(dll.display_forward())   # Output: 1