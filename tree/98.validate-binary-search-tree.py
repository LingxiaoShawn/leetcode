# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
    Goal: check if the given tree is a binary search tree
    Node: 
        For each node of binary search tree:
        1. The maximum of left subtree should be less than val of node
        2. The minimum of right subtree should be greater than val of node
"""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if self.isValidBST(root.left) and self.isValidBST(root.right):
            if root.left:
                node = root.left
                while node.right:
                    node = node.right
                if node.val >= root.val: return False
            if root.right:
                node = root.right
                while node.left:
                    node = node.left
                if node.val <= root.val: return False
            return True
        return False
