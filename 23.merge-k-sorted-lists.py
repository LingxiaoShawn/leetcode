# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
    Goal: Merge K sorted lists into one sorted lists.
    Note: still have trouble in time tradeoff. 
'''
class Solution(object):

    @staticmethod
    def firstNode_list_insert (firstNode_list, firstNode):
        list_pointer=parent= firstNode_list
        while firstNode.val > list_pointer.val.val:
            parent = list_pointer
            list_pointer = list_pointer.next
        parent.next = ListNode(firstNode)
        parent.next.next = list_pointer
        return None

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # check conditions of lists
        if lists == None: return None
        lists = [x for x in lists if x != None]
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
 
        # Idea: maintain a sorted linked list of k first nodes of given k sorted list.

        # Step 1: construct a sorted linked list of length k. 
        INF = 1e10
        # init a sorted list
        firstNode_list = ListNode(ListNode(-INF))
        firstNode_list.next = ListNode(ListNode(INF))
       
        # insert firstNode of all lists into the maintained sorted list
        for firstNode in lists:
            # Insert firstNode into firstNode_list
            self.firstNode_list_insert(firstNode_list, firstNode)

        # init combined list
        combined_list = ListNode(0)

        # traverse each list according to the order in firstNode_list
        combined_list_end = combined_list
        temp_node = firstNode_list.next.val
        while temp_node.val < INF:
            traversing_list = temp_node
            # delete the traversing firstNode from firstNode_list
            firstNode_list.next = firstNode_list.next.next
            temp_node = firstNode_list.next.val
            # length 1 traversing_list
            if traversing_list.next == None:
                combined_list_end.next = traversing_list
                combined_list_end = combined_list_end.next
            else:
                # add nodes of traversing list into combined_list
                while traversing_list != None and traversing_list.val <= temp_node.val:
                    combined_list_end.next = traversing_list
                    combined_list_end = combined_list_end.next
                    traversing_list = traversing_list.next
                # add the new first node of traversing list into firstNode_list
                if traversing_list != None:
                    self.firstNode_list_insert(firstNode_list, traversing_list)
            
        return combined_list.next

       

