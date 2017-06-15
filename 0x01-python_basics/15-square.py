#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        print("Retrieving the size")
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            print("Please only enter numbers for height")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(0, self.__size):
                print(self.__size * "#")
