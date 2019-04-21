class Node:
    """
    An object for storing a single node in a linked list.
    Models two attributes - data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

    
class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of node in the list.
        Runs in O(n) time.
        """

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds new node containing data at the head of the list.
        Takes O(1) time.
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key.
        Returns the node or 'None' if not found.
        Takes O(n) time
        """
        
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(l) time but finding the node at insertion point takes O(n) time.
        
        Overall, takes O(n) time
        """
        
        if index == 0:
            self.add(data)
        elif index > 0:
            newNode = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            previous = current
            nextNode = current.next_node

            previous.next_node = newNode
            newNode.next_node = nextNode

    def remove(self, key):
        """
        Removes node containing data that matches the key
        Returns the node or 'None' if the key is not found

        Takes O(n) time
        """
        
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data is key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data is key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time
        """

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

