from PyPDF2 import PageRange

from tree.node.algorithms import NodeAlgorithms, NodeNofFoundException, NodeFunction
from tree.node.node import Node
from tree.pdf_merger import PdfMerger


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

    def build_pdf(self):
        print("the result is {}".format(self.child_left_right_self(self.__root)))

    @staticmethod
    def child_left_right_self(node: Node):
        if not node:
            return None
        if not node.children:
            # return current one file url
            return node.value.source

        child_files = []
        for child in node.children:
            child_pdf = Tree.child_left_right_self(child)
            if child_pdf:
                child_files.append(child_pdf)

        file_name = "file-{}".format(node.value.source)
        child_pdfs = "file-{}-children".format(node.value.source)

        if len(child_files) == 1:
            child_pdfs = child_files[0]
        else:
            merger = PdfMerger()
            for pdf in child_files:
                merger.append(pdf, bookmark=pdf)
            merger.write(child_pdfs)

        merger = PdfMerger()
        merger.append(node.value.source, bookmark='main')
        merger.append(child_pdfs, pages=PageRange(':'), bookmark='children')
        merger.write(file_name)
        merger.close()

        return file_name

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
