# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Assume n will always be valid 
        a=b = head
        # To simulate a beginning node to avoid dirty checking
        a_parent = ListNode(0)
        a_parent.next = a
        # Construct b
        for _ in range(n):
            b = b.next
        # Now update a and b simultaneously
        while b != None:
            a_parent = a 
            a = a_parent.next
            b = b.next
        # Now delete a
        if a_parent.next == head:
            head = a.next
        else:
            a_parent.next = a.next
         
        return head

