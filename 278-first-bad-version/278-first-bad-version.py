# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left=1
        right=n
       
        while(left<=right):
            mid=(right+left)//2
            if(isBadVersion(mid)):
                if(isBadVersion(mid-1)):
                    right=mid-1
                else:
                    break
            else:
                left=mid+1
        return mid
        
        