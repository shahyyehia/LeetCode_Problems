class Solution(object):
    def sortedSquares(self, nums):
        n = [i*i for i in (nums)]
        n.sort()
        return n
       