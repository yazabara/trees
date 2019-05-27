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

    def print_tree_by_depths(self):
        print("----------------------------------------------------------------------------")
        print("Tree with node size = {} and depth = {} ".format(self.__size, self.__depth))
        print("Tree root: {}".format(self.__root))
        i = 1
        while i <= self.__depth:
            NodeAlgorithms.do_smth_by_depth(self.__root, i, NodeFunction(lambda node: print(node, end=' ')))
            print()
            i = i + 1
        print("----------------------------------------------------------------------------")
