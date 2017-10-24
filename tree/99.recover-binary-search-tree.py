# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
    Goal: recover the binary search tree which has two elements exchanged.
    Idea: 
          1.Just like sorted linked list, both moving-forward one and moving
          -backward one will make mistake when comparing with the elements
          between the moved position and orignal position. And when we tra-
          verse the binary search tree inorder, it's just the same as the
          sorted linked list.(Notice that the two positions can be adjacent!)
          2. Morris Traversal can achieve O(1) space cost. 
"""
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return None
        INF = 1e10
        visited_node= TreeNode(-INF)
        wrong_node1 = wrong_node2 = None
        wrong_node1_next = None
        stack = []
        cur_node = root
        while stack or cur_node:
            if cur_node:
                # first go left and push all node into stack(this is the
                # first-time visit for each node)
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                # once reach the left-bottom None, pop out node from stack,
                # which is the second time visit for the popped node
                cur_node = stack.pop()
                # find the inorder node
                if visited_node.val >= cur_node.val:
                    if not wrong_node1:
                        wrong_node1 = visited_node
                        wrong_node1_next = cur_node
                    else:
                        wrong_node2 = cur_node
                        break
                visited_node = cur_node
                # after that we will go right, start to find next inorder node
                # (root --> the deepest left(None) --> back one step(found inorder node)
                # --> assign its right node as root)
                cur_node = cur_node.right

        if wrong_node1:
            # These two exchanged positions are adjacent in inorder traversal
            if not wrong_node2: wrong_node2 = wrong_node1_next 
            temp = wrong_node1.val
            wrong_node1.val = wrong_node2.val
            wrong_node2.val = temp

        return None
