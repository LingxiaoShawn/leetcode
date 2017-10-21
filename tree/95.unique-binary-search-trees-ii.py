# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree_copy(self, root_src, bias):
        if root_src:
            root_dst = TreeNode(bias + root_src.val)
            root_dst.left = self.tree_copy(root_src.left, bias)
            root_dst.right = self.tree_copy(root_src.right, bias)
            return root_dst
        return None
           
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        if n == 1: return [TreeNode(1)]
        results = [None for _ in range(n+1)]
        results[0] = [None]     # This None is important for upcoming loop
        results[1] = [TreeNode(1)]
        for i in xrange(2, n+1):
            results[i] = []
            for j in xrange(i):
                for rightNode in results[i-1-j]:
                    new_rightNode = self.tree_copy(rightNode,j+1)
                    for leftNode in results[j]:
                        tree = TreeNode(j+1)
                        tree.left = leftNode
                        tree.right = new_rightNode
                        results[i].append(tree)
    

        return results[n]
