# Markhus Dammar
# 3/5/2020
# This is the class structure for Stack and Queue

from SLL import LinkedList


class Stack:
    def __init__(self):
        self.myList = LinkedList()

    def push(self, data):
        self.myList.prepend(data)

    def pop(self, data):
        return self.myList.remove_head(data)


class Queue:
    def __init__(self):
        self.myList = LinkedList()

    def push(self, data):
        self.myList.append(data)

    def pop(self, data):
        return self.myList.remove_head(data)
