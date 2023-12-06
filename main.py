# код бінарного дерева

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinareTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)
    def _insert_recursive(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(value, current_node.left)

        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(value, current_node.right)

    def inorder_travelsal(self):
            se

    def _inorder_travelsal_recursive(self, current_node):
        if current_node is not None:
            self._inorder_travelsal_recursive(current_node.left)
            print(current_node.value)
            self._inorder_travelsal_recursive(current_node.right)


