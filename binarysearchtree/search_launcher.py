from binarysearchtreefactory import BinarySearchTreeFactory


def find_node(startingNode, label):
    pass


if __name__ == "__main__":
    factory = BinarySearchTreeFactory()
    root = factory.build(("quick", "brown", "fox", "jumps", "over", "the", "lazy", "dogs", "back"))
    node = find_node("brown")
    print(node)
#                    quick
#                   /    \
#               brown    the
#              /    \
#            back   fox
#                  /    \
#                dog   jumps
#                          \
#                          over
#                          /
#                        lazy
