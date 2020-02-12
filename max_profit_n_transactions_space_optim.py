def maxProfit(self, A):
        n = len(A)
        if n == 0:
            return 0
        if n==1:
            return 0
        if n ==2:
            return max(0, A[1]- A[0])
        dp = [[[float("-inf") for _ in range(2)] for _ in range(2)] for _ in range(2)]
        flag = 1
        maximum = 0
        dp[flag^1][0][0] = -A[0]     #buy
        dp[flag][0][0] = max(dp[flag^1][0][0] , -A[1])
        dp[flag][0][1] = dp[flag^1][0][0] + A[1]
        maximum = max(maximum,dp[flag^1][0][1])
        flag = flag^1
        #dp.pop(0)
        #dp.append([[float("-inf") for _ in range(2)] for _ in range(2)])
        for i in range(2,n):
            dp[flag][0][0] = max(dp[flag^1][0][0] , -A[i])  #0_Buy
            dp[flag][0][1] = max(dp[flag^1][0][1] , dp[flag^1][0][0] + A[i]) #0_sell
            maximum = max(maximum, dp[flag][0][1])
            dp[flag][1][0] = max(dp[flag^1][1][0],dp[flag^1][0][1] - A[i]) #1_buy
            dp[flag][1][1] = max(dp[flag^1][1][1] , dp[flag^1][1][0] + A[i]) #1_sell = 2 transactions
            maximum = max(maximum, dp[flag][1][1])
            flag = flag^1
        return(maximum)