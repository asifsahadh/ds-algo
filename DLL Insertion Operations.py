# doubly linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, value):
            new_node = Node(value)
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, value): 
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def insert_at_pos(self, pos, value):
        new_node = Node(value)
        if pos == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        curr = self.head
        c = 0

        while curr and c < pos - 1:
            curr = curr.next
            c += 1

        new_node.next = curr.next
        new_node.prev = curr

        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node