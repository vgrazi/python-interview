class Node:
    def __init__(self, label, leftChild, rightChild):
        self.__rightChild = rightChild
        self.__label = label
        self.__leftChild = leftChild

    def __str__(self) -> str:
        return f"{super().__str__()} {self.__label}"

    def get_label(self):
        return self.__label

    def get_left_child(self):
        return self.__leftChild

    def set_left_child(self, node):
        self.__leftChild = node

    def get_right_child(self):
        return self.__rightChild

    def set_right_child(self, node):
        self.__rightChild = node

    def print_all(self):
        print(self.__label)
        if self.__leftChild is None:
            print(None)
        else:
            self.__leftChild.print_all()
        if self.__rightChild is None:
            print(None)
        else:
            self.__rightChild.print_all()


