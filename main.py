from tree.tree import Tree

if __name__ == '__main__':
    tree = Tree("1")
    tree \
        .add_node("2", lambda node: "1" == node.value) \
        .add_node("3", lambda node: "1" == node.value) \
        .add_node("4", lambda node: "1" == node.value) \
        .add_node("5", lambda node: "1" == node.value) \
        .add_node("6", lambda node: "1" == node.value)
    print(tree.get_size())
    tree \
        .add_node("7", lambda node: "2" == node.value) \
        .add_node("13", lambda node: "7" == node.value) \
        .add_node("14", lambda node: "7" == node.value) \
        .add_node("8", lambda node: "3" == node.value) \
        .add_node("9", lambda node: "4" == node.value) \
        .add_node("10", lambda node: "5" == node.value) \
        .add_node("11", lambda node: "6" == node.value) \
        .add_node("12", lambda node: "6" == node.value)
    print(tree.get_size())
    print("---------- ||| ----------")
    print(tree.print_tree_by_depths())

