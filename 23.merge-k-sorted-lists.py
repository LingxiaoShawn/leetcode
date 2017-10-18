# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import *
'''
Goal:
    Merge K sorted lists into one sorted lists.
Note:
    Used a priority queue to save all first nodes of k lists, and traverse
    each list according to its order in the list. Each traversing will end 
    once current value is larger than the value of the top node of the queue.
    And if the traversing list doesn't end, it will be added into the queue.
        * PriorityQueue is a wrapped threadsafe implementation of heapq.
Complexity analysis:
    The complexity of the algorithm is O(N+C*log(k)),
    where N is the total number of nodes in all lists, k is the number 
    of lists, C is the number of change point in the combined lists.
    Bescially C < N, but in worst case C = N. For small number of k and 
    large N, C will << N in the average situation.
'''
class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """ New version, using default PriorityQueue
        """
        # check conditions of lists
        lists = [(x.val, x) for x in lists if x != None]    # O(k)
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0][1]

        # init combined list 
        combined_list=point = ListNode(0)
        # init a heapq
        q = []
        # insert first node of all lists into the queue
        INF = 1e10
        for item in lists:      # O(k) for building heap
            heappush(q, item) 
        heappush(q,(INF, ListNode(INF)))

        # traverse each list according to their order in the queue
        next_node_val, next_node = heappop(q)
        while next_node_val < INF:  # O(N) for traversing all nodes
            cur_node = next_node
            next_node_val, next_node = heappop(q)
            # add suitable node from cur_node(list) to combined_list
            while cur_node and cur_node.val <= next_node_val:
                point.next = cur_node
                point = point.next
                cur_node = cur_node.next
            if cur_node: heappush(q,(cur_node.val, cur_node))   # O(C*log(k))
        return combined_list.next

        """Old version
        # Ok the commented version actually implemented a PriorityQueue but not 
        # efficient than(actually pretty slow) than python default PriorityQueue.
        """

        ## Idea: maintain a sorted linked list of k first nodes of given k sorted list.

        ## Step 1: construct a sorted linked list of length k. 
        #INF = 1e10
        ## init a sorted list
        #firstNode_list = ListNode(ListNode(-INF))
        #firstNode_list.next = ListNode(ListNode(INF))
       
        ## insert firstNode of all lists into the maintained sorted list
        #for firstNode in lists:
        #    # Insert firstNode into firstNode_list
        #    self.firstNode_list_insert(firstNode_list, firstNode)

        ## init combined list
        #combined_list = ListNode(0)

        ## Step 2: traverse each list according to the order in firstNode_list
        #combined_list_end = combined_list
        #temp_node = firstNode_list.next.val
        #while temp_node.val < INF:
        #    traversing_list = temp_node
        #    # delete the traversing firstNode from firstNode_list
        #    firstNode_list.next = firstNode_list.next.next
        #    temp_node = firstNode_list.next.val
        #    # length 1 traversing_list
        #    if traversing_list.next == None:
        #        combined_list_end.next = traversing_list
        #        combined_list_end = combined_list_end.next
        #    else:
        #        # add nodes of traversing list into combined_list
        #        while traversing_list != None and traversing_list.val <= temp_node.val:
        #            combined_list_end.next = traversing_list
        #            combined_list_end = combined_list_end.next
        #            traversing_list = traversing_list.next
        #        # add the new first node of traversing list into firstNode_list
        #        if traversing_list != None:
        #            self.firstNode_list_insert(firstNode_list, traversing_list)
            
        #return combined_list.next

       

