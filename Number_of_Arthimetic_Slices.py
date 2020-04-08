#https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n<=2:
            return 0
        a,b = min(A),max(A)
        diff = b - a
            
        if diff == 0:
            return (2**n - 1 - n - (n*(n-1))//2)
        dp = [defaultdict(list) for _ in range(n)]  #0 for start
        count = 0
        for i in range(1,n):
            for j in range(i):
                diff = A[i] - A[j]
                if len(dp[j][diff]) == 0:
                    dp[i][diff].append(1)
                else:
                    dp[i][diff].append(1)
                    for el in dp[j][diff]:
                        count+=1
                        dp[i][diff].append(el+1)
        return count
                
