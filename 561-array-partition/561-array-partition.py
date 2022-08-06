class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        sums=0
        for i in range(0,len(nums),2):
            if nums[i]<=nums[i+1]:
                sums+=nums[i]
            else:
                sums+=nums[i+1]
        return sums
        