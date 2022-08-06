class Solution(object):
    def isMonotonic(self, nums):
        original=[]
        dec=[]
        for i in range(len(nums)):
            original.append(nums[i])
            dec.append(nums[i])
        nums.sort()
        dec.sort(reverse=True)
        def equalss(list1,list2):
            for i in range(len(list1)):
                if list1[i]!=list2[i]:
                    return False
            return True
        equalss(original,dec)
        if equalss(original,nums) or equalss(original,dec):
            return "true"
        else:
            return False
        
        
        