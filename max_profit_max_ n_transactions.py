def maxProfit(self, A):
        n = len(A)
        if n == 0:
            return 0
        if n==1:
            return 0
        if n ==2:
            return max(0, A[1]- A[0])
        dp = [[[float("-inf") for _ in range(2)] for _ in range(2)] for _ in range(n)]
        maximum = 0
        dp[0][0][0] = -A[0]     #buy
        dp[1][0][0] = max(dp[0][0][0] , -A[1])
        dp[1][0][1] = dp[0][0][0] + A[1]
        maximum = max(maximum,dp[1][0][1])
        for i in range(2,n):
            dp[i][0][0] = max(dp[i-1][0][0] , -A[i])  #0_Buy
            dp[i][0][1] = max(dp[i-1][0][1] , dp[i-1][0][0] + A[i]) #0_sell
            maximum = max(maximum, dp[i][0][1])
            dp[i][1][0] = max(dp[i-1][1][0],dp[i-1][0][1] - A[i]) #1_buy
            dp[i][1][1] = max(dp[i-1][1][1] , dp[i-1][1][0] + A[i]) #1_sell = 2 transactions
            maximum = max(maximum, dp[i][1][1])
        return(maximum)
