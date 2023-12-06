#код бінарного дерева

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
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
        self._inorder_travelsal_recursive(self.root)

    def _inorder_travelsal_recursive(self, current_node):
        if current_node is not None:
            self._inorder_travelsal_recursive(current_node.left)
            print(current_node.value)
            self._inorder_travelsal_recursive(current_node.right)

    def search(self, value):
        return self._search_recursive(value, self.root)

    def _search_recursive(self, value, current_node):
        if current_node is None:
            return False
        elif current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursive(value, current_node.left)
        else:
            return self._search_recursive(value, current_node.right)

    def find_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value