class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            j=0
            while j<i:
                dp[i]+=dp[i-1-j]*dp[j] #we are doing it relatively, rather than calculating the absolute values so we can look back on earlier calculated values
                j+=1#catalan numbers
        return dp[n]
