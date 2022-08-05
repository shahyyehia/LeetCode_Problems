class Solution(object):
    def longestCommonPrefix(self, strs):
        min=1000
        word=""
        for i in range(len(strs)):
            length=len(strs[i])
            if(length<min):
                min=length
                word=strs[i]
        found=0
        while (len(word)>0):
            for i in range(len(strs)):
                if word == strs[i][0:len(word)]:
                    found+=1
            if (found==len(strs)):
                break
            else:
                 word=word[:len(word)-1]
                 found=0
        return word