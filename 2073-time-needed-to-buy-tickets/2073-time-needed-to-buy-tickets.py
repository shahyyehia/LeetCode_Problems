class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        n=tickets[k]
        if (n==0):
            return 0
        seconds=0
        for i in range(n):
            for j in range(len(tickets)):
                if tickets[k]==0:
                    if j>k:
                        break
                if (tickets[j]>0):
                    seconds+=1
                    tickets[j]-=1
            print(tickets)
        return seconds
        