class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return 1
        nums_list = [1] * (n+1)
        for i in xrange(2,n+1):
            temp = j = 0
            for j in xrange(i//2):
                temp += nums_list[j] * nums_list[i-1-j]
            nums_list[i] = 2 * temp
            if i%2: nums_list[i] += nums_list[j+1]**2
        return nums_list[n]

