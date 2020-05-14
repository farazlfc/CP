#https://leetcode.com/problems/sum-of-subsequence-widths/
class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        '''A[i] * (2 ^ i) means the positive effect of A[i] on res,
while A[i] * 2 ^ (n - i - 1) means the negative effect of A[i] on res.
Let us suppose we have: XXXX A[i] XXXX,
from A[i] to left, we have (2 ^ i) Subsequence, since the string is sorted , so for all these (2 ^ i) substring, A[i] is the largest, the contribution is A[i].
while from A[i] to right, we have 2 ^ (n - i - 1) Subsequence, so A[i] is the smallest for them, the contribution is -A[i].'''
        A = sorted(A) 
        n = len(A)
        #1 2 3 #
        sum_ = 0
        for i in range(n):
            sum_ += (2**i)*A[i] - ((2**(n-1 - i))*A[i]);
            
        return sum_%(10**9 + 7)
