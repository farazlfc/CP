#https://leetcode.com/problems/minimum-falling-path-sum-ii/
#Given a square grid of integers arr, a falling path with non-zero shifts is a choice of exactly one element from each row of arr, such that no two elements chosen in adjacent rows are in the same column.

#Return the minimum sum of a falling path with non-zero shifts.

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n,m = len(arr),len(arr[0])
        new_arr = []
        for ARR in arr:
            temp = []
            for i in range(m):
                temp.append([ARR[i],i])
            temp = sorted(temp, key = lambda x: x[0])
            new_arr.append(temp[:2])
        temp = new_arr
        index = [[None for _ in range(2)] for _ in range(n)]
        sum_ = [[float("inf") for _ in range(2)] for _ in range(n)]
        sum_[0][0] = temp[0][0][0]
        sum_[0][1] = temp[0][1][0]
        index[0][0] = temp[0][0][1]
        index[0][1] = temp[0][1][1]
        #sum_ = [[0 for _ in range(2)] for _ in range(n)]
        for i in range(1,n):
            if temp[i][0][1] != index[i-1][0]:  #ith row index, first prior.
                sum_[i][0] = sum_[i-1][0] + temp[i][0][0]
                index[i][0] = temp[i][0][1]
            else:
                sum_[i][0] = sum_[i-1][1] + temp[i][0][0]   #cuz minima of 2
                index[i][0] = temp[i][0][1]
            if temp[i][1][1] != index[i-1][0]:
                sum_[i][1] = sum_[i-1][0] + temp[i][1][0]   #one will satsify
                index[i][1] = temp[i][1][1]
            else:
                sum_[i][1] = sum_[i-1][1] + temp[i][1][0]
                index[i][1] = temp[i][1][1]
            if sum_[i][1] < sum_[i][0]:   #final check, first priority to '0' index
                sum_[i][0],sum_[i][1] = sum_[i][1],sum_[i][0]
                index[i][0],index[i][1] = index[i][1],index[i][0]
        return min(sum_[-1][0],sum_[-1][1])
                


