class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class ArvoreBinariaTrivial:

    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = TreeNode(val)

        if not self.root:
            self.root = new_node
            return

        current = self.root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def array_to_bst_trivial(self, array):
        for val in array:
            self.insert(val)
        return self.root