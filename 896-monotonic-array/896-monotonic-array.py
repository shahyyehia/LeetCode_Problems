class Solution(object):
    def isMonotonic(self, nums):
        original=[]
        dec=[]
        for i in range(len(nums)):
            original.append(nums[i])
            dec.append(nums[i])
        nums.sort()
        dec.sort(reverse=True)
        if original==nums or original==dec:
            return "true"
        else:
            return False
        
        
        