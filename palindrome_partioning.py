#Given a string s, partition s such that every substring of the partition is a palindrome.
#Return the minimum cuts needed for a palindrome partitioning of s.
#The definition of 'cut' array is the minimum number of cuts of a sub string. More specifically, cut[n] stores the cut number of string s[0, n-1].



class Solution(object):
    def minCut(self, s):
        
        ## at cut[i] indicates the number of minimum cuts of s[i:j)
        cut = [-1] + [x for x in range(len(s))]  #max cuts in a string of length n = n-1;
        
        dp = [[False] * (len(s)+1) for _ in range(len(s)+1)]
        
        
        for length in range(len(s)):
            for start in range(len(s) - length):
                end = start + length
                if length == 0: dp[start][end] = True
                elif length == 1: dp[start][end] = s[start] == s[end]
                else: dp[start][end] = dp[start+1][end-1] and s[start] == s[end]
        
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j][i-1]: 
                    cut[i] = min(cut[i],cut[j]+1)
        return cut[-1]
