#https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

class Solution(object):
    def minCost(self, n, cuts):
        c=len(cuts)
        cuts.sort()
        cuts.insert(0,0)
        cuts.append(n)
        dp=[[-1]*(c+1) for _ in range(c+1)]

        def recur(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini=float('inf')
            for ind in range(i,j+1):
                cost=cuts[j+1]-cuts[i-1]+recur(i,ind-1)+recur(ind+1,j)
                mini=min(mini,cost)
            dp[i][j]=mini
            return mini
        return recur(1,c)
        