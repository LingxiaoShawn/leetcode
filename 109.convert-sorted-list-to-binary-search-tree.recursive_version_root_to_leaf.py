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

class Solution(object):
    def construct_subtree(self,sublist):
        if len(sublist) <= 0:
            return None
        mid_index = len(sublist) // 2
        root = TreeNode(sublist[mid_index])
        root.left = self.construct_subtree(sublist[:mid_index])
        root.right = self.construct_subtree(sublist[mid_index+1:])
        return root 
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # find the middle point of the linked list
        if not head: return None
        if not head.next: return TreeNode(head.val)
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return self.construct_subtree(vals)
