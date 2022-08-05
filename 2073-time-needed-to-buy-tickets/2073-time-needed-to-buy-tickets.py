class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        n=tickets[k]
        if (n==0):
            return 0
        seconds=0
        for j in range(len(tickets)):
            if (tickets[j]>0):
                if (j>k):
                    if(tickets[j]>=n):
                        seconds-=1
                if (tickets[j]-n>=0):
                    seconds+=n
                    tickets[j]-=n
                else:
                    seconds += tickets[j]
                    tickets[j]=0
                

        return seconds
            
        