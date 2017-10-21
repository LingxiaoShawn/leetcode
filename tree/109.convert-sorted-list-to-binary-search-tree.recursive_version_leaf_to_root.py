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
    This solution is too tricky! 
    Note:
        1.Recursive algorithm <==> Mathematical Induction
        2.Any subtree is constructed with successive elements on the 
        original linked list. 
"""
class Solution(object):
    """
        Intead of using global variable self.head, we can also change API
        of construct_binary_subtree method as:(which will be more clear)
        Args:
            start_head(ListNode): the starting point of linked list 
            n(int): the length that will be #nodes in subtree
        Returns:
            end_head(ListNode): the node of start_head going next with n times
            root(TreeNode): the constructed subtree based on element between
                            start_head and end_head
    """
    def construct_binary_subtree(self,n):
        if n <= 0:
            return None
        # First construct left subtree, notice that head will
        # moved to the middle of the linked list after that!
        left_subtree = self.construct_binary_subtree(n//2)   # 这里的n//2用来表明head向后移动了n//2+1步
        root = TreeNode(self.head.val)
        root.left = left_subtree
        # Next step is the most important step!
        self.head = self.head.next
        root.right = self.construct_binary_subtree(n-1-n//2) # 这里的输入用来表明list的剩余长度
        return root
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.head = head
        n = 0
        # calculate length of linked list
        while head:
            n += 1
            head = head.next
        return self.construct_binary_subtree(n)
