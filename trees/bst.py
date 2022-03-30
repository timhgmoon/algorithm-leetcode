
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def searchBST(self, root, val):
        if root == None or root.val == val:
            return root
        if val > root.val:
            return self.searchBST(root.right, val)
        
        return self.searchBST(root.left, val)


tree = TreeNode(4)
tree.left = TreeNode(2)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right = TreeNode(7)

val = 2

print(tree.searchBST(tree, val))