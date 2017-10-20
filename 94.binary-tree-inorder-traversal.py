# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
    Goal: traverse a binary tree inorderly. Use iterative method.
    Note: Notice that the result of inorder traversal is exactly 
          matching the sequence of second-visited nodes in DFS!
"""
class Solution(object):
    #@staticmethod
    #def recur_tra(root, saved_list):
    #    if not root.left:
    #        recur_tra(root.left, saved_list)
    #    saved_list.append(root.val)
    #    if not root.right:
    #        recur_tra(root.right, saved_list)
    #    return None
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # First let's do the simplest version: recursive traversal
        if not root: return []
        #result = []
        #recur_tra(root, result)
        #return result

        # Another version is to use DFS traversal with secondary visit
        stack = [root]
        inorder_vals = []
        while stack:
            cur_node = stack.pop()
            # if the node has been visited, then we should add the val into result
            if hasattr(cur_node,'visited'):
                inorder_vals.append(cur_node.val)
            else: 
                # else, we should visit the node, append right node, itself, left node 
                # into the stack, and also mark the node as visited
                if cur_node.right: stack.append(cur_node.right)
                cur_node.visited = True
                stack.append(cur_node)
                if cur_node.left: stack.append(cur_node.left)
        return inorder_vals
