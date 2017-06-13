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
        if value != None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:

    def __init__(self, head=None):
        self.head = head

    def head(self):
        return self.head

    def sorted_insert(self, value):
        lst = []
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

        current = self.head
        while current:
            lst.append(str(current.data))
            current = current.next_node

        print(sorted(lst, key=int))
