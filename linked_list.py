class Node:
    # an object for sorting a single node of a linked list
    # model 2 attributes - data and the link to the next in the list
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):  
        # this function will return a string when the object is being called
        return "<Node data: %s>" % self.data

class LinkedList:
    # Singly linked list
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        # Adds new node containing data at head of the list
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        # inserts a new node containing data at index position
        # insertion tales o(1) time but finding the node at the insertion point takes o(n) time
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head
            while position > 1:
                current = node.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node
            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        # Removes Node containing data that matches the key
        # Returns the node or None if key doesnt exist
        # Takes o(n) time
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def remove_at_index(self, index):
        # Removes Node at specified index
        # Takes o(n) time
        if index >= self.__count:
            raise IndexError('index out of range')
        current = self.head
        if index == 0:
            self.head = current.next_node
            self.__count -= 1
            return current
        position = index
        while position > 1:
            current = current.next_node
            position -= 1
        prev_node = current
        current = current.next_node
        next_node = current.next_node
        prev_node.next_node = next_node
        self.__count -= 1
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
            return current
            
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next_node


    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '-> '.join(nodes)
