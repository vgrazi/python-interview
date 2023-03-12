from binarysearchtreefactory import BinarySearchTreeFactory


def find_node(param):
    pass


if __name__ == "__main__":
    factory = BinarySearchTreeFactory()
    root = factory.make(("quick", "brown", "fox", "jumps", "over", "the", "lazy", "dogs", "back"))
    find_node("brown")
    # root.print_all()
