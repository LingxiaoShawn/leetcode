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
        cur_node = root
        while cur_node:
            if cur_node.left:
                # build or remove return path from the rightest leaf of the left subtree
                rightest_leaf = cur_node.left
                while rightest_leaf.right != None and rightest_leaf.right != cur_node:
                    rightest_leaf = rightest_leaf.right
                
                if rightest_leaf.right == None:
                    # build return path
                    rightest_leaf.right = cur_node
                    # then keep go left
                    cur_node = cur_node.left
                else:
                    # delete return path
                    rightest_leaf.right = None
                    # and cur_node should be added into inorder list
                    if visited_node.val > cur_node.val:
                        if not wrong_node1:
                            wrong_node1 = visited_node
                            wrong_node2 = cur_node
                        else:
                            wrong_node2 = cur_node
                            break
                    visited_node = cur_node
                    # then go right
                    cur_node = cur_node.right
            else:
                # reach the bottem 
                # add cur_node into inorder list
                if visited_node.val > cur_node.val:
                    if not wrong_node1:
                        wrong_node1 = visited_node
                        wrong_node2 = cur_node
                    else:
                        wrong_node2 = cur_node
                        break
                visited_node = cur_node
                # then go right
                cur_node = cur_node.right 
               
        if wrong_node1:
            temp = wrong_node1.val
            wrong_node1.val = wrong_node2.val
            wrong_node2.val = temp

        return None
