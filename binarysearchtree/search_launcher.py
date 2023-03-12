from binarysearchtreefactory import BinarySearchTreeFactory

if __name__ == "__main__":
    factory = BinarySearchTreeFactory()
    root = factory.make(("quick", "brown", "fox", "jumps", "over", "the", "lazy", "dogs", "back"))
    root.print_all()
