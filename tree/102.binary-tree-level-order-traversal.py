# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        result = []
        level_stack=deque([root])
        
        while level_stack:
            next_level_stack = deque([])
            cur_level_vals = []
            result.append(cur_level_vals)
            while level_stack:
                cur_node = level_stack.popleft()
                cur_level_vals.append(cur_node.val)
                if cur_node.left: next_level_stack.append(cur_node.left)
                if cur_node.right: next_level_stack.append(cur_node.right)
            level_stack = next_level_stack
            
        return result
