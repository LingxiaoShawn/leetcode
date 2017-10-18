# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        if not head.next: return head
        if k == 0: return head

        length = 1
        pointer = head
        while pointer.next:
            length += 1
            pointer = pointer.next

        k = k % length
        if k == 0: return head
       
        pointer.next = head
        for _ in range(length - k):
            pointer = pointer.next
       
        head = pointer.next
        pointer.next = None

        return head
