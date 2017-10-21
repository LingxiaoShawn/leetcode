# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
    Goal: convert a sorted linked list into a binary tree
    Idea: Build a tree with specific height and #n_leaves using DFS, iteratively.
          Insert the value to the node when visit the node second time.
"""
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # check condition of head
        if not head: return None
        if not head.next: return TreeNode(head.val)
        # traverse the list and save values
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        vals = list(reversed(vals))
        # build a tree with n_leaves and height
        temp = len(vals)
        heightMinus1 = -1
        while temp:
            heightMinus1 += 1
            temp >>= 1
        n_leaves = len(vals) + 1 - 2**heightMinus1
        # traverse and build tree using DFS
        bbt = TreeNode(0)
        bbt.height = 1
        stack = [bbt]
        cur_n_leaves = 0
        while stack:
            cur_node = stack.pop()
            if hasattr(cur_node, 'visited'):
                # If the node has been visited, we pop out an element 
                # and assign to this node
                cur_node.val = vals.pop()
            else: 
                # If the node hasn't been visited, create new children
                # if the height and #nodes haven't been exceeded. And 
                # add them into stack
                cur_node.visited = True
                if cur_node.height < heightMinus1:
                    temp1=cur_node.right = TreeNode(0)
                    temp2=cur_node.left = TreeNode(0)
                    temp1.height=temp2.height = cur_node.height + 1
                    stack.append(temp1)
                    stack.append(cur_node)
                    stack.append(temp2)
                elif cur_node.height == heightMinus1:
                    if cur_n_leaves < n_leaves:
                        temp=cur_node.right = TreeNode(0)
                        temp.height = cur_node.height + 1
                        cur_n_leaves += 1
                        stack.append(temp)
                    stack.append(cur_node)
                    if cur_n_leaves < n_leaves:
                        temp=cur_node.left = TreeNode(0)
                        temp.height = cur_node.height + 1
                        cur_n_leaves += 1
                        stack.append(temp)
                else:
                    stack.append(cur_node)
        return bbt

