from tree.node.algorithms import NodeAlgorithms, NodeNofFoundException, NodeFunction
from tree.node.node import Node


class Tree:

    def __init__(self, value) -> None:
        self.__size = 1
        self.__depth = 1
        self.__root = Node(value, None)

    def get_size(self) -> int:
        return self.__size

    def add_node(self, value, function):
        target = NodeAlgorithms.find_self_left_right(self.__root, NodeFunction(function))
        if target:
            target.children.append(Node(value, target, target.depth + 1))
            self.__size = self.__size + 1
            self.__depth = max(self.__depth, target.depth + 1)
            return self
        else:
            raise NodeNofFoundException()

    def smart_print(self):
        print(self.__root)
        i = 1
        while i <= self.__depth:
            NodeAlgorithms.print_by_depth(self.__root, i)
            print()
            i = i + 1
