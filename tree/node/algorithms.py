from abc import ABC, abstractmethod

from tree.node.node import Node


class NodeNofFoundException(RuntimeError):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NodeAbstractFunc(ABC):

    @abstractmethod
    def apply(self, node: Node):
        raise NotImplementedError


class NodeFunction(NodeAbstractFunc):

    def __init__(self, function) -> None:
        super().__init__()
        self.function = function

    def apply(self, node: Node):
        return self.function(node)


class NodeAlgorithms:

    @staticmethod
    def do_smth_by_depth(node: Node, depth=1, do_func: NodeAbstractFunc = None):
        """
        Method goes through all nodes with rule:
        self node -> for each child in children [left -> right]
        :return: Node
        """
        if not do_func or not node:
            return

        if node.depth == depth:
            do_func.apply(node)

        if node.depth > depth:
            return

        for child in node.children:
            NodeAlgorithms.do_smth_by_depth(child, depth, do_func)

    @staticmethod
    def child_left_right_self(node: Node, do_func: NodeAbstractFunc):
        for child in node.children:
            NodeAlgorithms.child_left_right_self(child, do_func)
        do_func.apply(node)

    @staticmethod
    def do_self_left_right(node: Node, do_func: NodeAbstractFunc):
        """
        Method goes through all nodes with rule:
        self node -> for each child in children [left -> right]
        :return: Node
        """
        do_func.apply(node)
        for child in node.children:
            NodeAlgorithms.do_self_left_right(child, do_func)

    @staticmethod
    def find_self_left_right(node: Node, find: NodeAbstractFunc):
        """
        Method goes through all nodes with rule:
        self node -> for each child in children [left -> right]
        :return: Node
        """
        if find.apply(node):
            return node
        for child in node.children:
            result = NodeAlgorithms.find_self_left_right(child, find)
            if result is not None:
                return result
        return None
