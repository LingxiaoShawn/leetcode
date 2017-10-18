# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
    Goal: Merge two sorted linked list.
    Note: The hardest parts:
            1. End of each list.
            2. Stop condition.
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Check l1 and l2
        if l1 == None: return l2
        if l2 == None: return l1

        # l1 and l2 are non-empty lists
        INF = 1e10
        start=end = ListNode(0)
        a = l1
        b = l2
        
        # merge two lists iteratively
        while True:
            while a.val <= b.val:
                end.next = a
                end = end.next
                a = a.next
                # Two tricks：
                #   1. Use an node with INF value as the NULL end 
                #      of each list to make inner while condition works.
                #   2. Put stop condition of the outer while inside
                #      the inner while loop. 
                if a == None:
                    if b.val >= INF:
                        return start.next
                    a = ListNode(INF)
            # Below can be used to remove the bottom loop, but will increase running time.
            # temp = a
            # a = b
            # b = temp
            while b.val <= a.val:
                end.next = b
                end = end.next
                b = b.next
                if b == None: 
                    if a.val >= INF:
                        return start.next
                    b = ListNode(INF)
        return start.next
