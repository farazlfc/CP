#https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n<=2:
            return 0
        a,b = min(A),max(A)
        diff = b - a
        def binomialCoef(n, k): 
            C = [[0 for x in range(k+1)] for x in range(n+1)] 
            for i in range(n+1): 
                for j in range(min(i, k)+1): 
                    # Base Cases 
                    if j == 0 or j == i: 
                        C[i][j] = 1
                    else: 
                        C[i][j] = C[i-1][j-1] + C[i-1][j] 
            return C[n][k] 
            
        if diff == 0:
            return (2**n - 1 - n - binomialCoef(n,2))
        dp = [defaultdict(list) for _ in range(n)]  #0 for start
        
        for i in range(1,n):
            for j in range(i):
                diff = A[i] - A[j]
                if len(dp[j][diff]) == 0:
                    dp[i][diff].append(1)
                else:
                    dp[i][diff].append(1)
                    for el in dp[j][diff]:
                        dp[i][diff].append(el+1)
        count = 0
        for index in dp:
            for key in index.keys():
                for element in index[key]:
                    if element > 1:
                        count+=1
        return count
