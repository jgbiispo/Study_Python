class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value) -> bool:
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value) -> bool:
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self, node, result=None):
        if result is None:
            result = []

        if node is None:
            return result

        self.inorder(node.left, result)
        result.append(node.value)

        self.inorder(node.right, result)

        return result

    def preorder(self, node, result=None):
        if result is None:
            result = []

        if node is None:
            return result

        result.append(node.value)
        self.preorder(node.left, result)
        self.preorder(node.right, result)

        return result

    def postorder(self, node, result=None):
        if result is None:
            result = []

        if node is None:
            return result

        self.postorder(node.left, result)
        self.postorder(node.right, result)

        result.append(node.value)

        return result

    def height(self, node) -> int:

        if node is None:
            return -1

        left = self.height(node.left)
        right = self.height(node.right)

        return 1 + max(left, right)

    def count_nodes(self, node) -> int:

        if node is None:
            return 0

        left = self.count_nodes(node.left)
        right = self.count_nodes(node.right)

        return 1 + left + right

    def min_value(self, node):

        if node is None:
            return None

        if node.left is None:
            return node.value

        return self.min_value(node.left)


def run_test():
    bst = BinarySearchTree()

    for value in [10, 5, 15, 3, 7, 20]:
        bst.insert(value)

    print(bst.search(7))
    print(bst.search(99))
    print(bst.inorder(bst.root))
    print(bst.preorder(bst.root))
    print(bst.postorder(bst.root))
    print(bst.height(bst.root))

    bst2 = BinarySearchTree()
    bst2.insert(10)
    print(bst2.height(bst2.root))

    bst3 = BinarySearchTree()
    print(bst3.height(bst3.root))

    print(bst.count_nodes(bst.root))
    print(bst2.count_nodes(bst2.root))
    print(bst3.count_nodes(bst3.root))

    print(bst.min_value(bst.root))
    print(bst2.min_value(bst2.root))
    print(bst3.min_value(bst3.root))
