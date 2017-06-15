class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:

    def __init__(self, head=None):
        self.head = head

    def head(self):
        return self.head

    def sorted_insert(self, value):
        new_node = Node(value)
        curr = self.head

        if curr is None:
            self.head = new_node

        elif curr.data > value:
            new_node.next_node = curr
            self.head = new_node

        else:
            while curr.next_node is not None:
                if curr.next_node.data > value:
                    break
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        s = ""
        curr = self.head
        while curr:
            s += str(curr.data)
            if curr.next_node is not None:
                s += '\n'
            curr = curr.next_node
        return s
