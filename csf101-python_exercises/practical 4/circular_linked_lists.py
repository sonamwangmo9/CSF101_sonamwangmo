class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    def delete(self, key):
        if self.is_empty():
            return

        if self.head.data == key and self.head.next == self.head:
            self.head = None
        elif self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == key:
                    prev.next = current.next
                    break

    def display(self):
        if self.is_empty():
            return "List is empty"
        elements = []
        current = self.head
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return ' -> '.join(elements) + ' -> (back to start)'

# Usage example
cll = CircularLinkedList()
cll.insert_end(1)
cll.insert_end(2)
cll.insert_beginning(0)
print(cll.display())  # Output: 0 -> 1 -> 2 -> (back to start)
cll.delete(1)
print(cll.display())  # Output: 0 -> 2 -> (back to start)
