from node import Node


def add_node(parent, node):
    if(node.get_label()< parent.get_label()):
        subnode = parent.get_left_child()
        if subnode is None:
            parent.set_left_child(node)
        else:
            add_node(subnode, node)
    else:
        subnode = parent.get_right_child()
        if subnode is None:
            parent.set_right_child(node)
        else:
            add_node(subnode, node)

class BinarySearchTreeFactory :

    def build(self, data):
        root = None
        for label in data:
            node = Node(label, None, None)
            if root is None:
                root = node
            else:
                add_node( root, node)
        return root




