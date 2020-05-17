#https://leetcode.com/contest/biweekly-contest-26/problems/form-largest-integer-with-digits-that-add-up-to-target/
def largestNumber(self, cost: List[int], target: int) -> str:
    
    dp = [-1] * (target + 1)
    dp[0] = 0
    
    pruned = {}
    for i, c in enumerate(cost):
        pruned[c] = i + 1  
        
    for t in range(1, target + 1):
        sums = [dp[t - c] * 10 + d for c, d in pruned.items() if t - c >= 0]
        if sums: dp[t] = max(sums)  
            
    return "0" if dp[target] <= 0 else str(dp[target])

#Knapsack basically
