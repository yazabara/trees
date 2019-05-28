from pdf_data import PdfData
from tree.tree import Tree

if __name__ == '__main__':
    tree = Tree(PdfData("root.pdf"))
    tree \
        .add_node(PdfData("first.pdf"), lambda node: "root.pdf" == node.value.source) \
        .add_node(PdfData("result1.pdf"), lambda node: "root.pdf" == node.value.source) \
        .add_node(PdfData("result2.pdf"), lambda node: "root.pdf" == node.value.source) \
        .add_node(PdfData("test.pdf"), lambda node: "result2.pdf" == node.value.source) \
        .add_node(PdfData("second.pdf"), lambda node: "result1.pdf" == node.value.source) \
        .add_node(PdfData("second.pdf"), lambda node: "result2.pdf" == node.value.source)

    tree.print_tree_by_depths()
    tree.build_pdf()
