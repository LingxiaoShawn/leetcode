# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

''' 
    Goal: Sum two linked-list represented non-neative integers together. 
    Note: How to process the end of linked list is the key point.
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        temp_node = result
        while l1 != None or l2 != None:
            if l1 == None: l1 = ListNode(0)     # Add new node to escape dirty 
            if l2 == None: l2 = ListNode(0)     # ending of linked list
            q, r = divmod(temp_node.val + l1.val + l2.val, 10)
            temp_node.val = r
            if l1.next != None or l2.next != None or q != 0: # Stop condition
                temp_node.next = ListNode(q)
                temp_node = temp_node.next
            l1 = l1.next
            l2 = l2.next

        return result